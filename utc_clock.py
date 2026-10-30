"""
utc_clock.py - The orrery's one reading of the clock, in UTC, and its one
switch for asking JPL fresh.

The orrery used to read the computer's own clock (datetime.now(),
date.today()), which gives Chicago time with no time zone attached, and
then treated that reading as UTC when it converted a date for JPL. So a
"now" it asked JPL for was off by five or six hours, and the orbit
cache's "fetched" stamps were local time while the website's are UTC.
Tony's ruling of 2026-10-28: "we should standardize on utc." Every
module that reads the clock reads it here instead (L-504; the data path
first, the Earth System fetches, the report stamps and the tools after).

TWO KINDS OF READING

    utc_now() and utc_today() give the date and time in UTC as a plain
    datetime or date, with no time zone attached. The orrery's dates are
    all plain ones that mean UTC -- the date fields, the plot's date
    line, utc_to_tdb in orbit_data_manager.py -- and a datetime that
    carries a time zone cannot be compared with or subtracted from a
    plain one; Python stops with an error. So the reading stays plain,
    and it is UTC.

    utc_stamp() gives a moment as ISO text that says its zone, ending
    "+00:00", for a stamp written into a file. parse_stamp() reads a
    stamp back in either form: one that says its zone, or an old one
    with none, which was written from the computer's local clock before
    2026-10-29 and is converted from local time to UTC.

ASKING JPL FRESH

    HORIZONS_CACHE is False, and every astroquery call on the data path
    passes it as cache=. astroquery keeps each answer from JPL on disk
    for a week (astroquery.cache_conf.cache_timeout, 604800 s) and hands
    it back when the same question is asked again. On 2026-10-29 the
    website's builder was handed an earlier run's orbit for 2026 ED138
    after JPL had revised it (L-399). The orrery keeps its own caches
    (data/osculating_cache.json, data/orbit_paths.json), so a record that
    says "fetched" today must have been fetched today. The cost is one
    JPL round trip when the same plot is asked twice, which the orrery's
    own orbit cache already absorbs.

Key functions:
    utc_now()           the date and time now, UTC, plain datetime
    utc_today()         today's date, UTC
    utc_stamp()         a moment as ISO text ending "+00:00"
    parse_stamp(text)   a stamp in either form, as a plain UTC datetime

Consumed by: palomas_orrery.py, orbit_data_manager.py, idealized_orbits.py,
osculating_cache_manager.py, path_plan.py, orbital_period.py,
period_fetch.py, horizons_check.py, close_approach_data.py,
palomas_orrery_dashboard.py

Module updated: October 29, 2026 with Anthropic's Claude Opus 5.5 (L-504,
first slice: written).

Role: utility
Domain: utilities
"""

import datetime as _dt

# Pass as cache= to every astroquery Horizons call (see ASKING JPL FRESH
# above): False, so a record stamped "fetched" today was fetched today.
HORIZONS_CACHE = False


def utc_now():
    """The date and time now in UTC, as a plain datetime (no zone attached)."""
    return _dt.datetime.now(_dt.timezone.utc).replace(tzinfo=None)


def utc_today():
    """Today's date in UTC. In Chicago's evening this is already tomorrow."""
    return utc_now().date()


def utc_stamp(moment=None):
    """A moment as ISO text that says its zone, ending "+00:00".

    With no argument, now. A plain datetime given is taken to be UTC.
    """
    if moment is None:
        moment = utc_now()
    if moment.tzinfo is None:
        moment = moment.replace(tzinfo=_dt.timezone.utc)
    return moment.astimezone(_dt.timezone.utc).isoformat()


def parse_stamp(text):
    """A stamp read back as a plain UTC datetime, whichever form it is in.

    A stamp that says its zone ("+00:00", "Z", or any offset) is turned
    to UTC. One with no zone was written from the computer's local clock
    before 2026-10-29 and is read as local time, then turned to UTC.
    Raises ValueError for text that is not a date at all.
    """
    text = str(text).strip()
    if text.endswith('Z'):
        text = text[:-1] + '+00:00'
    moment = _dt.datetime.fromisoformat(text)
    if moment.tzinfo is None:
        moment = moment.astimezone()          # local time, as it was written
    return moment.astimezone(_dt.timezone.utc).replace(tzinfo=None)
