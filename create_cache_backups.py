"""
create_cache_backups.py - One-shot script to create timestamped backups of star data caches.

Calls simbad_manager.protect_all_star_data() to back up SIMBAD query results
and stellar property caches. Run manually before risky cache operations.

Module updated: April 2026 with Anthropic's Claude Opus 4.6
"""
from simbad_manager import protect_all_star_data
protect_all_star_data()  # Creates timestamped backups