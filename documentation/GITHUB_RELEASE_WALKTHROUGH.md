# GitHub Release Walkthrough

## Paloma's Orrery Release Process

**Last updated:** January 11, 2026

---

## Before You Start

### Choose the Right Source Folder!

| Folder | Purpose | Use for Release ZIP? |
|--------|---------|---------------------|
| `palomas_orrery_for_github` | Git repo with `.git/` folder | ❌ NO - contains git history (~200+ MB bloat) |
| `google_drive_repository_for_upload` | Clean copy for distribution | ✅ YES - no git overhead |

**Lesson learned (v2.2.0):** Using the git repo folder accidentally included `.git/` and ballooned the ZIP from ~220 MB to ~489 MB!

---

## Pre-Release Checklist

### 1. Sync Code to Release Folder

Make sure `google_drive_repository_for_upload/palomas_orrery_cross_platform` has:

- [ ] All latest `*.py` files (copy from working folder or git repo)
- [ ] Latest `README.md` in root
- [ ] Latest `requirements.txt` in root
- [ ] `.gitignore` file
- [ ] Launcher scripts:
  - [ ] `START_HERE.bat` (Windows)
  - [ ] `start_orrery.command` (macOS)
  - [ ] `start_orrery.desktop` (Linux)
- [ ] Updater scripts:
  - [ ] `UPDATE_CODE.bat` (Windows)
  - [ ] `update_code.sh` (macOS/Linux)
  - [ ] `update_code.desktop` (Linux)

### 2. Check Data Files

- [ ] `data/orbit_paths.json` (main cache ~100 MB)
- [ ] `data/orbit_paths_backup.json` (ONE backup only)
- [ ] `data/osculating_cache.json`
- [ ] `data/` climate files (co2, temperature, sea_level, etc.)
- [ ] `star_data/*.vot` files (Gaia, Hipparcos)
- [ ] `star_data/*.pkl` files (star properties)

### 3. Remove Bloat

DELETE these before zipping:

- [ ] `.git/` folder (if present - BIG!)
- [ ] `__pycache__/` folder
- [ ] Extra backup files:
  - [ ] `orbit_paths.json.backup_old`
  - [ ] `orbit_paths.json.verify_backup.*`
  - [ ] `*.backup_old` files
  - [ ] Keep only ONE `.backup` per data file

### 4. Verify No Sensitive Files

- [ ] No API keys or credentials
- [ ] No personal paths hardcoded
- [ ] No test files with personal data

---

## Create the Release ZIP

### Step 1: Create ZIP File

1. Open `google_drive_repository_for_upload` folder
2. Right-click on `palomas_orrery_cross_platform` (or your release folder)
3. Select "Send to" → "Compressed (zipped) folder"
4. Rename to `palomas_orrery_X_X_zip.zip` (e.g., `palomas_orrery_2_2_zip.zip`)

### Step 2: Verify ZIP Size

| Expected Size | Status |
|---------------|--------|
| 130-250 MB | ✅ Normal |
| 400+ MB | ⚠️ Check for `.git/` folder or extra backups! |

### Step 3: Test the ZIP (Optional but Recommended)

1. Extract to a test location
2. Verify folder structure looks correct
3. Check that `palomas_orrery.py` is present
4. Check that `data/` and `star_data/` have files

---

## Push Code to GitHub

### Step 1: Commit Changes

In GitHub Desktop (with `palomas_orrery_for_github` repo):

1. Review all changes in "Changes" tab
2. Write commit message describing what's new
3. Click "Commit to main"
4. Click "Push origin"

### Step 2: Verify on GitHub.com

1. Go to https://github.com/tonylquintanilla/palomas_orrery
2. Check that latest files are there
3. Verify commit message appears

---

## Create GitHub Release

### Step 1: Go to Releases

1. Go to https://github.com/tonylquintanilla/palomas_orrery
2. SIGN IN
3. Click "Releases" (right sidebar)
4. Click "Create a new release" (or "Draft a new release")

### Step 2: Fill in Release Details

**Tag version:** `v2.X.0` (e.g., `v2.2.0`)

**Release title:** `v2.X.0 - Brief Description`

**Description template:**
```markdown
## What's New

- Feature 1
- Feature 2
- Bug fix 1

## Downloads

- `palomas_orrery_X_X_zip.zip` - Python source + data files (Windows, macOS, Linux)

## Notes

- Python 3.11-3.13 supported
- See README.md for installation instructions

Tony Quintanilla | tonyquintanilla@gmail.com
```

### Step 3: Attach Files

1. Drag and drop `palomas_orrery_X_X_zip.zip` into the upload area
2. Wait for upload to complete
3. Verify file appears in "Assets"

### Step 4: Publish

1. Review everything one more time
2. Click "Publish release"

---

## Update an Existing Release

### Replace a ZIP File (Same Filename)

If you need to fix a release (e.g., ZIP was too big, missing files):

1. Go to https://github.com/tonylquintanilla/palomas_orrery/releases
2. SIGN IN!
3. Find the release you want to update
4. Click **"Edit"** (pencil icon, top right of release)
5. Scroll down to "Assets"
6. Click the **"X"** next to the file you want to remove
7. Confirm deletion
8. Drag and drop the corrected ZIP file
9. Wait for upload to complete
10. Click **"Update release"**

**Note:** Users who already downloaded the old file won't automatically get the new one. The download count resets for the new file.

### Update Release Notes Only

1. Go to the release page
2. Click **"Edit"**
3. Modify the description text
4. Click **"Update release"**

The tag and attached files remain unchanged.

### Add Additional Files to Existing Release

1. Go to the release page
2. Click **"Edit"**
3. Drag and drop new files into the Assets area
4. Click **"Update release"**

### Delete a Release Entirely

1. Go to the release page
2. Click **"Edit"**
3. Scroll to the bottom
4. Click **"Delete this release"** (red button)
5. Confirm deletion

**Warning:** This removes the release but NOT the git tag. To remove the tag too:
```bash
git push --delete origin v2.X.0
```

### Create a Patch Release (v2.2.1)

If the fix is significant, consider a new patch release instead of replacing:

1. Create new ZIP with fixes
2. Create new release with tag `v2.2.1`
3. Note in description: "Fixes issue in v2.2.0: [description]"
4. Leave old release in place (some users may have linked to it)

---

## Post-Release

### Update Google Drive

1. Upload new ZIP to Google Drive repository folder
2. (Optional) Remove old version or rename to `_archived`

### Update Google Sites Webpage

1. Update version number if mentioned
2. Update "last updated" date
3. Update any changed download links

### Announce (Optional)

- Instagram post
- Reddit r/vibecoding
- Email interested parties

---

## Updating Local Repositories (Linux/macOS)

After pushing changes from Windows, other machines may not get updates immediately.

### Full Update (All Files)

```bash
cd ~/Desktop/palomas_orrery
git fetch origin
git reset --hard origin/main
```

This overwrites ALL local files with exactly what's on GitHub.

### Single File Update (Faster)

If you only changed one file and want to pull just that:

```bash
cd ~/Desktop/palomas_orrery
git checkout origin/main -- palomas_orrery.py
```

Replace `palomas_orrery.py` with whatever file you need.

### Verify a File is on GitHub

Before pulling, confirm your changes actually made it to GitHub:

```bash
# Check if a specific change is in the remote file
curl -s "https://raw.githubusercontent.com/tonylquintanilla/palomas_orrery/main/palomas_orrery.py" | grep "your_search_term"
```

### Why Updates Might Not Appear

| Symptom | Cause | Fix |
|---------|-------|-----|
| File date updated but content unchanged | `git fetch` succeeded but `reset` didn't run | Run `git reset --hard origin/main` |
| Updater says "complete" but no changes | Push wasn't done from Windows | Go back to Windows, click "Push origin" |
| Changes on GitHub.com but not locally | Local cache issue | Use single file pull or full reset |

**Note:** There can be a brief lag (~1-2 minutes) between pushing to GitHub and the raw file being available. If `curl` shows old content, wait a moment and try again.

---

## Troubleshooting

### ZIP is too large (400+ MB)

Check for:
- `.git/` folder included (biggest culprit!)
- Multiple backup files (`*.backup`, `*.backup_old`, `*.verify_backup`)
- `__pycache__/` folders
- Accidentally nested folders

### Files missing from GitHub

If GitHub Desktop shows commits but files don't appear:
1. Try "Fetch origin" then "Pull"
2. If that fails, download files directly from GitHub.com
3. Check if `.gitignore` is excluding the files

### Release asset upload fails

- Check file size (GitHub limit is 2 GB)
- Check internet connection
- Try a different browser
- Try uploading via GitHub CLI: `gh release upload v2.X.0 filename.zip`

---

## Quick Reference

### Folder Purposes

```
google_drive_repository_for_upload/    ← RELEASE SOURCE (clean, no .git)
    palomas_orrery_cross_platform/
        data/
        star_data/
        *.py
        
palomas_orrery_for_github/             ← GIT REPO (has .git, for commits)
    .git/                              ← Don't include in release!
    data/
    star_data/
    *.py
    
palomas_orrery/                        ← WORKING COPY (daily development)
    data/
    star_data/
    *.py
```

### File Size Reference

| Component | Approximate Size |
|-----------|------------------|
| Python code (*.py) | ~2 MB |
| orbit_paths.json | ~100 MB |
| star_data/ (all files) | ~50 MB |
| Climate data | ~5 MB |
| ONE backup file | ~100 MB |
| **Total (clean)** | **~130-250 MB** |
| .git/ folder | ~200+ MB (EXCLUDE!) |

---

*Document created after the v2.2.0 "489 MB oops" incident*
