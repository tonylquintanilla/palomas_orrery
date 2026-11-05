"""
jpl_outcome.py -- what JPL Horizons answered when the orrery asked it for a
body, sorted into the kinds a caller has to tell apart (L-512, slice a,
part A2; Tony's ruling 1 of 2026-11-04: "no such object" is not a failure
to reach JPL).

THE OUTCOMES

    found        JPL answered with the body's positions.
    unknown      JPL answered that it has no such body: astroquery's
                 "Unknown target (...)", or Horizons' own "No matches
                 found." under "Matching small-bodies:", "No such record",
                 or "DXREAD: requested IOBJ= ... is out of bounds" (a record
                 number past the end of its tables).
    ambiguous    JPL answered that more than one body matches: astroquery's
                 "Ambiguous target name; provide unique id", or Horizons'
                 own list under "Matching small-bodies:" or "Multiple
                 major-bodies match string".
    unreachable  JPL could not be reached or did not answer: a connection
                 error, a timeout, or an HTTP failure (requests'
                 ConnectionError, Timeout, HTTPError, ChunkedEncodingError,
                 and Python's own ConnectionError and TimeoutError).
    other        Anything else: a date outside the body's ephemeris ("No
                 ephemeris for target"), an empty answer, an answer that
                 cannot be read, a local error. Never called an outage.
    not_asked    The orrery did not ask JPL (Planet 9, an exoplanet, no
                 date inside the body's window).

    Only "unreachable" is an outage. "unknown" and "ambiguous" are JPL's
    definite answers about the body; a store or a fallback never answers
    for them (ruling 1; the Oct 31 ruling that a record holds one
    identity).

HOW JPL SAYS EACH, AS READ ON 2026-11-04 (astroquery 0.4.9.post1, server
https://ssd.jpl.nasa.gov/api/horizons.api, each answered with HTTP 200)

    "Zzqxw Notabody" as a small body: astroquery raises ValueError
      "Unknown target (Zzqxw Notabody). Maybe try different id_type?";
      the text reads "Matching small-bodies:" then "No matches found."
    "Halley" as a small body: ValueError "Ambiguous target name; provide
      unique id:" with records 2688, 90000001, 90000002 ...
    "Jupiter" as a major body: the same ValueError; the text reads
      "Multiple major-bodies match string "JUPITER*"".
    "-98765": ValueError "Query failed without known error message"; the
      text reads "No such record, positive values only".
    "none" as a small body (6AC4721's id): "Unknown target (none)".
    120136472 (MK2) and 120225088 (Xiangliu): ValueError "Query failed
      without known error message"; the text reads "DXREAD: requested
      IOBJ= ******** is out of bounds, no action taken."
    -61 (Juno) on 1900-01-01: ValueError "Horizons Error: No ephemeris for
      target "Juno (spacecraft)" prior to A.D. 2011-AUG-05 ..." -- other.
    120090482 (Vanth) around Orcus: found.

    astroquery recognises the first two kinds itself and passes the rest
    on as "Query failed ... received the following response:" with JPL's
    text; outcome_of_exception reads that text with outcome_of_text, so
    both of the orrery's routes (astroquery, and position_accuracy's
    direct request) sort the same words the same way.

WHO USES IT

    palomas_orrery_helpers.fetch_trajectory and palomas_orrery.fetch_position
    fill a caller's report dict with the outcome; position_accuracy.
    fetch_small_body_state raises JplTargetError for a definite unknown or
    ambiguous answer. The fallback branches in palomas_orrery.py
    (plot_actual_orbits, the static worker's two, the animation worker's)
    ask holds_fallback before drawing anything in JPL's place.

THE BODIES JPL HAS NO SOLUTION FOR

    MK2 (120136472), Xiangliu (120225088) and 6AC4721 are drawn from
    their typed elements whatever JPL answers (Tony's ruling of
    2026-11-04, night). JPL serves no positions for any of them: for
    MK2 and Xiangliu it answers "DXREAD: requested IOBJ= ******** is out
    of bounds", the same for their system ids (920136472, 920225088),
    and its small-body pages list both only as discoveries, with no
    orbit. Their elements come from published papers, cited in
    orbital_elements.py (Xiangliu: Kiss et al. 2017; MK2:
    arXiv:2509.05880) and named in their hovers. The ids are kept: they
    follow the pattern JPL uses for Vanth (120090482), so a solution JPL
    publishes is found under them. "No such body" still keeps every
    other body out of the fallbacks.

Role: computation
Domain: orrery

Module created: November 4, 2026, evening, with Anthropic's Claude Opus 5.5
(L-512, slice a, part A2: "no such body" is not "JPL unreachable").
Updated: November 4, 2026, night, with Anthropic's Claude Opus 5.5
(L-512 A2, Tony's ruling: the three bodies JPL has no solution for keep
their drawings).
"""

FOUND = 'found'
UNKNOWN = 'unknown'
AMBIGUOUS = 'ambiguous'
UNREACHABLE = 'unreachable'
OTHER = 'other'
NOT_ASKED = 'not_asked'

# JPL's definite answers that there is no single such body.
NOT_A_BODY = (UNKNOWN, AMBIGUOUS)

# Bodies JPL has no solution for, drawn from their published elements
# whatever JPL answers (Tony's ruling of 2026-11-04, night; see the
# docstring). Names as the fallback lists in palomas_orrery.py spell them.
DRAWN_FROM_PAPERS = frozenset(('MK2', 'Xiangliu', '6AC4721'))

SAYS = {
    FOUND: 'JPL answered',
    UNKNOWN: 'JPL has no such body (unknown target)',
    AMBIGUOUS: 'JPL matches more than one body (ambiguous target)',
    UNREACHABLE: 'JPL could not be reached',
    OTHER: 'JPL gave no positions (not an outage)',
    NOT_ASKED: 'not asked of JPL',
}


class JplTargetError(ValueError):
    """JPL's definite answer that a target is unknown or ambiguous. A
    ValueError, so a caller that catches ValueError or Exception still
    catches it."""

    def __init__(self, outcome, message):
        ValueError.__init__(self, message)
        self.outcome = outcome


def outcome_of_text(text):
    """UNKNOWN or AMBIGUOUS when Horizons' text says so, else None. Read
    with the same markers astroquery 0.4.9's _parse_result uses, plus the
    two record-number answers it does not recognise."""
    if not text:
        return None
    lines = str(text).split('\n')
    for idx, line in enumerate(lines):
        if 'Matching small-bodies' in line or 'Multiple major-bodies match string' in line:
            following = [ln for ln in lines[idx + 1:] if ln.strip()]
            if following and 'No matches found' in following[0]:
                return UNKNOWN
            return AMBIGUOUS
        if 'No such record' in line:
            return UNKNOWN
        if 'DXREAD' in line and 'out of bounds' in line:
            return UNKNOWN
    return None


def _unreachable_types():
    types = [ConnectionError, TimeoutError]
    try:
        import requests
        types += [requests.exceptions.ConnectionError,
                  requests.exceptions.Timeout,
                  requests.exceptions.HTTPError,
                  requests.exceptions.ChunkedEncodingError]
    except ImportError:
        pass
    return tuple(types)


def outcome_of_exception(exc):
    """The outcome an exception from a JPL question stands for."""
    if isinstance(exc, JplTargetError):
        return exc.outcome
    if isinstance(exc, _unreachable_types()):
        return UNREACHABLE
    if isinstance(exc, ValueError):
        msg = str(exc)
        if msg.startswith('Unknown target ('):
            return UNKNOWN
        if msg.startswith('Ambiguous target name'):
            return AMBIGUOUS
        said = outcome_of_text(msg)
        if said is not None:
            return said
    return OTHER


def merge_routes(first, second):
    """fetch_position's outcome when its first route (the direct request)
    gave `first` and astroquery then gave `second`. A definite unknown or
    ambiguous answer from the first route is never overwritten by an
    outage, or by another failure, of the second."""
    if second == FOUND:
        return FOUND
    if first in NOT_A_BODY and second not in NOT_A_BODY:
        return first
    return second


def tell(report, outcome, detail=''):
    """Write the outcome into a caller's report dict, if it passed one."""
    if report is not None:
        report['outcome'] = outcome
        report['detail'] = str(detail)[:300]
    return outcome


def holds_fallback(name, report):
    """True, with a console line, when JPL's answer about `name` was that
    it has no such body or more than one: nothing is drawn in JPL's place
    (ruling 1). False for every other outcome, when no report was kept,
    and for a body in DRAWN_FROM_PAPERS, which JPL has no solution for
    and the orrery draws from its published elements."""
    outcome = (report or {}).get('outcome')
    if name in DRAWN_FROM_PAPERS:
        if outcome in NOT_A_BODY:
            print("[JPL ANSWER] %s: %s; drawn from its published elements "
                  "(L-512, Tony's ruling of Nov 4)" % (name, SAYS[outcome]),
                  flush=True)
        return False
    if outcome in NOT_A_BODY:
        print("[JPL ANSWER] %s: %s; not drawn from a fallback "
              "(L-512, ruling 1)" % (name, SAYS[outcome]), flush=True)
        return True
    return False
