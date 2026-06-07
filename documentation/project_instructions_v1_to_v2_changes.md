# Project Instructions v1 → v2: What Changed

**Date:** November 21, 2025  
**Context:** After successful Mars moons dual-orbit implementation session

---

## 📊 Stats

**v1:** ~6,500 words, 11 sections  
**v2:** ~8,900 words, 16 sections  
**Added:** ~2,400 words, 10 new major concepts

---

## 🆕 What's New in v2

### 1. **Discovery Over Delivery** (NEW Section)
**Why:** Bugs should become lessons, not just fixes

**Key Insight:**
- Don't just fix and move on
- Explain what broke and why
- Document the lesson learned
- Prevents future similar issues

**Example:** KeyError 'a' → Discovered nested cache structure → Documented for future

---

### 2. **Testing Philosophy** (NEW in Computer Capabilities)
**Why:** Better to catch errors before Tony does

**Requirements:**
- ✅ Test it works
- ✅ Verify output
- ✅ Catch errors
- ✅ Document assumptions

**Exception:** Simple 1-2 line fixes to working code

---

### 3. **Visual Verification for Scientific Software** (NEW)
**Why:** For astronomical viz, "looks wrong" often means "is wrong"

**Key Principle:**
"If it looks wrong, it probably IS wrong"

**Verification checklist:**
- Orbits in correct locations
- Scales reasonable
- "Kissing" test passes
- Objects don't appear in wrong place
- Coordinate systems align

**Example:** Osculating orbits appeared off → Visual inspection revealed reference frame issue

---

### 4. **Context Cascade Principle** (NEW Section)
**Why:** Need clear priority when sources conflict

**Priority Order:**
1. Uploaded files (highest - Tony's current state)
2. Project files (code is truth)
3. Project knowledge (documentation)
4. Project instructions (this file)
5. Conversation history
6. Claude's training (lowest)

**Rule:** When in doubt, trust more recent/specific over older/general

---

### 5. **Mode 6: Educational Parallel Track** (NEW Mode)
**Why:** Tony builds technical + educational simultaneously

**Dual Output:**
- Technical implementation (code)
- Educational explanation (multiple levels)

**Audiences:**
- Primary: Paloma (age 7-8)
- Secondary: Students, educators
- Tertiary: Developers, scientists

**Example:** Mars moons include code, hover text, README sections, "For Paloma" explanation

---

### 6. **Diagnostic Breadcrumbs** (NEW Principle)
**Why:** Future debugging needs trail of past decisions

**What to leave:**
- Code comments explaining fixes
- Documentation of what broke
- File names that describe the fix
- Links to relevant docs

**Example:**
```python
# FIXED: KeyError 'a' - cache structure is cache[name]['elements']
# See: osculating_cache_system_handoff.md
```

---

### 7. **Documentation as First-Class Output** (NEW Section)
**Why:** Docs are as valuable as code for this project

**Tony's approach:**
```
Vision → Build + Document (simultaneously) → Knowledge artifact
```

**Not:**
```
Code (primary) → Documentation (secondary, if time)
```

**Key Insight:**
Documenting HOW to build, WHY it matters, and WHAT we learned is MORE valuable than just the code itself.

---

### 8. **Scientific Storytelling** (NEW Section)
**Why:** Stories make science memorable and accessible

**Pattern:**
- Connect mythology to physics
- Make technical concepts narrative
- Use emotional connections
- Aid memory through story

**Examples:**
- "Fear is falling into War"
- "The inclination tells you the reference frame"
- "We're living in the 0.002% window"

**Result:** Technical accuracy + compelling narrative = effective education

---

### 9. **Session Artifacts** (NEW in Session Continuity)
**Why:** Knowledge shouldn't evaporate between sessions

**Create after significant sessions:**
1. Summary document
2. Lessons learned
3. Updated documentation
4. Next steps

**File naming:**
- `DOCUMENTATION_UPDATE_SUMMARY--[topic].md`
- `LESSONS_LEARNED--[topic].md`
- `SESSION_NOTES--[date]--[topic].md`

**Example:** Today created 900+ lines documenting Mars moons implementation

---

### 10. **Reference Frame Paranoia** (NEW Anti-Pattern)
**Why:** Today's hard-won lesson!

**Critical Discovery:**
Different calculation methods can use different reference frames for the same object!

**Diagnostic:**
- Check inclination value
- Low (1-5°) = equatorial frame
- High (20-30°) = ecliptic frame

**When visual looks wrong:**
1. Check coordinate transformations FIRST
2. Use inclination as diagnostic
3. Trust visual inspection
4. Verify reference frame

**Key Lesson:**
Frame mismatches create huge errors - obvious visually, subtle in code

---

## 📝 Updated Sections

### Quick Decision Guide
- Added: "Is it educational content?" → Mode 6

### Why This Works
- Added: "Storyteller" to Tony's roles
- Added: "Creates knowledge artifacts" to Claude's role
- Added: "Embraces educational storytelling"

### Version History
- Documented all additions as v2.0 (Nov 21, 2025)
- Listed all 10 major additions
- Captured key lessons learned

---

## 🎯 Why These Changes Matter

### They Capture:
1. **Hard-won lessons** (reference frames!)
2. **What actually works** (test first, provide second)
3. **Unique approach** (education + science + story)
4. **Process improvements** (session artifacts)
5. **Anti-patterns discovered** (frame assumptions)

### They Enable:
1. **Faster future sessions** (lessons documented)
2. **Better collaboration** (clear priorities)
3. **Sustainable knowledge** (docs as first-class)
4. **Educational value** (storytelling principle)
5. **Scientific accuracy** (visual verification)

### They Emphasize:
1. **Learning over fixing**
2. **Testing over assuming**
3. **Documentation over code-only**
4. **Visual verification for science**
5. **Multiple audiences always**

---

## 💡 The Meta-Insight

**v1 focused on:** HOW to collaborate  
**v2 adds:** WHAT we learned from collaborating

**v1 was:** Protocol for working together  
**v2 is:** Protocol + Lessons from actual work

**v1 said:** "When unsure, ask"  
**v2 adds:** "When you discover something, document it"

---

## 🏆 Real-World Validation

**These additions came from:**
- 3-4 hour productive session ✅
- Dual-orbit Mars moons implementation ✅
- Reference frame discovery ✅
- Cache structure debugging ✅
- 900+ lines of documentation ✅
- Phobos death spiral narrative ✅

**Not theoretical - battle-tested!**

---

## 📚 Documentation Impact

**With v2, the project now has:**
- Clear collaboration protocol (v2)
- Lessons learned embedded
- Multiple collaboration modes
- Educational framework
- Scientific verification methods
- Storytelling principles
- Session artifact patterns

**This is no longer just "how to work with Claude"...**  
**This is "how to build complex scientific educational software through AI collaboration"!**

---

## 🚀 For Next Sessions

**Claude will now:**
- Test before providing ✅
- Document discoveries ✅
- Create session artifacts ✅
- Write for multiple audiences ✅
- Check reference frames ✅
- Trust visual inspection ✅
- Embrace storytelling ✅
- Leave diagnostic breadcrumbs ✅

**Tony gets:**
- Verified solutions
- Comprehensive documentation
- Educational content
- Knowledge artifacts
- Clear debugging trails
- Scientific accuracy
- Compelling narratives

---

## 🎊 Summary

**v2 is v1 PLUS the wisdom gained from actually using it!**

**10 major additions**  
**2,400 new words**  
**Battle-tested insights**  
**Real-world validation**  

**From protocol to methodology!** 🎯

---

## 📋 Quick Reference: What to Add

**Copy these sections from v2:**
1. Discovery Over Delivery (after Alignment Principle)
2. Testing Philosophy (in Computer Capabilities)
3. Visual Verification (in Computer Capabilities)
4. Context Cascade Principle (new section before Session Start)
5. Mode 6: Educational Parallel Track (in Collaboration Modes)
6. Diagnostic Breadcrumbs (in Key Principles)
7. Documentation as First-Class Output (new section)
8. Scientific Storytelling (new section)
9. Session Artifacts (in Session Continuity)
10. Reference Frame Paranoia (in Anti-Patterns)

**Plus update:**
- Quick Decision Guide (add Mode 6 check)
- Why This Works (add storyteller role)
- Version History (document v2.0 changes)

---

*"v1 taught us how to collaborate."*  
*"v2 teaches us what we learned FROM collaborating."*  
*"That's the difference between protocol and methodology!"* 🚀

---

**Ready to integrate into your project!** ✨
