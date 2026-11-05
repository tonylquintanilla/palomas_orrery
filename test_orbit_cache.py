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
Module updated: November 4, 2026, evening, with Anthropic's Claude Opus 5.5
(L-512, slice a, part A2, ruling 1): TestJplOutcome, all offline on faked
answers in JPL's own words of 2026-11-04. fetch_trajectory and
fetch_position tell an unknown target, an ambiguous one and an unreachable
JPL apart, and call nothing else an outage; fetch_position on both routes
(the direct small-body request, then astroquery), a definite answer from
the first never overwritten by the second's outage; the four fallback
branches in palomas_orrery.py ask jpl_outcome.holds_fallback; each check
shown able to fail. Registered in main(), whose last line names them.
Updated Nov 4, night, for Tony's ruling: MK2, Xiangliu and 6AC4721, which
JPL has no solution for, keep their drawings whatever JPL answers.)
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

# ----------------------------------------------------------------------------
# L-512 A2: "no such body" is not "JPL unreachable" (Tony's ruling 1).
# Every answer below is faked; nothing here reaches the network.
# ----------------------------------------------------------------------------

OUTCOME_SUMMARY = {}
JD_TEST = 2461348.5   # 2026-11-04 00:00 TDB, the day the answers were read

# The words JPL used on 2026-11-04 (jpl_outcome.py's docstring), cut down.
SAID_UNKNOWN_SMALL = ("API VERSION: 1.2\nAPI SOURCE: NASA/JPL Horizons API\n\n"
                      "Matching small-bodies:\n    No matches found.\n")
SAID_AMBIGUOUS_SMALL = ("API VERSION: 1.2\n\nMatching small-bodies:\n\n"
                        "    Record #  Epoch-yr  Primary Desig  >MATCH NAME<\n"
                        "        2688            1982 HG1        Halley\n"
                        "    90000001    -239    1P              Halley\n")
SAID_NO_RECORD = "API VERSION: 1.2\n\nNo such record, positive values only\n"
SAID_OUT_OF_BOUNDS = ("API VERSION: 1.2\n\nDXREAD: requested IOBJ= ******** is "
                      "out of bounds, no action taken.\nRecord boundaries:\n")
SAID_NO_EPHEMERIS = ('API VERSION: 1.2\n\nNo ephemeris for target "Juno (spacecraft)" '
                     'prior to A.D. 2011-AUG-05 17:19:12.1832 TDB\n')


def _astroquery_says(text):
    """The ValueError astroquery 0.4.9.post1 raises for an answer whose
    words it does not recognise."""
    return ValueError('Query failed without known error message; received '
                      'the following response:\n' + text)


def _faked_answers():
    """Each outcome as the two routes meet it: (label, exception, outcome)."""
    import requests
    import jpl_outcome as J
    return [
        ('unknown, astroquery\'s words',
         ValueError('Unknown target (Zzqxw). Maybe try different id_type?'), J.UNKNOWN),
        ('unknown, "No such record"', _astroquery_says(SAID_NO_RECORD), J.UNKNOWN),
        ('unknown, a record number out of bounds (MK2)',
         _astroquery_says(SAID_OUT_OF_BOUNDS), J.UNKNOWN),
        ('ambiguous, astroquery\'s words',
         ValueError('Ambiguous target name; provide unique id:\n  2688  Halley'), J.AMBIGUOUS),
        ('unreachable, no connection',
         requests.exceptions.ConnectionError("Failed to resolve 'ssd.jpl.nasa.gov'"),
         J.UNREACHABLE),
        ('unreachable, a timeout', requests.exceptions.ReadTimeout('read timed out'),
         J.UNREACHABLE),
        ('unreachable, an HTTP failure',
         requests.exceptions.HTTPError('503 Server Error: Service Unavailable'), J.UNREACHABLE),
        ('other, a date outside the ephemeris',
         ValueError('Horizons Error: No ephemeris for target "Juno (spacecraft)" prior to '
                    'A.D. 2011-AUG-05'), J.OTHER),
        ('other, a malformed answer', ValueError('could not convert string to float'), J.OTHER),
        ('other, a local error', KeyError('x'), J.OTHER),
    ]


def _vectors_table(jd):
    from astropy.table import Table
    return Table({'datetime_jd': [jd], 'x': [1.0], 'y': [0.5], 'z': [0.1],
                  'vx': [0.001], 'vy': [0.01], 'vz': [0.0],
                  'range': [1.12], 'range_rate': [0.002]})


def _fake_horizons(answer):
    """A Horizons stand-in: vectors() raises `answer` if it is an
    exception, else returns it. It counts its calls."""
    class FakeHorizons(object):
        calls = 0

        def __init__(self, *args, **kwargs):
            pass

        def vectors(self, **kwargs):
            FakeHorizons.calls += 1
            if isinstance(answer, BaseException):
                raise answer
            return answer
    return FakeHorizons


def _load_fetch_position(**override):
    """palomas_orrery.fetch_position, read from the file and run on its own
    (importing palomas_orrery would open the app's window)."""
    import jpl_outcome as J
    from astropy.time import Time
    from constants_new import KM_PER_AU, LIGHT_MINUTES_PER_AU
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, 'palomas_orrery.py'), encoding='utf-8') as f:
        src = f.read()
    m = re.search(r'\ndef fetch_position\(.*?\n(?=def )', src, re.S)
    if not m:
        raise AssertionError('fetch_position not found in palomas_orrery.py')
    ns = {'Time': Time, 'np': np, 'HORIZONS_CACHE': False,
          'objects': [], 'parent_planets': {}, 'planetary_params': {},
          'KNOWN_ORBITAL_PERIODS': {}, 'KM_PER_AU': KM_PER_AU,
          'LIGHT_MINUTES_PER_AU': LIGHT_MINUTES_PER_AU,
          'calculate_planet9_position_on_orbit': lambda: (1.0, 2.0, 3.0, 3.74)}
    for name in ('tell', 'outcome_of_exception', 'merge_routes', 'SAYS', 'FOUND',
                 'OTHER', 'NOT_ASKED', 'NOT_A_BODY', 'UNREACHABLE'):
        ns[name] = getattr(J, name)
    ns.update(override)
    exec(compile(m.group(0), 'palomas_orrery.py (fetch_position)', 'exec'), ns)
    return ns


def _position(ns, horizons_answer, direct=None, object_id='-61', id_type=None):
    """fetch_position's result and report, with Horizons faked and the
    direct small-body request faked by `direct` (an exception, or a
    (state, record) pair) when the target is a small body."""
    from datetime import datetime as _dt
    ns['Horizons'] = _fake_horizons(horizons_answer)
    report = {}
    with patch('position_accuracy.fetch_small_body_state') as direct_request:
        if isinstance(direct, BaseException):
            direct_request.side_effect = direct
        elif direct is not None:
            direct_request.return_value = direct
        result = ns['fetch_position'](object_id, _dt(2026, 11, 4), center_id='Sun',
                                      id_type=id_type, report=report)
    return result, report, ns['Horizons'].calls


def _trajectory(horizons_answer, dates=None, **kwargs):
    import palomas_orrery_helpers as H
    from astropy.time import Time
    from datetime import datetime as _dt
    dates = dates or [_dt(2026, 11, 4)]
    if horizons_answer == 'TABLE':
        horizons_answer = _vectors_table(Time(dates).jd[0])
    report = {}
    with patch('palomas_orrery_helpers.Horizons', _fake_horizons(horizons_answer)):
        result = H.fetch_trajectory('-61', dates, center_id='Sun', report=report, **kwargs)
    return result, report


class _FakeResponse(object):
    def __init__(self, text, status=200):
        self.text = text
        self.status_code = status

    def raise_for_status(self):
        if self.status_code >= 400:
            import requests
            raise requests.exceptions.HTTPError('%d Server Error' % self.status_code)


class TestJplOutcome(unittest.TestCase):
    """L-512 A2 (ruling 1): fetch_trajectory and fetch_position tell an
    unknown target, an ambiguous one and an unreachable JPL apart, on both
    of fetch_position's routes, and hand the outcome to their callers; an
    unknown or ambiguous target never enters a fallback branch."""

    def setUp(self):
        self._quiet = patch('builtins.print')
        self._quiet.start()

    def tearDown(self):
        self._quiet.stop()

    def _count(self, key):
        OUTCOME_SUMMARY[key] = OUTCOME_SUMMARY.get(key, 0) + 1

    # -- the sorting itself ------------------------------------------------
    def test_each_answer_is_sorted(self):
        import jpl_outcome as J
        for label, exc, outcome in _faked_answers():
            self.assertEqual(J.outcome_of_exception(exc), outcome, label)
        self.assertEqual(J.outcome_of_text(SAID_UNKNOWN_SMALL), J.UNKNOWN)
        self.assertEqual(J.outcome_of_text(SAID_AMBIGUOUS_SMALL), J.AMBIGUOUS)
        self.assertEqual(J.outcome_of_text('Multiple major-bodies match string "JUPITER*"\n'
                                           '  ID#  Name\n  5  Jupiter Barycenter\n'), J.AMBIGUOUS)
        self.assertIsNone(J.outcome_of_text(SAID_NO_EPHEMERIS))
        self.assertIsNone(J.outcome_of_text(''))
        # a leftover exception is never called an outage
        for exc in (RuntimeError('boom'), TypeError('t'), OSError('disk'), ValueError('')):
            self.assertEqual(J.outcome_of_exception(exc), J.OTHER, repr(exc))
        self._count('sorting')

    # -- fetch_trajectory ---------------------------------------------------
    def test_fetch_trajectory_outcomes(self):
        import jpl_outcome as J
        result, report = _trajectory('TABLE')
        self.assertEqual(report['outcome'], J.FOUND)
        self.assertAlmostEqual(result[0]['x'], 1.0)
        for label, exc, outcome in _faked_answers():
            result, report = _trajectory(exc)
            self.assertEqual(report.get('outcome'), outcome, 'fetch_trajectory: ' + label)
            self.assertEqual(result, [None], label)
            self._count('fetch_trajectory')
        # an empty answer is not an outage
        result, report = _trajectory(_vectors_table(0.0)[:0])
        self.assertEqual(report['outcome'], J.OTHER)
        # not asked at all
        result, report = _trajectory('TABLE', start_date=datetime(2030, 1, 1))
        self.assertEqual(report['outcome'], J.NOT_ASKED)

    def test_fetch_trajectory_success_and_padding_unchanged(self):
        """A found answer reads as before, and a clamped date still pads
        to None, with or without a report."""
        import palomas_orrery_helpers as H
        from astropy.time import Time
        dates = [datetime(2026, 11, 3), datetime(2026, 11, 4)]
        table = _vectors_table(Time(dates).jd[1])
        with patch('palomas_orrery_helpers.Horizons', _fake_horizons(table)):
            plain = H.fetch_trajectory('-61', dates, start_date=dates[1])
            report = {}
            told = H.fetch_trajectory('-61', dates, start_date=dates[1], report=report)
        self.assertEqual(len(plain), 2)
        self.assertIsNone(plain[0])
        self.assertAlmostEqual(plain[1]['x'], 1.0)
        self.assertEqual(plain, told)
        self.assertEqual(report['outcome'], 'found')

    # -- fetch_position, astroquery's route only (not a small body) --------
    def test_fetch_position_astroquery_route(self):
        import jpl_outcome as J
        ns = _load_fetch_position()
        result, report, calls = _position(ns, _vectors_table(JD_TEST))
        self.assertEqual(report['outcome'], J.FOUND)
        self.assertAlmostEqual(result['x'], 1.0)
        for label, exc, outcome in _faked_answers():
            result, report, calls = _position(ns, exc)
            self.assertIsNone(result, label)
            self.assertEqual(report.get('outcome'), outcome, 'fetch_position: ' + label)
            self._count('fetch_position, astroquery')
        result, report, calls = _position(ns, _vectors_table(JD_TEST)[:0])
        self.assertIsNone(result)
        self.assertEqual(report['outcome'], J.OTHER)
        result, report, calls = _position(ns, None, object_id='planet9_placeholder')
        self.assertEqual(report['outcome'], J.NOT_ASKED)
        # the success case reads the same without a report
        plain = ns['fetch_position']
        ns['Horizons'] = _fake_horizons(_vectors_table(JD_TEST))
        self.assertAlmostEqual(plain('-61', datetime(2026, 11, 4))['x'], 1.0)

    # -- fetch_position, the direct small-body request first ---------------
    def test_fetch_position_direct_route(self):
        import jpl_outcome as J
        ns = _load_fetch_position()
        state = ({'x': 2.0, 'y': 0.0, 'z': 0.0, 'vx': 0.0, 'vy': 0.01, 'vz': 0.0,
                  'range': 2.0, 'range_rate': 0.0}, {'source': 'faked'})
        result, report, calls = _position(ns, RuntimeError('not asked'), direct=state,
                                          object_id='2688', id_type='smallbody')
        self.assertEqual(report['outcome'], J.FOUND)
        self.assertEqual(calls, 0, 'astroquery asked after the direct request answered')
        self.assertAlmostEqual(result['x'], 2.0)
        connection = _faked_answers()[4][1]
        unknown = J.JplTargetError(J.UNKNOWN, 'Horizons: Matching small-bodies: | No matches found.')
        ambiguous = J.JplTargetError(J.AMBIGUOUS, 'Horizons: Matching small-bodies: | 2688 Halley')
        cases = [
            # (direct request, astroquery, outcome)
            (unknown, connection, J.UNKNOWN),          # step 8: never overwritten by an outage
            (ambiguous, connection, J.AMBIGUOUS),      # step 8
            (unknown, _faked_answers()[6][1], J.UNKNOWN),   # ... nor by an HTTP failure
            (unknown, ValueError('Unknown target (Zzqxw). Maybe try different id_type?'), J.UNKNOWN),
            (unknown, _faked_answers()[8][1], J.UNKNOWN),   # ... nor by a malformed answer
            (connection, ValueError('Unknown target (Zzqxw). Maybe try different id_type?'), J.UNKNOWN),
            (connection, ValueError('Ambiguous target name; provide unique id:'), J.AMBIGUOUS),
            (connection, connection, J.UNREACHABLE),
            (connection, _faked_answers()[7][1], J.OTHER),
            (ValueError('Horizons returned no vector table'), connection, J.UNREACHABLE),
            (connection, _vectors_table(JD_TEST), J.FOUND),
        ]
        for direct, second, outcome in cases:
            result, report, calls = _position(ns, second, direct=direct,
                                              object_id='2688', id_type='smallbody')
            self.assertEqual(report.get('outcome'), outcome,
                             'direct %r then %r' % (direct, second))
            self.assertEqual(calls, 1)
            self._count('fetch_position, both routes')

    def test_the_direct_request_sorts_jpl_words(self):
        """position_accuracy.fetch_small_body_state reads JPL's own text:
        unknown and ambiguous raise JplTargetError; no ephemeris is not
        one; a lost connection propagates as the outage it is."""
        import requests
        import jpl_outcome as J
        from position_accuracy import fetch_small_body_state
        from test_position_digits import RECORDED_2XR_HEADER, RECORDED_2XR_DATA, _answer

        def ask(text=None, exc=None, status=200):
            fake = (lambda *a, **k: (_ for _ in ()).throw(exc)) if exc else \
                (lambda *a, **k: _FakeResponse(text, status))
            with patch('requests.get', fake):
                return fetch_small_body_state('Zzqxw', 'smallbody', '@sun', JD_TEST)

        for text, outcome in ((SAID_UNKNOWN_SMALL, J.UNKNOWN), (SAID_AMBIGUOUS_SMALL, J.AMBIGUOUS),
                              (SAID_NO_RECORD, J.UNKNOWN), (SAID_OUT_OF_BOUNDS, J.UNKNOWN)):
            with self.assertRaises(J.JplTargetError) as caught:
                ask(text)
            self.assertEqual(caught.exception.outcome, outcome)
            self.assertEqual(J.outcome_of_exception(caught.exception), outcome)
        for exc in (requests.exceptions.ConnectionError('no route'),
                    requests.exceptions.ConnectTimeout('slow')):
            with self.assertRaises(Exception) as caught:
                ask(exc=exc)
            self.assertEqual(J.outcome_of_exception(caught.exception), J.UNREACHABLE)
        with self.assertRaises(Exception) as caught:
            ask('', status=503)
        self.assertEqual(J.outcome_of_exception(caught.exception), J.UNREACHABLE)
        with self.assertRaises(ValueError) as caught:
            ask(SAID_NO_EPHEMERIS)
        self.assertNotIsInstance(caught.exception, J.JplTargetError)
        self.assertEqual(J.outcome_of_exception(caught.exception), J.OTHER)
        state, record = ask(_answer(RECORDED_2XR_HEADER, RECORDED_2XR_DATA))
        self.assertAlmostEqual(state['x'], 1.942725296484269)
        self._count('the direct request')

    # -- the callers --------------------------------------------------------
    def test_no_such_body_holds_the_fallback(self):
        import jpl_outcome as J
        # Vanth: on the fallback lists, and JPL has a solution for it.
        self.assertTrue(J.holds_fallback('Vanth', {'outcome': J.UNKNOWN}))
        self.assertTrue(J.holds_fallback('Vanth', {'outcome': J.AMBIGUOUS}))
        for outcome in (J.UNREACHABLE, J.OTHER, J.FOUND, J.NOT_ASKED):
            self.assertFalse(J.holds_fallback('Vanth', {'outcome': outcome}), outcome)
        self.assertFalse(J.holds_fallback('Vanth', {}))
        self.assertFalse(J.holds_fallback('Vanth', None))

    def test_the_three_keep_their_drawings(self):
        """Tony's ruling of Nov 4, night: MK2, Xiangliu and 6AC4721, which
        JPL has no solution for, are drawn from their published elements
        whatever JPL answers; each is on every fallback list."""
        import jpl_outcome as J
        self.assertEqual(J.DRAWN_FROM_PAPERS, frozenset(('MK2', 'Xiangliu', '6AC4721')))
        for name in sorted(J.DRAWN_FROM_PAPERS):
            for outcome in (J.UNKNOWN, J.AMBIGUOUS, J.UNREACHABLE, J.OTHER,
                            J.FOUND, J.NOT_ASKED):
                self.assertFalse(J.holds_fallback(name, {'outcome': outcome}),
                                 (name, outcome))
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, 'palomas_orrery.py'), encoding='utf-8') as f:
            src = f.read()
        lists = [line.split('=', 1)[1].split(']', 1)[0] for line in src.splitlines()
                 if line.strip().startswith(('ANALYTICAL_POSITION_FALLBACK =',
                                             'ANALYTICAL_ANIMATION_FALLBACK ='))]
        self.assertEqual(len(lists), 3)
        for found in lists:
            for name in J.DRAWN_FROM_PAPERS:
                self.assertIn("'%s'" % name, found)
        OUTCOME_SUMMARY['drawn'] = len(J.DRAWN_FROM_PAPERS)

    def test_every_fallback_branch_asks(self):
        """The four fallback branches in palomas_orrery.py pass the fetch's
        report to holds_fallback, and each fetch they follow keeps one."""
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, 'palomas_orrery.py'), encoding='utf-8') as f:
            src = f.read()
        problems = fallback_branch_problems(src)
        for line in problems:   # written past the quieted print
            sys.stdout.write('[OUTCOME CHECK] FAIL ' + line + chr(10))
        self.assertEqual(problems, [])
        OUTCOME_SUMMARY['branches'] = 4

    def test_the_outcome_checks_can_fail(self):
        """Planted faults: each is caught by the check that guards it."""
        import jpl_outcome as J
        # 1. fetch_position letting astroquery's outage overwrite the direct answer
        ns = _load_fetch_position(merge_routes=lambda first, second: second)
        unknown = J.JplTargetError(J.UNKNOWN, 'Horizons: No matches found.')
        result, report, calls = _position(ns, _faked_answers()[4][1], direct=unknown,
                                          object_id='2688', id_type='smallbody')
        self.assertNotEqual(report['outcome'], J.UNKNOWN)
        # 2. every leftover exception called an outage
        with patch('palomas_orrery_helpers.outcome_of_exception', lambda e: J.UNREACHABLE):
            result, report = _trajectory(_faked_answers()[0][1])
        self.assertNotEqual(report['outcome'], J.UNKNOWN)
        # 3. a fallback branch without the question
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, 'palomas_orrery.py'), encoding='utf-8') as f:
            src = f.read()
        planted = src.replace(
            "if planet in ANALYTICAL_POSITION_FALLBACK and not holds_fallback(planet, traj_report):",
            "if planet in ANALYTICAL_POSITION_FALLBACK:", 1)
        self.assertNotEqual(planted, src)
        self.assertTrue(fallback_branch_problems(planted))
        planted = src.replace("report=traj_report\n", "\n", 1)
        self.assertNotEqual(planted, src)
        self.assertTrue(fallback_branch_problems(planted))
        # 4. the ruling's three bodies without their exemption
        with patch.object(J, 'DRAWN_FROM_PAPERS', frozenset()):
            self.assertTrue(J.holds_fallback('MK2', {'outcome': J.UNKNOWN}))


# The fallback branches, by the condition each opens with, and the report
# its fetch keeps (L-512 A2). A branch added later is found by its list's
# name or by the analytical-position marker and must be named here.
FALLBACK_BRANCHES = [
    ('plot_actual_orbits', 'if planet in ANALYTICAL_POSITION_FALLBACK', 'traj_report'),
    ('the static worker, first loop (by MA)',
     "if (obj_data is None and obj['name'] in active_planetary_params and 'MA' in", 'pos_report'),
    ('the static worker, second loop',
     "if obj_data is None and obj['name'] in ANALYTICAL_POSITION_FALLBACK", 'pos_report'),
    ('the animation worker', "if obj['name'] in ANALYTICAL_ANIMATION_FALLBACK", 'traj_report'),
]


def fallback_branch_problems(src):
    """Each named fallback branch asks holds_fallback with its fetch's
    report, the fetch keeps that report, and no other branch opens on a
    fallback list."""
    problems = []
    lines = src.split('\n')
    for where, opens, report in FALLBACK_BRANCHES:
        at = [i for i, ln in enumerate(lines) if ln.strip().startswith(opens)]
        if len(at) != 1:
            problems.append('%s: %d branches open with %r' % (where, len(at), opens))
            continue
        cond = ' '.join(ln.strip() for ln in lines[at[0]:at[0] + 2])
        if 'holds_fallback(' not in cond or report not in cond.split('holds_fallback(', 1)[1]:
            problems.append('%s: does not ask holds_fallback(..., %s)' % (where, report))
        before = '\n'.join(lines[max(0, at[0] - 200):at[0]])
        if 'report=%s' % report not in before:
            problems.append('%s: the fetch before it keeps no report (report=%s)'
                            % (where, report))
    opened = [ln.strip() for ln in lines
              if re.match(r'\s*(if|elif)\b.*ANALYTICAL_(POSITION|ANIMATION)_FALLBACK', ln)]
    if len(opened) != 3:
        problems.append('%d branches open on a fallback list, 3 named' % len(opened))
    return problems


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
    suite.addTests(loader.loadTestsFromTestCase(TestJplOutcome))   # L-512 A2
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
          "asked fresh (%d not JPL, excepted); JPL's answers told apart "
          "(no such body, more than one, unreachable, other) on %d faked "
          "answers to fetch_trajectory, %d to fetch_position by astroquery "
          "and %d by both its routes, and %s fallback branches ask before "
          "drawing (%s bodies JPL has no solution for drawn from their "
          "papers whatever it answers); nothing left behind."
          % (total, fresh.get('files', '?'), fresh.get('calls', '?'),
             len(fresh.get('excepted', [])),
             OUTCOME_SUMMARY.get('fetch_trajectory', 0),
             OUTCOME_SUMMARY.get('fetch_position, astroquery', 0),
             OUTCOME_SUMMARY.get('fetch_position, both routes', 0),
             OUTCOME_SUMMARY.get('branches', '?'),
             OUTCOME_SUMMARY.get('drawn', '?')))
    return 0


if __name__ == "__main__":
    sys.exit(main())
