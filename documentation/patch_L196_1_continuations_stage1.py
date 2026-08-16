"""normalize_continuations_stage1.py -- L-195 / L-192. Mark citation-leg
continuation comments so the request builder can join them instead of
silently dropping them.

RUN COMMAND
-----------
Save this file into the palomas_orrery repo root (the same folder as
constants_new.py), open it in VS Code, and click Run.

    python normalize_continuations_stage1.py

WHAT IT DOES
------------
A citation comment that wraps onto a second line looks like this:

    # Source: NASA MESSENGER Mission; Winslow et al. 2013 -- magnetopause
    #         1.45 R_M and bow shock 1.96 R_M (used in the geometry below).

The builder's leg extractor matches labeled lines only, so the second
line is dropped -- and that dropped text is what the responder is asked
to verdict. This script relabels every such continuation with an
explicit marker naming the leg it continues:

    # Source: NASA MESSENGER Mission; Winslow et al. 2013 -- magnetopause
    # Source+: 1.45 R_M and bow shock 1.96 R_M (used in the geometry below).

Text is unchanged. Only the line's leading comment padding becomes a
label. The builder change that JOINS on this marker is a separate
deliverable; running this script alone changes no rendered output.

SCOPE
-----
Stage 1 of 2: the seven files the request builder reads today.
96 lines across 48 continuation runs. Stage 2 covers the remaining 23
files (117 runs) that will come into scope as annotations are added.

Leg-specific markers, per Tony's ruling 2026-08-16: a Ref+ sitting
under a Source line is a mismatch the builder can report, where a
generic marker would have nothing to compare against.

SAFETY
------
All-or-nothing. Every file is fingerprinted (CRLF-normalized) before
anything is written, and every target line must match its recorded text
exactly. Any mismatch aborts the whole run with nothing written.
Edits apply bottom-up within each file. Each file's own line endings
are preserved.

Success: one 'ok' line per file, then 'patch applied (N bytes)'.
Failure: a single 'ERROR:' or 'ANCHOR FAIL' line; nothing is written.
"""

import hashlib
import os
import sys

EDITS = {
    'constants_new.py': {
        'fp': '87a39ae3c7f8ebc84f8e929d16231c7f',
        'edits': [
            (392,
             '# Corrected 2026-04-15 per Gemini review (was 0.0088 = 8.8 meters!)',
             '# Source+: Corrected 2026-04-15 per Gemini review (was 0.0088 = 8.8 meters!)'),
            (391,
             '#         Overall dims 35.95 x 19.90 x 9.75 km (bilobed contact binary)',
             '# Source+: Overall dims 35.95 x 19.90 x 9.75 km (bilobed contact binary)'),
            (390,
             '#         Volume 3166 km^3 -> equivalent sphere radius 9.1 km',
             '# Source+: Volume 3166 km^3 -> equivalent sphere radius 9.1 km'),
            (380,
             '#         JPL SSD publishes 715; equatorial 870',
             '# Source+: JPL SSD publishes 715; equatorial 870'),
            (379,
             '#         Highly ellipsoidal: 1050x840x537 km -> geometric mean 779.5 km',
             '# Source+: Highly ellipsoidal: 1050x840x537 km -> geometric mean 779.5 km'),
            (369,
             '#         Confirmed by OSIRIS-REx OLA: mean radius 246 +/- 10 m, V = 0.062 km^3',
             '# Source+: Confirmed by OSIRIS-REx OLA: mean radius 246 +/- 10 m, V = 0.062 km^3'),
            (336,
             '#         Also IAU/LRO reference radius (Archinal et al. 2011)',
             '# Source+: Also IAU/LRO reference radius (Archinal et al. 2011)'),
            (271,
             "#         and the Sun's galactocentric distance.",
             "# Source+: and the Sun's galactocentric distance."),
            (270,
             '#         model-dependent, varying with assumed enclosed galactic mass',
             '# Source+: model-dependent, varying with assumed enclosed galactic mass'),
            (261,
             '#         ~2.4 light-years. Visualization boundary, not a measured value.',
             '# Source+: ~2.4 light-years. Visualization boundary, not a measured value.'),
            (260,
             "#         depends on assumed enclosed galactic mass and Sun's orbital distance.",
             "# Source+: depends on assumed enclosed galactic mass and Sun's orbital distance."),
            (259,
             '#         Estimates range 100,000-200,000 AU in the literature;',
             '# Source+: Estimates range 100,000-200,000 AU in the literature;'),
            (206,
             '# Using rho_sun = 1408 kg/m3, rho_comet ~ 500 kg/m3',
             '# Calculation+: Using rho_sun = 1408 kg/m3, rho_comet ~ 500 kg/m3'),
            (175,
             '#         Ch. 11 -- chromosphere extends ~2000 km above the photosphere.',
             '# Source+: Ch. 11 -- chromosphere extends ~2000 km above the photosphere.'),
            (121,
             '#          = 63,241.077 AU per light-year',
             '# Derived+: = 63,241.077 AU per light-year'),
            (117,
             '# Previous hardcoded value was 8.3167 (consistent to 5 sig figs)',
             '# Derived+: Previous hardcoded value was 8.3167 (consistent to 5 sig figs)'),
            (113,
             '# Previous hardcoded value was 0.00465047 (consistent to 6 sig figs)',
             '# Derived+: Previous hardcoded value was 0.00465047 (consistent to 6 sig figs)'),
        ],
    },
    'eris_visualization_shells.py': {
        'fp': '4646fc25f1d82604184d3a01e78c90b0',
        'edits': [
            (473,
             '#         Barycenter binary: system mass is the correct input, not Eris alone.',
             '# Source+: Barycenter binary: system mass is the correct input, not Eris alone.'),
            (472,
             '#         semi-major axis 67.8 AU gives ~14.3 Mkm (~0.095 AU).',
             '# Source+: semi-major axis 67.8 AU gives ~14.3 Mkm (~0.095 AU).'),
            (471,
             '#         Perihelion 38.0 AU gives ~8.0 Mkm (the shell uses this);',
             '# Source+: Perihelion 38.0 AU gives ~8.0 Mkm (the shell uses this);'),
            (470,
             '#         Claude Opus 5 2026-08-03.',
             '# Source+: Claude Opus 5 2026-08-03.'),
            (469,
             "#         construction from Dysnomia's orbit) via the standard Hill approximation,",
             "# Source+: construction from Dysnomia's orbit) via the standard Hill approximation,"),
            (375,
             '#         Surface temperature approximately -240 degC (modeled range -217 to -243 degC).',
             '# Source+: Surface temperature approximately -240 degC (modeled range -217 to -243 degC).'),
            (374,
             "#         upper limit ~1 nbar surface pressure, ~10,000x more tenuous than Pluto's.",
             "# Source+: upper limit ~1 nbar surface pressure, ~10,000x more tenuous than Pluto's."),
            (214,
             '#         Brown & Schaller (2007) (nitrogen/methane surface composition)',
             '# Source+: Brown & Schaller (2007) (nitrogen/methane surface composition)'),
            (40,
             '#         JWST (2023/2024) (D/H ratio in methane ice, internal heating evidence)',
             '# Source+: JWST (2023/2024) (D/H ratio in methane ice, internal heating evidence)'),
            (39,
             '#         Nimmo & Brown (2023) also supports a differentiated, rock-dominated interior.',
             '# Source+: Nimmo & Brown (2023) also supports a differentiated, rock-dominated interior.'),
            (38,
             "#         model's output, and ~500 K below rock melting.",
             "# Source+: model's output, and ~500 K below rock melting."),
            (37,
             '#         giving a modeled central temperature of 875 K. Modeled, not measured; one',
             '# Source+: giving a modeled central temperature of 875 K. Modeled, not measured; one'),
            (36,
             '#         radiogenic heating 4.5e-12 W/kg, thermal conductivity 3 W/m/K, surface 30 K,',
             '# Source+: radiogenic heating 4.5e-12 W/kg, thermal conductivity 3 W/m/K, surface 30 K,'),
            (35,
             '#         Nimmo & Brown (2023), Science Advances 9, eadi9201 -- interior model inputs:',
             '# Source+: Nimmo & Brown (2023), Science Advances 9, eadi9201 -- interior model inputs:'),
        ],
    },
    'mars_visualization_shells.py': {
        'fp': '5e6f10918c55fdc20b76bc38868c2a41',
        'edits': [
            (840,
             '#         project equatorial radius 3,396.2 km (Archinal et al. 2018).',
             '# Source+: project equatorial radius 3,396.2 km (Archinal et al. 2018).'),
            (839,
             '#         ~1.084 Mkm / ~319.2 R_Mars is the semi-major axis average, using the',
             '# Source+: ~1.084 Mkm / ~319.2 R_Mars is the semi-major axis average, using the'),
            (838,
             '#         Hill sphere varies with eccentricity (~0.98 Mkm perihelion to ~1.19 Mkm aphelion);',
             '# Source+: Hill sphere varies with eccentricity (~0.98 Mkm perihelion to ~1.19 Mkm aphelion);'),
            (837,
             '#         via standard Hill approximation, Claude Opus 5 2026-08-01',
             '# Source+: via standard Hill approximation, Claude Opus 5 2026-08-01'),
            (710,
             '    #         NASA Solar System Exploration (Earth comparison)',
             '    # Source+: NASA Solar System Exploration (Earth comparison)'),
            (595,
             '#         Vignes et al. 2000, GRL 27 (MPB 1.29 R_M, bow shock 1.64 R_M)',
             '# Source+: Vignes et al. 2000, GRL 27 (MPB 1.29 R_M, bow shock 1.64 R_M)'),
        ],
    },
    'mercury_visualization_shells.py': {
        'fp': '3ba34c52ea438f24a0dd2adb28b92da1',
        'edits': [
            (420,
             '#         input (no system-mass term).',
             '# Source+: input (no system-mass term).'),
            (419,
             '#         Mercury has no significant companion, so body mass is the correct',
             '# Source+: Mercury has no significant companion, so body mass is the correct'),
            (418,
             '#         Claude Opus 5 2026-08-03. Perihelion convention.',
             '# Source+: Claude Opus 5 2026-08-03. Perihelion convention.'),
            (417,
             '#         perihelion distance) via the standard Hill approximation,',
             '# Source+: perihelion distance) via the standard Hill approximation,'),
            (250,
             '#         1.45 R_M and bow shock 1.96 R_M (the values used in the geometry below).',
             '# Source+: 1.45 R_M and bow shock 1.96 R_M (the values used in the geometry below).'),
            (90,
             '#         Schmidt et al. 2010, Icarus -- tail >1,000 R_M, highly variable.',
             '# Source+: Schmidt et al. 2010, Icarus -- tail >1,000 R_M, highly variable.'),
            (64,
             '#         (MESSENGER gravity/topography, isostasy).',
             '# Source+: (MESSENGER gravity/topography, isostasy).'),
            (45,
             '#         2020 +/- 30 km (MESSENGER gravity and spin state). Used for visualization.',
             '# Source+: 2020 +/- 30 km (MESSENGER gravity and spin state). Used for visualization.'),
        ],
    },
    'moon_visualization_shells.py': {
        'fp': '1879a01d68ffed910690f91b6d4d2204',
        'edits': [
            (580,
             '#         (Moon mean radius 1,737.4 km), which lies inside that range.',
             '# Source+: (Moon mean radius 1,737.4 km), which lies inside that range.'),
            (579,
             '#         ~64,901 km (apogee). The shell uses 34.53 lunar radii = ~59,992 km',
             '# Source+: ~64,901 km (apogee). The shell uses 34.53 lunar radii = ~59,992 km'),
            (578,
             '#         The Hill radius varies over the orbit from ~58,147 km (perigee) to',
             '# Source+: The Hill radius varies over the orbit from ~58,147 km (perigee) to'),
            (577,
             '#         ~60,000 km is a conventional rounded value, not a measured constant.',
             '# Source+: ~60,000 km is a conventional rounded value, not a measured constant.'),
            (576,
             '#         Claude Opus 5 2026-08-03.',
             '# Source+: Claude Opus 5 2026-08-03.'),
            (575,
             '#         Earth-Moon distance) via the standard Hill approximation,',
             '# Source+: Earth-Moon distance) via the standard Hill approximation,'),
            (247,
             '        #         Draper (1847) for Draper point 798 K.',
             '        # Source+: Draper (1847) for Draper point 798 K.'),
            (246,
             '        #         Apollo Seismic Experiment reports (deep moonquakes, tidal stress);',
             '        # Source+: Apollo Seismic Experiment reports (deep moonquakes, tidal stress);'),
            (224,
             '#         tidal stress origin.',
             '# Source+: tidal stress origin.'),
            (223,
             '#         Deep moonquakes 700-1,200 km depth, concentrated at 800-1,000 km;',
             '# Source+: Deep moonquakes 700-1,200 km depth, concentrated at 800-1,000 km;'),
            (222,
             '#         Nakamura 2005, JGR 110 -- deep moonquake catalog reanalysis.',
             '# Source+: Nakamura 2005, JGR 110 -- deep moonquake catalog reanalysis.'),
            (131,
             '        #         outer core ~330 km radius, partially molten silicate boundary layer ~150 km thick.',
             '        # Source+: outer core ~330 km radius, partially molten silicate boundary layer ~150 km thick.'),
            (60,
             '        #         solid iron-rich inner core ~240 km radius (seismic constraint).',
             '        # Source+: solid iron-rich inner core ~240 km radius (seismic constraint).'),
            (39,
             '#         solid inner core ~240 km radius, from Apollo seismic array reanalysis.',
             '# Source+: solid inner core ~240 km radius, from Apollo seismic array reanalysis.'),
        ],
    },
    'pluto_visualization_shells.py': {
        'fp': '3c7f161b7a8b094f2097294a77d58450',
        'edits': [
            (634,
             '        #         All 5 moons (Charon, Styx, Nix, Kerberos, Hydra) lie within.',
             '        # Source+: All 5 moons (Charon, Styx, Nix, Kerberos, Hydra) lie within.'),
            (633,
             '        #         at perihelion 29.66 AU: ~5.99 Mkm (0.04 AU) = 5041 Pluto radii.',
             '        # Source+: at perihelion 29.66 AU: ~5.99 Mkm (0.04 AU) = 5041 Pluto radii.'),
            (608,
             '#         Barycenter binary: system mass is the correct input, not Pluto alone.',
             '# Source+: Barycenter binary: system mass is the correct input, not Pluto alone.'),
            (607,
             '#         Result ~5.99 Mkm (0.04 AU) = 5041 Pluto radii.',
             '# Source+: Result ~5.99 Mkm (0.04 AU) = 5041 Pluto radii.'),
            (606,
             '#         via the standard Hill approximation, Claude Opus 5 2026-08-03.',
             '# Source+: via the standard Hill approximation, Claude Opus 5 2026-08-03.'),
            (605,
             '#         (GM_Pluto 869.3 + GM_Charon 106.1 km^3/s^2) at perihelion 29.66 AU,',
             '# Source+: (GM_Pluto 869.3 + GM_Charon 106.1 km^3/s^2) at perihelion 29.66 AU,'),
            (529,
             '        #         Stern et al. (2015, Science) -- temperature inversion.',
             '        # Source+: Stern et al. (2015, Science) -- temperature inversion.'),
            (528,
             '        #         (~2,900 km from center, ~2.43 R_Pluto). Supersedes Gladstone 2016.',
             '        # Source+: (~2,900 km from center, ~2.43 R_Pluto). Supersedes Gladstone 2016.'),
            (503,
             '#         20+ haze layers.',
             '# Source+: 20+ haze layers.'),
            (502,
             "#         Stern et al. (2015, Science) -- surface pressure ~10 microbars (1/100,000th Earth's);",
             "# Source+: Stern et al. (2015, Science) -- surface pressure ~10 microbars (1/100,000th Earth's);"),
            (501,
             '#         for exobase altitude.',
             '# Source+: for exobase altitude.'),
            (500,
             '#         (~2,900 km from center, ~2.43 Pluto radii). Supersedes Gladstone et al. 2016',
             '# Source+: (~2,900 km from center, ~2.43 Pluto radii). Supersedes Gladstone et al. 2016'),
            (419,
             '        #         20 distinct haze layers up to 200 km, tholin formation, blue backlit color.',
             '        # Source+: 20 distinct haze layers up to 200 km, tholin formation, blue backlit color.'),
            (396,
             '#         20+ haze layers up to 200 km observed by New Horizons; temperature inversion.',
             '# Source+: 20+ haze layers up to 200 km observed by New Horizons; temperature inversion.'),
            (245,
             '        #         N2-dominated ice surface, water-ice mountains (2-3 km), Sputnik Planitia convection.',
             '        # Source+: N2-dominated ice surface, water-ice mountains (2-3 km), Sputnik Planitia convection.'),
            (244,
             '        #         Grundy et al. (2016, Science) -- surface composition mapping.',
             '        # Source+: Grundy et al. (2016, Science) -- surface composition mapping.'),
            (221,
             '#         Sputnik Planitia age <10 Myr.',
             '# Source+: Sputnik Planitia age <10 Myr.'),
            (220,
             '#         N2-dominated ice surface (Sputnik Planitia), water-ice mountains 2-3 km,',
             '# Source+: N2-dominated ice surface (Sputnik Planitia), water-ice mountains 2-3 km,'),
            (219,
             '#         Grundy et al. (2016, Science) -- surface composition mapping;',
             '# Source+: Grundy et al. (2016, Science) -- surface composition mapping;'),
            (151,
             '        #         ocean 100-180 km thick; lithosphere at least 300 km thick in some models to support high mountains.',
             '        # Source+: ocean 100-180 km thick; lithosphere at least 300 km thick in some models to support high mountains.'),
            (132,
             '#         water-ice mantle, subsurface ocean 100-180 km thick with ammonia antifreeze.',
             '# Source+: water-ice mantle, subsurface ocean 100-180 km thick with ammonia antifreeze.'),
            (56,
             '        #         core ~1,700 km / 70% diameter, radioactive isotopes (U-238, U-235, Th-232, K-40), ocean evidence.',
             '        # Source+: core ~1,700 km / 70% diameter, radioactive isotopes (U-238, U-235, Th-232, K-40), ocean evidence.'),
            (34,
             '#         rocky core ~1,700 km diameter (~70% of total), radioactive heating (U, Th, K).',
             '# Source+: rocky core ~1,700 km diameter (~70% of total), radioactive heating (U, Th, K).'),
        ],
    },
    'venus_visualization_shells.py': {
        'fp': '8bb96be6e1da8223aa712dceb7fff751',
        'edits': [
            (677,
             '#         Venus has no natural moons, so body mass is the correct input.',
             '# Source+: Venus has no natural moons, so body mass is the correct input.'),
            (676,
             '#         semi-major axis gives ~1.011 Mkm = 167.1 Venus radii.',
             '# Source+: semi-major axis gives ~1.011 Mkm = 167.1 Venus radii.'),
            (675,
             '#         Perihelion gives ~1.004 Mkm = 166 Venus radii (the shell uses this);',
             '# Source+: Perihelion gives ~1.004 Mkm = 166 Venus radii (the shell uses this);'),
            (674,
             '#         Claude Opus 5 2026-08-03.',
             '# Source+: Claude Opus 5 2026-08-03.'),
            (673,
             '#         distance 107.48 Mkm) via the standard Hill approximation,',
             '# Source+: distance 107.48 Mkm) via the standard Hill approximation,'),
            (582,
             '    #         Shan et al. 2015 -- induced bow shock 1.3-1.7 R_V.',
             '    # Source+: Shan et al. 2015 -- induced bow shock 1.3-1.7 R_V.'),
            (581,
             '    #         extends to ~45-60 R_V under active conditions;',
             '    # Source+: extends to ~45-60 R_V under active conditions;'),
            (524,
             '#         Shan et al. 2015 -- induced bow shock 1.4 R_V (range 1.36-1.46).',
             '# Source+: Shan et al. 2015 -- induced bow shock 1.4 R_V (range 1.36-1.46).'),
            (523,
             '#         Zhang et al. 2007 -- induced magnetopause ~1.05 R_V;',
             '# Source+: Zhang et al. 2007 -- induced magnetopause ~1.05 R_V;'),
            (430,
             '        #         (SPICAV/Venus Express stellar occultation). Mesosphere extent only.',
             '        # Source+: (SPICAV/Venus Express stellar occultation). Mesosphere extent only.'),
            (333,
             '#         Sanchez-Lavega 2018 -- troposphere/tropopause top range 60-65 km.',
             '# Source+: Sanchez-Lavega 2018 -- troposphere/tropopause top range 60-65 km.'),
            (332,
             '#         temperature 464 degC, CO2 96.5%, N2 3.5%.',
             '# Source+: temperature 464 degC, CO2 96.5%, N2 3.5%.'),
            (58,
             '        #         iron-nickel core, radius ~3,200 km, no dynamo (slow rotation or solid core).',
             '        # Source+: iron-nickel core, radius ~3,200 km, no dynamo (slow rotation or solid core).'),
            (39,
             '#         iron-nickel core, radius ~3,200 km, lack of dynamo due to slow rotation or solid core.',
             '# Source+: iron-nickel core, radius ~3,200 km, lack of dynamo due to slow rotation or solid core.'),
        ],
    },
}


def normalized(data):
    return data.replace(b'\r\n', b'\n')


def main():
    if not os.path.isfile('constants_new.py'):
        print('ERROR: run this from the palomas_orrery repo root '
              '(the folder holding constants_new.py).')
        return 1

    staged = []
    total = 0

    for name in sorted(EDITS):
        spec = EDITS[name]
        if not os.path.isfile(name):
            print('ERROR: %s not found.' % name)
            return 1

        with open(name, 'rb') as handle:
            raw = handle.read()

        fp = hashlib.md5(normalized(raw)).hexdigest()
        if fp != spec['fp']:
            print('ERROR: %s does not match the base this patch was built '
                  'against.' % name)
            print('       expected %s' % spec['fp'])
            print('       found    %s' % fp)
            print('       Nothing written. Commit or revert local edits, '
                  'then re-run.')
            return 1

        crlf = b'\r\n' in raw
        text = normalized(raw).decode('utf-8')
        lines = text.split('\n')

        for number, old, new in spec['edits']:
            index = number - 1
            if index < 0 or index >= len(lines):
                print('ANCHOR FAIL: %s line %d is past end of file.'
                      % (name, number))
                return 1
            if lines[index] != old:
                print('ANCHOR FAIL: %s line %d does not read as recorded.'
                      % (name, number))
                print('       expected %r' % old)
                print('       found    %r' % lines[index])
                print('       Nothing written.')
                return 1
            lines[index] = new

        out = '\n'.join(lines).encode('utf-8')
        try:
            out.decode('ascii')
        except UnicodeDecodeError:
            print('ERROR: %s would contain non-ASCII bytes. Nothing written.'
                  % name)
            return 1
        if crlf:
            out = out.replace(b'\n', b'\r\n')
        staged.append((name, out, len(spec['edits'])))
        total += len(out)

    for name, out, count in staged:
        with open(name, 'wb') as handle:
            handle.write(out)
        print('ok  %-34s %2d lines marked' % (name, count))

    print('patch applied (%d bytes)' % total)
    return 0


if __name__ == '__main__':
    sys.exit(main())
