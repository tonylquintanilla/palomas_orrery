# Complete replacement for test_orbit_cache.py with proper isolation

"""
test_orbit_cache.py - Comprehensive test suite for orbit data caching and repair

This module tests the orbit data manager's caching functionality including:
- Loading and saving cache files
- Format conversion (old to new)
- Corruption detection and repair
- Incremental updates
- Edge cases and error handling

Run this module periodically to ensure cache functionality remains robust.

Its fixture files are written into a temporary folder, made when the
tests start and removed when they finish, so nothing is left in the
repository (L-448). Until 2026-10-15 they went to test_output/, and
test_output/test_orbit_paths.json, which git tracked, was rewritten on
every maintenance run.

Role: devtool
Domain: dev_tools

Module updated: October 15, 2026 with Anthropic's Claude Opus 5.5 (L-448:
the fixture is written into a temporary folder, removed when the tests
finish, instead of test_output/ in the repository.)
Module updated: October 29, 2026 with Anthropic's Claude Opus 5.5 (L-504,
first slice: TestUtcClock. The clock reads UTC through utc_clock; the
orbit cache's "fetched" stamp is read back in both forms, a planted old
one with no zone and a new one ending "+00:00"; no module on the data
path reads the local clock or asks JPL without cache=; each check shown
able to fail.)
Module updated: November 3, 2026 with Anthropic's Claude Opus 5.5 (L-476:
path_drawing.py, which asks JPL for a path by its plan, joins the data
path's modules.)
Module updated: November 4, 2026 with Anthropic's Claude Opus 5.5 (L-512,
slice a, part A1): TestFreshCalls, the fresh switch checked across the
whole repository on Python's parser (every call of vectors, elements or
ephemerides, or their _async forms, across line breaks, must pass
cache=HORIZONS_CACHE; a reference that is not a direct call is flagged; a
file that does not parse fails; non-JPL calls sit on NOT_JPL, printed
every run). It replaces the line-text check on DATA_PATH_MODULES, which
keep their clock checks. Registered in main(), whose last line names the
files and calls it examined. TestOrbitCache now tests functions of
orbit_data_manager.py marked DEPRECATED (data/orbit_paths.json retired).)
"""
import ast
import json
import os
import re
import shutil
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
import numpy as np
from unittest.mock import patch, MagicMock, Mock
import sys

# CRITICAL: DO NOT import orbit_data_manager at module level!
# We'll import it inside each test after setting up patches

class TestOrbitCache(unittest.TestCase):
    """Test suite for orbit data caching functionality"""

    @classmethod
    def setUpClass(cls):
        # L-448: a temporary folder outside the repository, removed in
        # tearDownClass, so a run leaves no file for git to see.
        cls.shared_dir = tempfile.mkdtemp(prefix="test_orbit_cache_")

    @classmethod
    def tearDownClass(cls):
        shutil.rmtree(cls.shared_dir, ignore_errors=True)

    def setUp(self):
        """Set up test environment before each test"""
        self.test_dir = self.shared_dir
            
        # Clear any existing test files
        for file in os.listdir(self.test_dir):
            file_path = os.path.join(self.test_dir, file)
            if os.path.isfile(file_path):
                os.unlink(file_path)
                
        self.test_cache_file = os.path.join(self.test_dir, "test_orbit_paths.json")
        
        # Create sample data for testing
        self.sample_new_format = {
            "Mars_Sun": {
                "data_points": {
                    "2025-01-01": {"x": 1.5, "y": 0.2, "z": 0.1},
                    "2025-01-02": {"x": 1.51, "y": 0.21, "z": 0.11},
                    "2025-01-03": {"x": 1.52, "y": 0.22, "z": 0.12}
                },
                "metadata": {
                    "start_date": "2025-01-01",
                    "end_date": "2025-01-03",
                    "center_body": "Sun",
                    "last_updated": "2025-01-01"
                }
            },
            "Jupiter_Sun": {
                "data_points": {
                    "2025-01-01": {"x": 5.2, "y": 0.3, "z": 0.15},
                    "2025-01-02": {"x": 5.21, "y": 0.31, "z": 0.16}
                },
                "metadata": {
                    "start_date": "2025-01-01",
                    "end_date": "2025-01-02",
                    "center_body": "Sun",
                    "last_updated": "2025-01-01"
                }
            }
        }
        
        self.sample_old_format = {
            "Venus_Sun": {
                "x": [0.72, 0.73, 0.74],
                "y": [0.1, 0.11, 0.12],
                "z": [0.05, 0.051, 0.052]
            },
            "Earth_Sun": {
                "x": [1.0, 1.01, 1.02],
                "y": [0.0, 0.01, 0.02],
                "z": [0.0, 0.001, 0.002]
            }
        }
        
    def tearDown(self):
        """Clean up test environment after each test"""
        # The temporary folder is removed once, after the last test
        # (tearDownClass). Here, just clean up the module.
        if 'orbit_data_manager' in sys.modules:
            del sys.modules['orbit_data_manager']
            
    def test_save_and_load_valid_cache(self):
        """Test saving and loading valid cache data"""
        # Patch BEFORE importing
        with patch.dict('os.environ', {'ORBIT_PATHS_FILE': self.test_cache_file}):
            # Now import with the patch active
            import orbit_data_manager
            
            # Override the constant
            orbit_data_manager.ORBIT_PATHS_FILE = self.test_cache_file
            
            # Save data
            orbit_data_manager.save_orbit_paths(self.sample_new_format, self.test_cache_file)
            
            # Verify file exists in test directory
            self.assertTrue(os.path.exists(self.test_cache_file))
            
            # Load the data
            loaded_data = orbit_data_manager.load_orbit_paths(self.test_cache_file)
            
            # Verify data matches
            self.assertEqual(loaded_data, self.sample_new_format)
            
    def test_load_nonexistent_file(self):
        """Test loading when cache file doesn't exist"""
        with patch.dict('os.environ', {'ORBIT_PATHS_FILE': self.test_cache_file}):
            import orbit_data_manager
            orbit_data_manager.ORBIT_PATHS_FILE = self.test_cache_file
            
            # Ensure file doesn't exist
            self.assertFalse(os.path.exists(self.test_cache_file))
            
            # Mock the status_display to avoid issues
            orbit_data_manager.status_display = None
            
            # Load should return empty dict
            loaded_data = orbit_data_manager.load_orbit_paths(self.test_cache_file)
            self.assertEqual(loaded_data, {})
            
    def test_old_format_conversion(self):
        """Test automatic conversion from old to new format"""
        with patch.dict('os.environ', {'ORBIT_PATHS_FILE': self.test_cache_file}):
            import orbit_data_manager
            orbit_data_manager.ORBIT_PATHS_FILE = self.test_cache_file
            orbit_data_manager.status_display = None
            
            # Save old format data
            with open(self.test_cache_file, 'w') as f:
                json.dump(self.sample_old_format, f)
                
            # Load data (should trigger conversion)
            loaded_data = orbit_data_manager.load_orbit_paths(self.test_cache_file)
            
            # Verify conversion happened
            for key in self.sample_old_format:
                self.assertIn(key, loaded_data)
                self.assertIn("data_points", loaded_data[key])
                self.assertIn("metadata", loaded_data[key])
                
    def test_corrupted_json_file(self):
        """Test handling of corrupted JSON file"""
        with patch.dict('os.environ', {'ORBIT_PATHS_FILE': self.test_cache_file}):
            import orbit_data_manager
            orbit_data_manager.ORBIT_PATHS_FILE = self.test_cache_file
            orbit_data_manager.status_display = None
            
            # Write invalid JSON
            with open(self.test_cache_file, 'w') as f:
                f.write("{invalid json content}")
                
            # Load should handle gracefully
            loaded_data = orbit_data_manager.load_orbit_paths(self.test_cache_file)
            self.assertEqual(loaded_data, {})
            
            # Check that backup was created
            backup_files = [f for f in os.listdir(self.test_dir) if '.corrupted' in f]
            self.assertTrue(len(backup_files) > 0, 
                           f"No backup files found. Files in {self.test_dir}: {os.listdir(self.test_dir)}")
                           
    def test_status_display_updates(self):
        """Test that status display is updated during operations"""
        with patch.dict('os.environ', {'ORBIT_PATHS_FILE': self.test_cache_file}):
            import orbit_data_manager
            orbit_data_manager.ORBIT_PATHS_FILE = self.test_cache_file
            
            # Track all print statements as a proxy for status updates
            print_messages = []
            
            # Mock the print function to capture messages
            with patch('builtins.print') as mock_print:
                mock_print.side_effect = lambda *args, **kwargs: print_messages.append(' '.join(str(arg) for arg in args))
                
                # Create corrupted cache
                corrupted_data = {
                    "Valid_Sun": self.sample_new_format["Mars_Sun"],
                    "Invalid_Sun": "corrupted"
                }
                
                with open(self.test_cache_file, 'w') as f:
                    json.dump(corrupted_data, f)
                    
                # Load with repair - this should trigger status updates
                orbit_data_manager.load_orbit_paths(self.test_cache_file)
                
                # Verify that status messages were printed
                # We should see messages about cache repair
                status_messages = [msg for msg in print_messages if 'CACHE REPAIR' in msg or 'Cache repaired' in msg]
                self.assertTrue(len(status_messages) > 0, 
                              f"No status messages found. All messages: {print_messages}")
            
    def test_partially_corrupted_entries(self):
        """Test detection and removal of corrupted entries"""
        with patch.dict('os.environ', {'ORBIT_PATHS_FILE': self.test_cache_file}):
            import orbit_data_manager
            orbit_data_manager.ORBIT_PATHS_FILE = self.test_cache_file
            orbit_data_manager.status_display = None
            
            # Create mixed valid/invalid data
            corrupted_data = {
                "Mars_Sun": self.sample_new_format["Mars_Sun"],  # Valid
                "Venus_Sun": None,  # Invalid
                "Earth_Sun": "invalid string",  # Invalid
                "Neptune_Sun": {  # Valid old format
                    "x": [30.0, 30.1],
                    "y": [0.1, 0.11],
                    "z": [0.01, 0.011]
                }
            }
            
            with open(self.test_cache_file, 'w') as f:
                json.dump(corrupted_data, f)
                
            # Load with repair
            loaded_data = orbit_data_manager.load_orbit_paths(self.test_cache_file)
            
            # Verify only valid entries remain
            self.assertIn("Mars_Sun", loaded_data)
            self.assertIn("Neptune_Sun", loaded_data)
            self.assertNotIn("Venus_Sun", loaded_data)
            self.assertNotIn("Earth_Sun", loaded_data)


# L-504, the first slice: the modules on the data path, each of which now
# reads the clock through utc_clock and asks JPL with cache=HORIZONS_CACHE.
DATA_PATH_MODULES = [
    'palomas_orrery.py', 'orbit_data_manager.py', 'idealized_orbits.py',
    'osculating_cache_manager.py', 'path_plan.py', 'orbital_period.py',
    'period_fetch.py', 'horizons_check.py', 'close_approach_data.py',
    'palomas_orrery_dashboard.py',
    'path_drawing.py',   # L-476: asks JPL for a path by its plan
]
_LOCAL_CLOCK = re.compile(r'datetime\.now\(\s*\)|datetime\.today\(\)|'
                          r'date\.today\(\)|\.utcnow\(\)')


def _local_clock_lines(text):
    """Lines of code (not comments) that read the computer's local clock."""
    return [line.strip() for line in text.splitlines()
            if _LOCAL_CLOCK.search(line) and not line.lstrip().startswith('#')]


# L-512 (slice a, part A1): the fresh switch is checked across the whole
# repository, on Python's parser, not on line text (Tony's prompt of Nov 4,
# 2026: "the fresh switch's check covers the whole repository"). Until then
# a line-text check looked only at DATA_PATH_MODULES, and nine JPL calls
# elsewhere asked without the switch, so astroquery could answer them from
# the copy it keeps on disk for a week.
JPL_METHODS = ('vectors', 'elements', 'ephemerides',
               'vectors_async', 'elements_async', 'ephemerides_async')
# Calls of those names that are not astroquery: (file, function, method,
# reason). Printed every run.
NOT_JPL = [
    ('provenance_history.py', 'compare', 'elements',
     "collections.Counter.elements(): a multiset's members, not JPL"),
]
# Not scanned: documentation/ (its old patch scripts carry code in strings)
# and the tests, which plant unfresh calls on purpose.
SKIP_DIRS = ('documentation', '.git', '__pycache__')


def _is_test(name):
    return name.startswith('test_') or name.endswith('_test.py')


def repo_py_files(root):
    """Every .py file the fresh check reads, as paths relative to root."""
    out = []
    for folder, dirs, files in os.walk(root):
        dirs[:] = sorted(d for d in dirs
                         if d not in SKIP_DIRS and not d.startswith('.'))
        for name in sorted(files):
            if name.endswith('.py') and not _is_test(name):
                out.append(os.path.relpath(os.path.join(folder, name), root))
    return out


def _says_fresh(call):
    """True when the call passes cache=HORIZONS_CACHE as a keyword (the
    name, or utc_clock.HORIZONS_CACHE). cache=True, a comment, a string or
    a **kwargs that might hold it does not count."""
    for kw in call.keywords:
        if kw.arg == 'cache':
            v = kw.value
            return ((isinstance(v, ast.Name) and v.id == 'HORIZONS_CACHE') or
                    (isinstance(v, ast.Attribute) and v.attr == 'HORIZONS_CACHE'))
    return False


def _payload_only(call):
    """get_query_payload=True written in the call: it builds the request and
    asks JPL nothing."""
    return any(kw.arg == 'get_query_payload' and
               isinstance(kw.value, ast.Constant) and kw.value.value is True
               for kw in call.keywords)


def fresh_scan(text, filename, exceptions=None):
    """(calls, problems, excepted, payload) for one file's source text.

    calls      every direct call of a JPL method name found
    problems   each call without cache=HORIZONS_CACHE, each reference to a
               JPL method name that is not a direct call (saved under
               another name, or asked by getattr), or the file not parsing
    excepted   calls on the NOT_JPL list
    payload    calls exempt as get_query_payload=True
    """
    if exceptions is None:
        exceptions = NOT_JPL
    base = os.path.basename(filename)
    try:
        tree = ast.parse(text, filename)
    except SyntaxError as exc:
        return [], ['%s: does not parse (%s)' % (filename, exc.msg)], [], []
    parent = {}
    for node in ast.walk(tree):
        for child in ast.iter_child_nodes(node):
            parent[child] = node

    def function_of(node):
        while node in parent:
            node = parent[node]
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                return node.name
        return '<module>'

    calls, problems, excepted, payload = [], [], [], []
    for node in ast.walk(tree):
        if (isinstance(node, ast.Call) and isinstance(node.func, ast.Name)
                and node.func.id == 'getattr' and len(node.args) > 1
                and isinstance(node.args[1], ast.Constant)
                and node.args[1].value in JPL_METHODS):
            problems.append('%s:%d in %s: getattr(..., %r) asks a JPL method '
                            'by name; call it directly with '
                            'cache=HORIZONS_CACHE'
                            % (filename, node.lineno, function_of(node),
                               node.args[1].value))
        if not (isinstance(node, ast.Attribute) and node.attr in JPL_METHODS):
            continue
        fn = function_of(node)
        where = '%s:%d in %s: .%s' % (filename, node.lineno, fn, node.attr)
        call = parent.get(node)
        if not (isinstance(call, ast.Call) and call.func is node):
            problems.append('%s is not called where it is named (saved under '
                            'another name?); call it directly with '
                            'cache=HORIZONS_CACHE' % where)
            continue
        calls.append(where)
        rule = [e for e in exceptions
                if e[0] == base and e[1] == fn and e[2] == node.attr]
        if rule:
            excepted.append('%s() -- %s' % (where, rule[0][3]))
        elif _payload_only(call):
            payload.append(where + '(get_query_payload=True)')
        elif not _says_fresh(call):
            problems.append('%s() without cache=HORIZONS_CACHE' % where)
    return calls, problems, excepted, payload


def fresh_scan_repo(root):
    """The fresh check over the repository: (files, calls, problems,
    excepted, payload)."""
    files = repo_py_files(root)
    calls, problems, excepted, payload = [], [], [], []
    for rel in files:
        with open(os.path.join(root, rel), encoding='utf-8') as f:
            text = f.read()
        c, p, e, q = fresh_scan(text, rel)
        calls += c; problems += p; excepted += e; payload += q
    return files, calls, problems, excepted, payload


FRESH_SUMMARY = {}


class TestUtcClock(unittest.TestCase):
    """L-504: the clock is read as UTC, and the orbit cache's "fetched"
    stamps are read back in both forms -- the old one with no zone, written
    from the local clock, and the new one ending "+00:00"."""

    def test_utc_now_is_utc(self):
        import utc_clock
        now = utc_clock.utc_now()
        self.assertIsNone(now.tzinfo)
        real = datetime.now(timezone.utc).replace(tzinfo=None)
        self.assertLess(abs((real - now).total_seconds()), 5)
        self.assertEqual(utc_clock.utc_today(), utc_clock.utc_now().date())

    def test_new_stamp_says_its_zone(self):
        import utc_clock
        stamp = utc_clock.utc_stamp()
        self.assertTrue(stamp.endswith('+00:00'), stamp)
        back = utc_clock.parse_stamp(stamp)
        self.assertLess(abs((utc_clock.utc_now() - back).total_seconds()), 5)
        self.assertEqual(utc_clock.parse_stamp('2026-10-28T19:57:00Z'),
                         datetime(2026, 10, 28, 19, 57))

    def test_planted_old_stamp_is_read_as_local_time(self):
        import utc_clock
        # Planted: a stamp as the cache holds it from before 2026-10-29,
        # local time with no zone.
        local = datetime(2026, 10, 28, 14, 57, 0)
        expect = local.astimezone(timezone.utc).replace(tzinfo=None)
        self.assertEqual(utc_clock.parse_stamp(local.isoformat()), expect)

    def test_cache_age_reads_both_forms(self):
        import osculating_cache_manager as ocm
        import utc_clock
        ago = timedelta(days=3, hours=1)
        new_form = {'metadata': {'fetched': utc_clock.utc_stamp(
            utc_clock.utc_now() - ago)}}
        old_form = {'metadata': {'fetched': (datetime.now() - ago).isoformat()}}
        self.assertEqual(ocm.calculate_age_days(new_form), 3)
        self.assertEqual(ocm.calculate_age_days(old_form), 3)
        self.assertIsNone(ocm.calculate_age_days(
            {'metadata': {'fetched': 'not a date'}}))

    def test_data_path_reads_no_local_clock(self):
        # L-512: asking JPL fresh is checked across the whole repository by
        # TestFreshCalls; this keeps the clock checks on the data path.
        here = os.path.dirname(os.path.abspath(__file__))
        found = {}
        for name in DATA_PATH_MODULES:
            with open(os.path.join(here, name), encoding='utf-8') as f:
                text = f.read()
            bad = _local_clock_lines(text)
            if 'utc_clock' not in text:
                bad.append('does not import utc_clock')
            if bad:
                found[name] = bad
        self.assertEqual(found, {}, 'local clock, or no utc_clock: %s' % found)

    def test_these_checks_can_fail(self):
        # Each check above, shown catching the fault it exists for.
        self.assertEqual(len(_local_clock_lines('    now = datetime.now()\n')), 1)
        self.assertEqual(len(_local_clock_lines('    d = datetime.date.today()\n')), 1)
        self.assertEqual(_local_clock_lines('#    now = datetime.now()\n'), [])

        # The reader as it was before L-504, given a new stamp: it returns
        # nothing, so test_cache_age_reads_both_forms would fail on it.
        def old_reader(entry):
            try:
                fetched = datetime.fromisoformat(entry['metadata']['fetched'])
                return int((datetime.now() - fetched).total_seconds() / 86400)
            except Exception:
                return None
        import utc_clock
        self.assertIsNone(old_reader({'metadata': {'fetched': utc_clock.utc_stamp()}}))


class TestFreshCalls(unittest.TestCase):
    """L-512: every astroquery call in the repository asks JPL fresh,
    cache=HORIZONS_CACHE, found on Python's parser across line breaks.
    The tests and documentation/ are not scanned."""

    def test_every_jpl_call_asks_fresh(self):
        here = os.path.dirname(os.path.abspath(__file__))
        files, calls, problems, excepted, payload = fresh_scan_repo(here)
        FRESH_SUMMARY.update(files=len(files), calls=len(calls),
                             excepted=excepted, payload=len(payload))
        print('\n[FRESH CHECK] %d .py files examined, %d JPL-named calls '
              'found; %d build a request only (get_query_payload=True)'
              % (len(files), len(calls), len(payload)))
        for line in excepted:
            print('[FRESH CHECK] not JPL, excepted: %s' % line)
        for line in problems:
            print('[FRESH CHECK] FAIL %s' % line)
        self.assertTrue(len(files) > 0 and len(calls) > 0,
                        'the fresh check examined nothing')
        self.assertEqual(problems, [])

    def test_the_fresh_check_can_fail(self):
        def probs(src, exceptions=()):
            return fresh_scan(src, 'planted.py', list(exceptions))[1]
        ok = 'def f(o):\n    return o.vectors(cache=HORIZONS_CACHE)\n'
        self.assertEqual(probs(ok), [])
        # across a line break, and through utc_clock's own name
        self.assertEqual(probs('def f(o):\n    return o.elements(\n'
                               '        refplane="earth",\n'
                               '        cache=utc_clock.HORIZONS_CACHE)\n'), [])
        planted = {
            'no keyword': 'def f(o):\n    return o.vectors()\n',
            'cache=True': 'def f(o):\n    return o.vectors(cache=True)\n',
            'a comment': 'def f(o):\n    return o.ephemerides()  # cache=HORIZONS_CACHE\n',
            'a string': 'def f(o):\n    return o.vectors("cache=HORIZONS_CACHE")\n',
            '**kwargs': 'def f(o, **k):\n    return o.vectors(**k)\n',
            'an _async form': 'def f(o):\n    return o.vectors_async()\n',
            'payload False': 'def f(o):\n    return o.vectors(get_query_payload=False)\n',
            'saved under another name': 'def f(o):\n    g = o.vectors\n    return g(cache=HORIZONS_CACHE)\n',
            'asked by getattr': 'def f(o):\n    return getattr(o, "elements")(cache=HORIZONS_CACHE)\n',
            'a file that does not parse': 'def f(o:\n',
        }
        for label, src in planted.items():
            self.assertTrue(probs(src), 'not caught: %s' % label)
        self.assertEqual(probs('def f(o):\n    return o.vectors(get_query_payload=True)\n'), [])
        # the exceptions list names a file, a function and a method
        counter = 'def compare(c):\n    return sorted(c.elements())\n'
        rule = [('planted.py', 'compare', 'elements', 'Counter')]
        self.assertEqual(probs(counter, rule), [])
        self.assertTrue(probs(counter))
        self.assertTrue(probs(counter.replace('compare', 'other'), rule))


def main():
    """Run the suite and close on a verdict, not on a directory path.

    unittest.main() writes OK / FAILED to stderr, and maintenance_run.py
    reads the last line of stdout. That left the Orbit cache row quoting
    the tearDown print -- a path, which appears whether the tests passed
    or not. Running the suite here lets the result be read and stated.
    """
    print("Test files are written into a temporary folder, removed when "
          "the tests finish.")
    print("Running tests in isolated environment...")

    here = os.path.dirname(os.path.abspath(__file__))
    old_folder = os.path.join(here, "test_output")
    before = set(os.listdir(here))
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestOrbitCache)
    suite.addTests(loader.loadTestsFromTestCase(TestUtcClock))
    suite.addTests(loader.loadTestsFromTestCase(TestFreshCalls))   # L-512
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    total = result.testsRun
    bad = len(result.failures) + len(result.errors)
    # L-448: the run leaves nothing behind -- its temporary folder is gone
    # and nothing new stands beside this file. Said with its evidence.
    left = sorted(set(os.listdir(here)) - before)
    shared = getattr(TestOrbitCache, "shared_dir", None)
    if shared and os.path.exists(shared):
        left.append(shared)
    if left:
        print("\nThe tests left files behind: %s" % ", ".join(left))
    else:
        print("\nNothing left behind: the temporary folder %s is removed and "
              "no file was added beside this one%s."
              % (shared, "" if not os.path.exists(old_folder)
                 else " (test_output/ is still there from before L-448)"))
    if bad or left:
        # Non-zero exit is what maintenance_run.py reads. unittest.main()
        # set it for free; forgetting it here would leave this row green
        # forever, which is the defect this patch exists to remove.
        print("\n%d of %d orbit cache tests FAILED%s." % (
            bad, total, "; and files were left behind: %s" % ", ".join(left)
            if left else ""))
        return 1
    fresh = FRESH_SUMMARY
    print("\nAll %d orbit cache tests passed: cache loads, old formats "
          "convert, corrupted entries are dropped; the clock reads UTC and "
          "both forms of the fetched stamp read back; the repository-wide "
          "fresh check examined %s .py files and %s JPL calls, every one "
          "asked fresh (%d not JPL, excepted); nothing left behind."
          % (total, fresh.get('files', '?'), fresh.get('calls', '?'),
             len(fresh.get('excepted', []))))
    return 0


if __name__ == "__main__":
    sys.exit(main())
