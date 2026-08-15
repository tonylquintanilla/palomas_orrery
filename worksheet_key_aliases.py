"""Retired worksheet keys and what replaced them.

Domain: dev_tools

A worksheet key names a code site by its enclosing function or
assignment. Rename that function and every key pointing into it goes
stale at once -- and neither end can be repaired. The code should be
renameable; forbidding a rename to protect a citation scheme is
backwards. And the worksheet must not be edited, because a worksheet
is the record of what was known on its date, and editing one to match
today's code is the same failure as citing over recalled data.

So the pointer is repaired in a third place: here. An entry records a
rename that happened. The evidence stays where it was written; the
path to it is updated.

THREE RULES, AND THEY ARE WHAT MAKE THIS SAFE

1. APPEND ONLY, AND ONLY IN RESPONSE TO A FINDING. An entry is added
   when a checker run reports KEY_STALE and a human confirms the cause
   was a rename. There is no maintenance duty and no reason to edit or
   delete an entry -- an alias records something that happened, and
   history does not un-happen.

2. IT LIVES BESIDE THE CHECKER AND THE CHECKER IMPORTS IT. A map in
   documentation/ would be a check in a store nobody opens, which is a
   check that cannot fail.

3. A BROKEN ALIAS IS ITS OWN FINDING. An alias whose target does not
   resolve reports ALIAS_STALE. A cycle reports ALIAS_CYCLE. Neither
   is ever a silent drop, because the whole reason this file is
   tolerable is that its lag is loud: the report keeps saying
   KEY_STALE until someone adds the entry, and keeps saying
   ALIAS_STALE if the entry is wrong.

WHY THIS SECOND STORE IS NOT THE KIND THAT DRIFTS

The failure this project's rules exist to kill is SILENT divergence --
the skill manifest advertising 1.1 against an actual 1.2 for three
weeks with nothing surfacing it. A store whose missing entry is a
standing finding in every run cannot diverge quietly. That is the
manifest failure with its polarity reversed.

WHAT NOT TO DO WHEN A PIN FAILS

test_worksheet_keys.py resolves keys minted at an earlier commit
against today's source. When a rename breaks one, the fix is an entry
here. Regenerating the pin file would make the failure disappear
without repairing anything, and would leave every worksheet in the
archive pointing at a name that no longer exists.

Format: retired key -> current key. Chains resolve transitively, so a
site renamed twice needs only the new hop appended.

    ALIASES = {
        'pluto_visualization_shells.py::create_pluto_core_shell::description':
            'pluto_visualization_shells.py::build_pluto_core_shell::description',
    }

Currently empty. That is the honest state: no rename has happened yet.
An empty map in the repo is visible; a map that does not exist until
the first rename is a mechanism nobody remembers at the moment it is
needed.

Module created: August 2026 with Anthropic's Claude Opus 5 (L-192).
"""

ALIASES = {}
