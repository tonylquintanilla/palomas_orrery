<!-- Doc-Kind: hand | JPL Horizons answers fetched by hand on 2026-10-07 during L-395's design round, verbatim. The Horizons check's offline tests are built on them. -->
# JPL Horizons answers, 2026-10-07 (L-395 design round)

Built on orrery 12693a53f9cb57c6beacada13f307985842b1780 at
https://github.com/tonylquintanilla/palomas_orrery, and gallery
4cfeca27d2a84171a0b278e20b1f79cf606a1f0b at
https://github.com/tonylquintanilla/tonyquintanilla.github.io.

Companion to `documentation/DESIGN_L395_horizons_check_20261007.md`.

## What this file is

- Every answer below was fetched by Tony in his browser on 2026-10-07,
  from JPL's own services, and pasted into the design session.
- They are copied here as pasted. A paste is an unverified transfer
  (safe-file-editing), so these are what reached the chat, not a
  byte-exact download.
- They were also copied once more, by Claude, from the chat into this
  file. So the build session re-fetches each one before its tests rely
  on it, and names any difference.
- The build session turns them into the check's offline test data.
  The check's first live run then shows whether JPL's live answers
  read the same way.
- Two services answered:
  - The Lookup service, `https://ssd.jpl.nasa.gov/api/horizons_lookup.api`,
    which resolves a name or number to objects. Its answers say
    `API VERSION: 1.1`.
  - Horizons' main service, `https://ssd.jpl.nasa.gov/api/horizons.api`,
    which answers about one record, or lists the records for a
    designation. Its answers say `API VERSION: 1.2`.
- Two planned queries were skipped as not needed: "499" and "10" with
  the major-body limiter (`group=mb`). The "499" one was in fact run
  later, as part of Group D.

## Group A: bare numbers, both indexes

### A1. `sstr=9`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=9&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = Pluto Barycenter
Type               = barycenter
Primary SPKID      = 9
Primary designation= 
Aliases            = 

Object name        = Apollo 9 S-IVB (spacecraft)
Type               = spacecraft
Primary SPKID      = -399090
Primary designation= 1969-018B
Aliases            = 

Object name        = DART Falcon 9 Booster (spacecraft)
Type               = spacecraft
Primary SPKID      = -149498
Primary designation= 2021-110B
Aliases            = 

Object name        = Falcon 9 RB Booster
Type               = spacecraft
Primary SPKID      = -162719
Primary designation= 2025-010D
Aliases            =
```

### A2. `sstr=499`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=499&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = Mars
Type               = planet
Primary SPKID      = 499
Primary designation= 
Aliases            = 

Object name        = 499 Venusia
Type               = asteroid (integrated barycenter)
Primary SPKID      = 20000499
Primary designation= A902 YE
Aliases            = 1950 CE, 2000499, J02Y00E
```

### A3. `sstr=10`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=10&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = Sun
Type               = Sun
Primary SPKID      = 10
Primary designation= 
Aliases            = Sol

Object name        = Pioneer 10 (spacecraft)
Type               = spacecraft
Primary SPKID      = -23
Primary designation= 1972-012A
Aliases            = 

Object name        = Apollo 10 S-IVB (spacecraft)
Type               = spacecraft
Primary SPKID      = -399100
Primary designation= 1969-043B
Aliases            = 

Object name        = Apollo 10 LM (spacecraft)
Type               = spacecraft
Primary SPKID      = -399101
Primary designation= 1969-059C
Aliases            = Snoopy

Object name        = 10 Hygiea
Type               = asteroid (integrated barycenter)
Primary SPKID      = 20000010
Primary designation= A849 GA
Aliases            = A900 GA, 2000010, I49G00A
```

## Group B: the same, major-body index only

### B1. `sstr=9&group=mb`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=9&group=mb&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = Pluto Barycenter
Type               = barycenter
Primary SPKID      = 9
Primary designation= 
Aliases            = 

Object name        = Apollo 9 S-IVB (spacecraft)
Type               = spacecraft
Primary SPKID      = -399090
Primary designation= 1969-018B
Aliases            = 

Object name        = DART Falcon 9 Booster (spacecraft)
Type               = spacecraft
Primary SPKID      = -149498
Primary designation= 2021-110B
Aliases            = 

Object name        = Falcon 9 RB Booster
Type               = spacecraft
Primary SPKID      = -162719
Primary designation= 2025-010D
Aliases            =
```

## Group C: Apophis, small-body index only

### C1. `sstr=2004 MN4&group=sb`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=2004%20MN4&group=sb&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = 99942 Apophis
Type               = asteroid (integrated barycenter)
Primary SPKID      = 20099942
Primary designation= 2004 MN4
Aliases            = 50264249, 3264226, 2099942, K04M04N
```

### C2. `sstr=99942&group=sb`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=99942&group=sb&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = 99942 Apophis
Type               = asteroid (integrated barycenter)
Primary SPKID      = 20099942
Primary designation= 2004 MN4
Aliases            = 50264249, 3264226, 2099942, K04M04N
```

## Group D: the planets, major-body index only

Each URL is
`https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=<id>&group=mb&format=text`.

### D1. `sstr=199&group=mb`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = Mercury
Type               = planet
Primary SPKID      = 199
Primary designation= 
Aliases            = 
```

### D2. `sstr=299&group=mb`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = Venus
Type               = planet
Primary SPKID      = 299
Primary designation= 
Aliases            = 
```

### D3. `sstr=399&group=mb`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = Earth
Type               = planet
Primary SPKID      = 399
Primary designation= 
Aliases            = Geocenter
```

### D4. `sstr=499&group=mb`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = Mars
Type               = planet
Primary SPKID      = 499
Primary designation= 
Aliases            = 
```

### D5. `sstr=599&group=mb`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = Jupiter
Type               = planet
Primary SPKID      = 599
Primary designation= 
Aliases            = 
```

### D6. `sstr=699&group=mb`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = Saturn
Type               = planet
Primary SPKID      = 699
Primary designation= 
Aliases            = 
```

### D7. `sstr=799&group=mb`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = Uranus
Type               = planet
Primary SPKID      = 799
Primary designation= 
Aliases            = 
```

### D8. `sstr=899&group=mb`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = Neptune
Type               = planet
Primary SPKID      = 899
Primary designation= 
Aliases            = 
```

## Group E: the wrong index, on purpose

### E1. `sstr=2004 MN4&group=mb`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=2004%20MN4&group=mb&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

NOTICE: no matches found
```

### E2. `sstr=499&group=sb`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=499&group=sb&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = 499 Venusia
Type               = asteroid (integrated barycenter)
Primary SPKID      = 20000499
Primary designation= A902 YE
Aliases            = 1950 CE, 2000499, J02Y00E
```

## Group F: comets, through the Lookup

### F1. `sstr=1P`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=1P&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = Halley
Type               = comet (integrated barycenter)
Primary SPKID      = 1000036
Primary designation= 1P
Aliases            = 1982 U1, 1909 R1, 1835 P1, 1758 Y1, 1682 Q1, 1607 S1, 1531 P1, 1456 K1, 1378 S1, 1301 R1, 1222 R1, 1145 G1, 1066 G1, 989, 989 N1, 912, 912 J1, 837, 837 F1, 760, 760 K1, 684, 684 R1, 66, 607, 607 H1, 530, 530 Q1, 451, 451 L1, 374, 374 E1, 295, 295 J1, 218, 218 H1, 1986 III, 1982i, 1910 II, 1909c, 1835 III, 1759 I, 1682, 1607, 1531, 1456, 141, 141 F1, 1378, 1301, 1222, 1145, 1066, 66 B1, -11 Q1, -86 Q1, -163 U1, -86, -239 K1, -239, -163, -11, 4000001
```

### F2. `sstr=90000030`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=90000030&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

NOTICE: no matches found
```

### F3. `sstr=2P`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=2P&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = Encke
Type               = comet (integrated barycenter)
Primary SPKID      = 1000025
Primary designation= 2P
Aliases            = 2025 NR197, 1822 L1, 1818 W1, 1805 U1, 1795 V1, 1786 B1, 1994 V, 1990 XXI, 1987 XIII, 1984 VI, 1980 XI, 1977 XI, 1974 V, 1971 II, 1970l, 1967h, 1967 XIII, 1964 IV, 1963h, 1961 I, 1960i, 1957c, 1957 VIII, 1954 IX, 1953f, 1951 III, 1950e, 1947i, 1947 XI, 1941b, 1941 V, 1937h, 1937 VI, 1934a, 1934 III, 1931a, 1931 II, 1928 II, 1927h, 1924b, 1924 III, 1921d, 1921 IV, 1918 I, 1917c, 1914d, 1914 VI, 1911d, 1911 III, 1908b, 1908 I, 1905 I, 1904b, 1901b, 1901 II, 1898d, 1898 III, 1895 I, 1894d, 1891c, 1891 III, 1888b, 1888 II, 1885 I, 1884d, 1881d, 1881 VII, 1878c, 1878 II, 1875a, 1875 II, 1871c, 1871 V, 1868 III, 1865 II, 1862 I, 1858 VIII, 1855 III, 1852 I, 1848 II, 1845 IV, 1842 I, 1838, 1835 II, 1832 I, 1829, 1825 III, 1822 II, 1819 I, 1805, 1795, 1786 I, 54604979, 4000002
```

### F4. `sstr=90000091`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=90000091&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

NOTICE: no matches found
```

### F5. `sstr=2026 A1&group=com`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=2026%20A1&group=com&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = MAPS (C/2026 A1)
Type               = comet (integrated barycenter)
Primary SPKID      = 1004111
Primary designation= C/2026 A1
Aliases            = K26A010
```

### F6. `sstr=C/2025 N1`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=C%2F2025%20N1&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = ATLAS (C/2025 N1)
Type               = comet (integrated barycenter)
Primary SPKID      = 1004083
Primary designation= C/2025 N1
Aliases            = 3I, K25N010
```

### F7. `sstr=3I`

URL: `https://ssd.jpl.nasa.gov/api/horizons_lookup.api?sstr=3I&format=text`

```
API VERSION: 1.1
API SOURCE: NASA/JPL Horizons Lookup API

Object name        = ATLAS (C/2025 N1)
Type               = comet (integrated barycenter)
Primary SPKID      = 1004083
Primary designation= C/2025 N1
Aliases            = 3I, K25N010
```

## Group G: pinned comet records, through Horizons' main service

### G1. Halley's pinned record, `COMMAND='90000030'`

URL: `https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='90000030'&OBJ_DATA=YES&MAKE_EPHEM=NO`

```
API VERSION: 1.2
API SOURCE: NASA/JPL Horizons API

*******************************************************************************
JPL/HORIZONS                      1P/Halley                2026-Oct-07 11:33:19
Rec #:90000030        Soln.date: 2025-Nov-21_15:57:34   # obs: 8518 (1835-1994)
 
IAU76/J2000 helio. ecliptic osc. elements (au, days, deg., period=Julian yrs):
 
  EPOCH=  2439875.5 ! 1968-Jan-20.0000000 (TDB)    RMSW= n.a.
   EC= .9679359956953212   QR= .5748638313743413   TP= 2446469.9736161465
   OM= 59.09894720612437   W= 112.2414314637764    IN= 162.1905300439129
   A= 17.92863504856929    MA= 274.3823371364693   ADIST= 35.28240626576424
   PER= 75.9152528074041   N= .012983244           ANGMOM= .018296559
   DAN= 1.78543            DDN= .82795             L= 305.8544912
   B= 16.4450919           MOID= .0745097          TP= 1986-Feb-08.4736161465
 
Comet physical (GM= km^3/s^2; RAD= km):
   GM= n.a.                RAD= 5.5
   M1=  5.5      M2=  13.6     k1=  8.     k2=  5.      PHCOF=  .030
Comet non-gravitational force model (AMRAT=m^2/kg;A1-A3=au/d^2;DT=days;R0=au):
   AMRAT=  0.                                      DT=  0.
   A1= 4.887055233121E-10  A2= 1.554720290005E-10  A3= 0.
 Non-standard or simulated/proxy model:
   ALN=  .1112620426   NK=  4.6142   NM=  2.15     NN=  5.093    R0=  2.808

COMET comments 
1: soln ref.= JPL#75, data arc: 1835-08-21 to 1994-01-11
2: k1=8.0, k2=5.0, phase coef.=0.03;
*******************************************************************************
```

### G2. Every Halley record, `COMMAND='DES=1P;'`

URL: `https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='DES=1P%3B'&OBJ_DATA=YES&MAKE_EPHEM=NO`

```
API VERSION: 1.2
API SOURCE: NASA/JPL Horizons API

*******************************************************************************
JPL/DASTCOM            Small-body Index Search Results     2026-Oct-07 11:34:03

 Comet AND asteroid index search:

    DES = 1P;

 Matching small-bodies: 

    Record #  Epoch-yr  >MATCH DESIG<  Primary Desig  Name  
    --------  --------  -------------  -------------  -------------------------
    90000001    -239    1P             1P              Halley
    90000002    -163    1P             1P              Halley
    90000003     -86    1P             1P              Halley
    90000004     -11    1P             1P              Halley
    90000005      66    1P             1P              Halley
    90000006     141    1P             1P              Halley
    90000007     218    1P             1P              Halley
    90000008     295    1P             1P              Halley
    90000009     374    1P             1P              Halley
    90000010     451    1P             1P              Halley
    90000011     530    1P             1P              Halley
    90000012     607    1P             1P              Halley
    90000013     684    1P             1P              Halley
    90000014     760    1P             1P              Halley
    90000015     837    1P             1P              Halley
    90000016     912    1P             1P              Halley
    90000017     989    1P             1P              Halley
    90000018    1066    1P             1P              Halley
    90000019    1145    1P             1P              Halley
    90000020    1222    1P             1P              Halley
    90000021    1301    1P             1P              Halley
    90000022    1378    1P             1P              Halley
    90000023    1456    1P             1P              Halley
    90000024    1531    1P             1P              Halley
    90000025    1607    1P             1P              Halley
    90000026    1682    1P             1P              Halley
    90000027    1759    1P             1P              Halley
    90000028    1835    1P             1P              Halley
    90000029    1910    1P             1P              Halley
    90000030    1968    1P             1P              Halley

 (30 matches. To SELECT, enter record # (integer), followed by semi-colon.)
*******************************************************************************
```

### G3. Encke's pinned record, `COMMAND='90000091'`

URL: `https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='90000091'&OBJ_DATA=YES&MAKE_EPHEM=NO`

```
API VERSION: 1.2
API SOURCE: NASA/JPL Horizons API

*******************************************************************************
JPL/HORIZONS                      2P/Encke                 2026-Oct-07 11:34:41
Rec #:90000091 (+COV) Soln.date: 2026-Oct-01_15:11:48    # obs: 880 (2018-2026)
 
IAU76/J2000 helio. ecliptic osc. elements (au, days, deg., period=Julian yrs):
 
  EPOCH=  2460147.5 ! 2023-Jul-22.0000000 (TDB)    RMSW= n.a.
   EC= .8469532425568865   QR= .3395910296522707   TP= 2460240.0266747689
   OM= 334.0240655739339   W= 187.2820411908973    IN= 11.33709697552753
   A= 2.218871117073451    MA= 332.4086523635144   ADIST= 4.098151204494632
   PER= 3.30526525077918   N= .298198846           ANGMOM= .013623462
   DAN= 3.92304            DDN= .34085             L= 161.165498
   B= -1.427808            MOID= .16594701         TP= 2023-Oct-22.5266747689
 
Comet physical (GM= km^3/s^2; RAD= km):
   GM= n.a.                RAD= 2.4
   M1=  15.7     M2=  n.a.     k1=  4.5    k2= n.a.     PHCOF= n.a.
Comet non-gravitational force model (AMRAT=m^2/kg;A1-A3=au/d^2;DT=days;R0=au):
   AMRAT=  0.                                      DT=  0.
   A1= 2.041002176702E-10  A2= 2.635817800183E-12  A3= 0.
 Non-standard or simulated/proxy model:
   ALN=  .1112620426   NK=  4.6142   NM=  2.15     NN=  5.093    R0=  2.808

COMET comments 
1: soln ref.= JPL#K273/20, data arc: 2018-11-05 to 2026-10-01
2: k1=4.5;
*******************************************************************************
```

### G4. Every Encke record, `COMMAND='DES=2P;'`

URL: `https://ssd.jpl.nasa.gov/api/horizons.api?format=text&COMMAND='DES=2P%3B'&OBJ_DATA=YES&MAKE_EPHEM=NO`

```
API VERSION: 1.2
API SOURCE: NASA/JPL Horizons API

*******************************************************************************
JPL/DASTCOM            Small-body Index Search Results     2026-Oct-07 11:35:16

 Comet AND asteroid index search:

    DES = 2P;

 Matching small-bodies: 

    Record #  Epoch-yr  >MATCH DESIG<  Primary Desig  Name  
    --------  --------  -------------  -------------  -------------------------
    90000031    1786    2P             2P              Encke
    90000032    1796    2P             2P              Encke
    90000033    1805    2P             2P              Encke
    90000034    1819    2P             2P              Encke
    90000035    1822    2P             2P              Encke
    90000036    1825    2P             2P              Encke
    90000037    1828    2P             2P              Encke
    90000038    1832    2P             2P              Encke
    90000039    1835    2P             2P              Encke
    90000040    1838    2P             2P              Encke
    90000041    1842    2P             2P              Encke
    90000042    1845    2P             2P              Encke
    90000043    1848    2P             2P              Encke
    90000044    1852    2P             2P              Encke
    90000045    1855    2P             2P              Encke
    90000046    1858    2P             2P              Encke
    90000047    1862    2P             2P              Encke
    90000048    1865    2P             2P              Encke
    90000049    1868    2P             2P              Encke
    90000050    1872    2P             2P              Encke
    90000051    1875    2P             2P              Encke
    90000052    1878    2P             2P              Encke
    90000053    1881    2P             2P              Encke
    90000054    1885    2P             2P              Encke
    90000055    1888    2P             2P              Encke
    90000056    1891    2P             2P              Encke
    90000057    1895    2P             2P              Encke
    90000058    1898    2P             2P              Encke
    90000059    1901    2P             2P              Encke
    90000060    1904    2P             2P              Encke
    90000061    1908    2P             2P              Encke
    90000062    1911    2P             2P              Encke
    90000063    1914    2P             2P              Encke
    90000064    1918    2P             2P              Encke
    90000065    1921    2P             2P              Encke
    90000066    1924    2P             2P              Encke
    90000067    1928    2P             2P              Encke
    90000068    1931    2P             2P              Encke
    90000069    1934    2P             2P              Encke
    90000070    1937    2P             2P              Encke
    90000071    1941    2P             2P              Encke
    90000072    1947    2P             2P              Encke
    90000073    1951    2P             2P              Encke
    90000074    1954    2P             2P              Encke
    90000075    1957    2P             2P              Encke
    90000076    1961    2P             2P              Encke
    90000077    1964    2P             2P              Encke
    90000078    1967    2P             2P              Encke
    90000079    1971    2P             2P              Encke
    90000080    1974    2P             2P              Encke
    90000081    1977    2P             2P              Encke
    90000082    1980    2P             2P              Encke
    90000083    1984    2P             2P              Encke
    90000084    1987    2P             2P              Encke
    90000085    1990    2P             2P              Encke
    90000086    1994    2P             2P              Encke
    90000087    1995    2P             2P              Encke
    90000088    1998    2P             2P              Encke
    90000089    2004    2P             2P              Encke
    90000090    2015    2P             2P              Encke
    90000091    2023    2P             2P              Encke

 (61 matches. To SELECT, enter record # (integer), followed by semi-colon.)
*******************************************************************************
```

### G5. MAPS, from Horizons' main service (object data only)

Tony's request for this one also returned an ephemeris for one date
(2025-Jan-01, before the comet's discovery). Only the object-data
block is kept here; the ephemeris is not used by the check.

```
*******************************************************************************
JPL/HORIZONS                  MAPS (C/2026 A1)             2026-Oct-07 11:51:16
Rec #:90004956 (+COV) Soln.date: 2026-Jun-05_03:03:24      # obs: 472 (74 days)
 
IAU76/J2000 helio. ecliptic osc. elements (au, days, deg., period=Julian yrs):
 
  EPOCH=  2461083.5 ! 2026-Feb-12.0000000 (TDB)    RMSW= n.a.
   EC= .9999626492034864   QR= .005729313972357485 TP= 2461135.0997441965
   OM= 7.865158402133161   W= 86.3247091505423     IN= 144.4936582288794
   A= 153.3920158911773    MA= 359.9732300543162   ADIST= 306.7783024683822
   PER= 1899.81947277601   N= .0005188             ANGMOM= .001841381
   DAN= .01077             DDN= .01224             L= 282.376828
   B= 35.4223137           MOID= .55581599         TP= 2026-Apr-04.5997441965
 
Comet physical (GM= km^3/s^2; RAD= km):
   GM= n.a.                RAD= n.a.
   M1=  14.8     M2=  n.a.     k1=  14.5   k2= n.a.     PHCOF= n.a.

COMET comments 
1: soln ref.= JPL#13, data arc: 2026-01-13 to 2026-03-28
2: k1=14.5;
*******************************************************************************
```

Written October 7, 2026 with Anthropic's Claude Opus 5.5.
