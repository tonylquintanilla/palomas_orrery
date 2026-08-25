#,Constant,Code value,Code's source line,Your value,Your source,Value correct?,Citation correct?,Notes
1,GRAVITATIONAL_CONSTANT_SI -- Newtonian constant of gravitation,6.67430e-11 m^3 kg^-1 s^-2,none,6.67430(15)×10−11 m3 kg−1 s−2,"CODATA 2018 / 2022 recommended values; Tiesinga et al. (2021), Rev. Mod. Phys. 93, 025010. DOI: 10.1103/RevModPhys.93.025010",YES,UNSOURCED,Exact match to the CODATA recommended central value with relative standard uncertainty of 2.2×10−5.
2,SOLAR_MASS_KG -- mass of the Sun,1.989e30 kg,none,1.98841×1030 kg,IAU 2015 Resolution B3 (nominal solar mass parameter (GM)⊙N​≡1.3271244×1020 m3 s−2) divided by CODATA 2018 G.,APPROX,UNSOURCED,The mass of the Sun is a derived quantity (GM)⊙​/G. The code value 1.989×1030 kg is rounded to 4 significant figures (+0.03% offset from derived value).
3,PARSEC_TO_AU -- astronomical units per parsec,206265.0 AU,none,π648000​ AU≈206264.806247 AU,IAU 2015 Resolution B2 (formal geometric definition 1 pc≡π180×3600​ AU).,APPROX,UNSOURCED,Exactly defined by IAU resolution as π648000​ AU. The code rounds this derived value to the nearest integer (206265.0).
4,SGR_A_MASS_SOLAR -- mass of Sagittarius A*,4.154e6 solar masses,# Source: GRAVITY Collaboration 2019,(4.154±0.014)×106 M⊙​,"GRAVITY Collaboration: Abuter et al. (2019), Astron. Astrophys. 625, L10, Table 1 / Section 3. DOI: 10.1051/0004-6361/201935656",YES,PARTIAL,"Value matches the combined orbit and spectroscopic fit in Abuter et al. (2019). Citation correctly attributes the collaboration and year, but omits paper title, journal reference, and DOI."
5,SGR_A_DISTANCE_LY -- distance to Sagittarius A*,26670.0 light-years,none,26673.1 ly (from R0​=8178 pc),"Derived from GRAVITY Collaboration: Abuter et al. (2019), Astron. Astrophys. 625, L10 (R0​=8178±13stat​±22sys​ pc) using IAU standard conversions.",APPROX,UNSOURCED,Primary publications report Galactic center distance in parsecs (8178 pc). Converting 8178 pc×3.261563777 ly/pc yields ≈26673.1 ly. The code rounds 26.673 kly to 4 significant figures (26670 ly).

### `worksheet_gemini-2.5-pro_L247_sgr_a_constants_20260825.md`

| # | Constant | Code value | Code's source line | Your value | Your source | Value correct? | Citation correct? | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `GRAVITATIONAL_CONSTANT_SI` -- Newtonian constant of gravitation | 6.67430e-11 m^3 kg^-1 s^-2 | none | $6.67430(15) \times 10^{-11}\text{ m}^3\text{ kg}^{-1}\text{ s}^{-2}$ | CODATA 2018 / 2022 recommended values; Tiesinga et al. (2021), *Rev. Mod. Phys.* 93, 025010. DOI: 10.1103/RevModPhys.93.025010 | YES | UNSOURCED | Exact match to the CODATA recommended central value with relative standard uncertainty of $2.2 \times 10^{-5}$. |
| 2 | `SOLAR_MASS_KG` -- mass of the Sun | 1.989e30 kg | none | $1.98841 \times 10^{30}\text{ kg}$ | IAU 2015 Resolution B3 (nominal solar mass parameter $(GM)_\odot^N \equiv 1.3271244 \times 10^{20}\text{ m}^3\text{ s}^{-2}$) divided by CODATA 2018 $G$. | APPROX | UNSOURCED | The mass of the Sun is a derived quantity $(GM)_\odot / G$. The code value $1.989 \times 10^{30}\text{ kg}$ is rounded to 4 significant figures ($+0.03\%$ offset from derived value). |
| 3 | `PARSEC_TO_AU` -- astronomical units per parsec | 206265.0 AU | none | $\frac{648000}{\pi}\text{ AU} \approx 206264.806247\text{ AU}$ | IAU 2015 Resolution B2 (formal geometric definition $1\text{ pc} \equiv \frac{180 \times 3600}{\pi}\text{ AU}$). | APPROX | UNSOURCED | Exactly defined by IAU resolution as $\frac{648000}{\pi}\text{ AU}$. The code rounds this derived value to the nearest integer ($206265.0$). |
| 4 | `SGR_A_MASS_SOLAR` -- mass of Sagittarius A* | 4.154e6 solar masses | `# Source: GRAVITY Collaboration 2019` | $(4.154 \pm 0.014) \times 10^6\ M_\odot$ | GRAVITY Collaboration: Abuter et al. (2019), *Astron. Astrophys.* 625, L10, Table 1 / Section 3. DOI: 10.1051/0004-6361/201935656 | YES | PARTIAL | Value matches the combined orbit and spectroscopic fit in Abuter et al. (2019). Citation correctly attributes the collaboration and year, but omits paper title, journal reference, and DOI. |
| 5 | `SGR_A_DISTANCE_LY` -- distance to Sagittarius A* | 26670.0 light-years | none | $26673.1\text{ ly}$ (from $R_0 = 8178\text{ pc}$) | Derived from GRAVITY Collaboration: Abuter et al. (2019), *Astron. Astrophys.* 625, L10 ($R_0 = 8178 \pm 13_{\text{stat}} \pm 22_{\text{sys}}\text{ pc}$) using IAU standard conversions. | APPROX | UNSOURCED | Primary publications report Galactic center distance in parsecs ($8178\text{ pc}$). Converting $8178\text{ pc} \times 3.261563777\text{ ly/pc}$ yields $\approx 26673.1\text{ ly}$. The code rounds $26.673\text{ kly}$ to 4 significant figures ($26670\text{ ly}$). |

---

**Findings**

* **`GRAVITATIONAL_CONSTANT_SI` (Row 1):** The code value `6.67430e-11` reproduces the official CODATA 2018 / 2022 recommended value. Precision is preserved without overstatement.
* **`SOLAR_MASS_KG` (Row 2):** Mass of the Sun is fundamentally constrained via the heliocentric gravitational constant $(GM)_\odot$. IAU 2015 Resolution B3 defines the nominal parameter $(GM)_\odot^N = 1.3271244 \times 10^{20}\text{ m}^3\text{ s}^{-2}$. Dividing by CODATA $G = 6.67430 \times 10^{-11}\text{ m}^3\text{ kg}^{-1}\text{ s}^{-2}$ gives:

$$\frac{1.3271244 \times 10^{20}}{6.67430 \times 10^{-11}} \approx 1.9884095 \times 10^{30}\text{ kg}$$



The code's `1.989e30` represents a textbook rounded constant. If high-precision orbital propagation is intended, either defining $M_\odot = (GM)_\odot^N / G$ programmatically or retaining at least 5 significant figures ($1.98841 \times 10^{30}\text{ kg}$) prevents precision loss.
* **`PARSEC_TO_AU` (Row 3):** Under IAU 2015 Resolution B2, the parsec is explicitly derived from the astronomical unit rather than measured independently:

$$1\text{ pc} = \frac{1\text{ AU}}{\tan(1'')} \approx \frac{648000}{\pi}\text{ AU} \approx 206264.80624709636\text{ AU}$$



Using `206265.0` introduces a relative error of $\approx 9.4 \times 10^{-7}$. The value should ideally be computed dynamically as `648000.0 / math.pi`.
* **`SGR_A_MASS_SOLAR` (Row 4):** The primary paper corresponding to `# Source: GRAVITY Collaboration 2019` is *“A geometric distance measurement to the Galactic center black hole with 0.3% uncertainty”* (Abuter et al., *A&A* 625, L10, 2019). Table 1 / Section 3 of that work reports the black hole mass as $M_\bullet = (4.154 \pm 0.014) \times 10^6\ M_\odot$ when using the combined S2 orbit fitting. The attribution is accurate in substance but should cite the specific paper and DOI.
* **`SGR_A_DISTANCE_LY` (Row 5):** Astrometric surveys report the Galactic Center distance ($R_0$) in parsecs ($R_0 = 8178 \pm 13_{\text{stat}} \pm 22_{\text{sys}}\text{ pc}$ in Abuter et al. 2019; and $8277 \pm 9_{\text{stat}} \pm 30_{\text{sys}}\text{ pc}$ in GRAVITY 2021). Converting $8178\text{ pc}$ using the Julian light-year ($1\text{ ly} \equiv 9.4607304725808 \times 10^{15}\text{ m}$) yields $26673.1\text{ ly}$. The value `26670.0` truncates the conversion to 4 significant digits ($26.67\text{ kly}$).