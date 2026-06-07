# Paloma's Orrery - Distribution Strategy

**Created:** November 29, 2025  
**Status:** Planning & Implementation  
**Current Version:** v1.0.0

---

## Overview

This document outlines the strategy for distributing Paloma's Orrery to different audiences through multiple channels. The goal is to make the orrery accessible to everyone from friends and family to the broader astronomy and climate education community.

### What We're Distributing

| Asset | Size | Audience |
|-------|------|----------|
| Windows Executable (zip) | ~250-350 MB | General users (no Python needed) |
| Python Source Code | ~15,000 lines | Developers, educators, contributors |
| macOS Executable (planned) | TBD | Mac users (Paloma!) |

### Distribution Package Contents

```
Palomas_Orrery_v1.0.0_Windows.zip
└── palomas_orrery/
    ├── START_HERE.bat           ← Menu launcher
    ├── README.txt               ← User guide
    ├── palomas_orrery.exe       ← Solar system (~44 MB)
    ├── star_visualization.exe   ← Stars (~43 MB)
    ├── reports/                 ← Generated outputs
    └── _internal/               ← Shared dependencies & data (~500 MB)
        ├── data/                ← Orbit cache, climate data (~100 MB)
        └── star_data/           ← Stellar catalogs (~330 MB)
```

---

## Distribution Channels

### 1. GitHub Releases (Primary - Public)

**Status:** 🔲 To implement

GitHub Releases is the standard for distributing software alongside source code.

**Benefits:**
- Direct download links (no clone/checkout needed)
- Version history with release notes
- Large file support (up to 2 GB per release asset)
- Professional appearance
- Links work from anywhere (Instagram bio, website, etc.)

**How to Create a Release:**
1. Go to repository → "Releases" → "Draft a new release"
2. Create tag (e.g., `v1.0.0`)
3. Upload `Palomas_Orrery_v1.0.0_Windows.zip` as release asset
4. Write release notes (features, requirements, known issues)
5. Publish

**Result:** Direct download link:
```
https://github.com/TonyQuintanilla/palomas_orrery/releases/download/v1.0.0/Palomas_Orrery_v1.0.0_Windows.zip
```

**Release Notes Template:**
```markdown
## Paloma's Orrery v1.0.0

### What's New
- Initial public release
- Solar system visualization with real NASA JPL data
- Star visualization with 123,000+ stars from Hipparcos/Gaia
- Climate and paleoclimate data preservation
- Interactive 3D Plotly visualizations

### System Requirements
- Windows 10/11 (64-bit)
- 4 GB RAM minimum (8 GB recommended)
- 1 GB disk space
- Internet connection (optional, for live JPL data)

### Installation
1. Download the zip file below
2. Extract to any folder
3. Run `START_HERE.bat`

### Known Issues
- First launch takes 30-60 seconds (normal)
- "Windows protected your PC" warning appears (click "More info" → "Run anyway")

### Data Sources
NASA JPL Horizons, ESA Gaia/Hipparcos, NOAA, NASA GISS, NSIDC, EPICA, LR04
```

---

### 2. Physical USB Drive (Friends & Family)

**Status:** ✅ Ready to implement

Perfect for personal sharing with friends and family who may not be comfortable with downloads.

**Recommended USB Structure:**
```
USB Drive (PALOMAS_ORRERY)/
├── CLICK_ME_FIRST.txt          ← Simple instructions
├── Palomas_Orrery_v1.0.0.zip   ← For copying elsewhere
└── palomas_orrery/             ← Ready to run from USB
    ├── START_HERE.bat
    ├── README.txt
    └── ...
```

**CLICK_ME_FIRST.txt Content:**
```
================================================================================
                    WELCOME TO PALOMA'S ORRERY!
================================================================================

TO RUN DIRECTLY FROM THIS USB:
  1. Open the "palomas_orrery" folder
  2. Double-click "START_HERE.bat"
  3. Wait 30-60 seconds for first launch

FOR BETTER PERFORMANCE:
  Copy the "palomas_orrery" folder to your computer first,
  then run START_HERE.bat from there.

TO SAVE A COPY:
  The zip file "Palomas_Orrery_v1.0.0.zip" contains everything.
  Copy it to your computer and extract wherever you like.

QUESTIONS?
  See README.txt inside the palomas_orrery folder
  Or contact: tonyquintanilla@gmail.com

================================================================================
                 "The sky's the limit! Or the stars are the limit!"
================================================================================
```

**USB Specifications:**
- Minimum size: 4 GB (8 GB recommended for headroom)
- Format: FAT32 (maximum compatibility) or NTFS
- Label: "PALOMAS_ORRERY" or similar

**Performance Note:**
Running directly from USB works but may be slower, especially on first launch. Recommend copying to local drive for regular use.

---

### 3. Google Drive (Backup/Alternative)

**Status:** 🔲 To implement

Secondary hosting for users unfamiliar with GitHub or as backup.

**Setup:**
1. Upload `Palomas_Orrery_v1.0.0_Windows.zip` to Google Drive
2. Set sharing to "Anyone with the link can view"
3. Get shareable link

**Limitations:**
- Large file downloads may require Google account
- Download links less clean than GitHub
- No version history or release notes

**Use Case:** 
- Backup if GitHub has issues
- Direct sharing with specific people
- Mirror for website downloads

---

### 4. Website Integration

**Status:** 🔲 To implement

Your website serves as the central hub connecting all distribution channels.

**Suggested Download Page Structure:**

```markdown
# Download Paloma's Orrery

## Windows Executable (Recommended)
No Python installation required. Just download, extract, and run!

**[Download v1.0.0 for Windows](github-release-link)** (350 MB)

Requirements:
- Windows 10/11 (64-bit)
- 4 GB RAM minimum
- 1 GB disk space

## Python Source Code
For developers, educators, and contributors.

**[View on GitHub](https://github.com/TonyQuintanilla/palomas_orrery)**

Requirements:
- Python 3.11+
- See requirements.txt for dependencies

## macOS (Coming Soon)
Mac version for Paloma and other Mac users - in development!
```

---

### 5. Instagram (@palomas_orrery)

**Status:** ✅ Active (visualizations)

Instagram is ideal for showcasing visualizations and driving traffic to downloads.

**Bio Link Strategy:**
- Use link aggregator (Linktree, etc.) or direct to website
- Include clear "Download" option

**Example Linktree Structure:**
```
🌍 Download the Orrery (Windows)
🐍 Python Source Code (GitHub)
🌐 Website
📺 YouTube Channel
```

**Post Strategy:**
- When sharing visualizations: "Made with Paloma's Orrery - free download in bio"
- Create "How to Get It" story highlight
- Occasional "New Release" posts for major updates

---

### 6. YouTube

**Status:** ✅ Active (videos)

Video descriptions can link to downloads.

**Description Template:**
```
Created with Paloma's Orrery - a free astronomical visualization system.

🔗 DOWNLOAD: [GitHub release link]
🔗 SOURCE CODE: https://github.com/TonyQuintanilla/palomas_orrery
🔗 INSTAGRAM: @palomas_orrery

Paloma's Orrery visualizes our solar system and stellar neighborhood using 
real data from NASA JPL Horizons, ESA Gaia/Hipparcos, and climate monitoring 
institutions.

"Data Preservation is Climate Action"
```

---

## Licensing

### Current Status

- **Python Source Code:** MIT License ✅
- **Executable Distribution:** MIT License (inherited from source)
- **Data:** Various sources with attribution requirements

### MIT License (Current)

The MIT license is appropriate for both source and executable:
- Simple and permissive
- Allows any use including commercial
- Requires only attribution
- Industry standard for open source

### Data Attribution

Data incorporated from third parties has its own terms:

| Source | License/Terms |
|--------|---------------|
| NASA JPL Horizons | Public domain (US government) |
| ESA Gaia/Hipparcos | Free for non-commercial; citation required |
| NOAA climate data | Public domain (US government) |
| NASA GISS | Public domain (US government) |
| NSIDC | Public domain with attribution |
| EPICA ice core | Academic citation required |
| LR04 benthic stack | Academic citation required |

### Suggested License Notice

For README and distribution:

```
LICENSE
=======

Paloma's Orrery source code is released under the MIT License.
See LICENSE file for full terms.

DATA ATTRIBUTION
================

This software incorporates scientific data from multiple sources:

Public Domain (US Government):
- NASA JPL Horizons ephemeris calculations
- NOAA Global Monitoring Laboratory CO2 measurements
- NASA GISS temperature records

ESA Data (citation required):
- Gaia DR3 stellar catalog
- Hipparcos stellar catalog

Academic Data (citation required for research use):
- EPICA Dome C ice core data
- LR04 benthic stack

Users should cite original data sources in academic or professional work.
See DATA_SOURCES section in README.txt for complete attribution.
```

---

## Version Numbering

Following semantic versioning (SemVer):

```
v MAJOR . MINOR . PATCH
  │        │       └── Bug fixes, minor tweaks
  │        └────────── New features, data updates
  └─────────────────── Breaking changes, major overhaul
```

**Examples:**
- `v1.0.0` → Initial release
- `v1.0.1` → Bug fix (e.g., fixed startup crash)
- `v1.1.0` → New feature (e.g., added asteroid belt visualization)
- `v2.0.0` → Major change (e.g., complete UI redesign)

**File Naming Convention:**
```
Palomas_Orrery_v1.0.0_Windows.zip
Palomas_Orrery_v1.1.0_Windows.zip
Palomas_Orrery_v1.1.0_macOS.zip
```

---

## macOS Build (Phase 2)

**Status:** 🔲 Planned (for Paloma)

### Requirements

PyInstaller does not cross-compile. Building macOS executable requires:
- macOS computer (or VM)
- Python 3.11+ installed
- All dependencies installed
- PyInstaller installed

### Options

**Option A: Direct Mac Access**
- Borrow/use a Mac
- Run same PyInstaller process
- Handle code signing (see below)

**Option B: GitHub Actions (CI/CD)**
- Automated builds on Mac runners
- More complex setup but fully automated
- Can build Mac releases without owning a Mac

**Option C: Friend with Mac**
- Send build instructions
- They run PyInstaller
- Less ideal but works

### macOS Code Signing

macOS Gatekeeper is stricter than Windows:

| Signing Status | User Experience |
|----------------|-----------------|
| Unsigned | "Cannot be opened because developer cannot be verified" |
| Ad-hoc signed | Same warning, but can be bypassed |
| Developer ID signed | Clean launch (requires $99/year Apple Developer account) |

**For initial distribution:**
- Unsigned is fine with instructions to bypass
- Instructions: Right-click → Open → Open (instead of double-click)

### macOS Build Checklist

When ready to build:

- [ ] Get Mac access (hardware, VM, or CI/CD)
- [ ] Install Python 3.11+
- [ ] Install all requirements.txt dependencies
- [ ] Install PyInstaller
- [ ] Test Python version runs correctly
- [ ] Run PyInstaller build
- [ ] Test executable on clean Mac
- [ ] Create distribution zip
- [ ] Add to GitHub Release

---

## Distribution Checklist

### Pre-Release

- [ ] Version number updated in code
- [ ] README_DISTRIBUTION.txt updated
- [ ] All features tested in executable
- [ ] Build scripts run cleanly
- [ ] Distribution zip created and tested

### GitHub Release

- [ ] Create release tag (e.g., `v1.0.0`)
- [ ] Write release notes
- [ ] Upload Windows zip
- [ ] Upload macOS zip (when available)
- [ ] Publish release
- [ ] Test download link

### Other Channels

- [ ] Update website download page
- [ ] Update Google Drive mirror
- [ ] Prepare USB drives (if distributing physically)
- [ ] Instagram post announcing release
- [ ] YouTube video description updated

---

## Future Considerations

### Windows Installer (NSIS/Inno Setup)

**Benefits:**
- More professional appearance
- Start menu shortcuts
- Uninstaller included
- Optional desktop shortcut

**Complexity:** Medium - requires learning installer tools

**Priority:** Low (zip distribution works fine)

### Code Signing

**Benefits:**
- No "Windows protected your PC" warning
- No macOS Gatekeeper warning
- More trustworthy appearance

**Cost:**
- Windows: ~$200-400/year for certificate
- macOS: $99/year Apple Developer account

**Priority:** Low (warnings are acceptable with instructions)

### Auto-Update Mechanism

**Benefits:**
- Users get updates automatically
- No manual re-download needed

**Complexity:** High - requires update server, version checking

**Priority:** Low (manual updates fine for now)

### Dash Web Interface

**Benefits:**
- No download required at all
- Accessible from any device
- Always latest version

**Complexity:** High - requires hosting, deployment

**Priority:** Medium (significant accessibility improvement)

---

## Distribution Size Analysis

| Component | Size | Notes |
|-----------|------|-------|
| `palomas_orrery.exe` | 44 MB | Main orrery |
| `star_visualization.exe` | 43 MB | Star viewer |
| `_internal/` base | ~150 MB | Python runtime, DLLs |
| `data/` | ~100 MB | Orbit cache, climate |
| `star_data/` | ~330 MB | Stellar catalogs |
| **Total uncompressed** | ~500-600 MB | |
| **Total zipped** | ~250-350 MB | Distribution size |

### Potential Optimizations

**"Lite" versions (not recommended for v1.0):**
- Solar System Only: ~150 MB (exclude star_data)
- Stars Only: ~400 MB (minimal orbit data)

**Trade-off:** Added complexity in build/distribution vs. modest size savings.

**Recommendation:** Single combined distribution is simpler and ensures users get the full experience.

---

## Contact & Support

**Distribution questions:**
- Email: tonyquintanilla@gmail.com
- GitHub Issues: https://github.com/TonyQuintanilla/palomas_orrery/issues

**For users:**
- README.txt in distribution
- GitHub repository wiki (if created)
- Website FAQ (if created)

---

## Revision History

| Date | Version | Changes |
|------|---------|---------|
| 2025-11-29 | 1.0 | Initial distribution strategy document |

---

*"The sky's the limit! Or the stars are the limit!"* ⭐🚀

*"Data Preservation is Climate Action"*
