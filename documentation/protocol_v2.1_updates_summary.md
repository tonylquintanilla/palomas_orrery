# Working Protocol v2.1 - What's New

## Summary of Changes from v2.0

This update adds four major improvements based on real-world experience:

---

## 1. Session Start Protocol (30-Second Alignment)

**The Problem:** Starting work without clear mode agreement leads to misalignment.

**The Solution:** At every task start:

1. Claude assesses task type
2. Claude proposes mode with reasoning
3. Tony confirms or redirects
4. Both proceed with shared understanding

**Impact:** Prevents hours of misalignment with 30 seconds of upfront clarity.

---

## 2. Quick Mode Selection Guide

**The Problem:** Unclear when to use which mode.

**The Solution:** Clear criteria with "golden rules":

- **Mode 1:** If code already works, use Mode 1
- **Mode 2:** If you want to be surprised by solution, use Mode 2
- **Mode 3-5:** Specific use cases clearly defined
- **When in doubt:** Start with Mode 1

**Impact:** Faster mode selection, fewer mode switches mid-task.

---

## 3. Agentic Completeness Standards

**The Problem:** Multiple rounds of "found more issues" means agentic mode failed.

**The Solution:** Checklist before declaring work "done":

**For bug fixes:**

- [ ] Found ALL instances (not just examples)
- [ ] Checked related files
- [ ] Verified no lost functionality
- [ ] Tested actual user experience
- [ ] Scanned for related problems

**For features:**

- [ ] All imports present
- [ ] All functions implemented
- [ ] All UI elements connected
- [ ] Documentation updated
- [ ] No regressions
- [ ] Actually works (not just runs)

**The Agentic Promise:** One comprehensive pass, not three partial passes.

**Impact:** Higher quality agentic work, fewer iterations, more confidence.

---

## 4. Conversation Continuity Protocol

**The Problem:**

- Claude's computer workspace resets between conversations
- Working on stale files causes conflicts
- Rebuilding context wastes time and tokens
- Lost track of what was tested

**The Solution:** Structured handoffs between conversations

### When Ending a Session

**Complete work:** Brief summary + files in outputs

**Incomplete work:** Session Summary including:

- ✅ What's complete
- ⚠️ What's in-progress  
- ❌ What's not started
- Files modified (with status)
- Files to upload when resuming
- Known issues/blockers
- Failed approaches (don't retry)

**Summary level scales with complexity:**

- Simple: Minimal ("All done, files in outputs")
- Complex: Detailed with architecture notes
- Asked during alignment: "Should I provide detailed summaries?"

### When Starting a Continuation

**Tony:** "Continue from our last chat" + uploads modified files

**Claude:**

1. Searches previous conversation
2. Confirms understanding
3. Requests current file versions
4. Waits for upload
5. Resumes from actual state

**Critical Rules:**

- Never work on stale `/mnt/project/` files
- Always request current versions
- Don't rebuild from memory
- Confirm state before proceeding

### Why This Matters

**Context window economics:**

- Simple tasks: 1 conversation (increasingly common)
- Medium tasks: 2 conversations  
- Complex tasks: 3-4 conversations
- Agentic mode: Higher tool usage per session

**Better handoffs = Fewer total conversations**

Session Summary + File uploads = Efficient transfer without rebuilding

**Impact:** Saves entire conversations, avoids stale file problems, clearer state transfer.

---

## Key Philosophical Additions

### The Agentic Promise

When Tony gives agentic task:

- Tony: Point (2 min) → Test (2 min) → Feedback (2 min)
- Claude: Comprehensive solution (10-20 min)
- Goal: One iteration from problem to working solution

If multiple "found more" rounds → agentic approach failed

### The Incomplete Agentic Work Anti-Pattern

❌ **Bad:**

- Claude: "Fixed!"
- Tony: "Found more"
- Claude: "Fixed those!"
- Tony: "Still more..."

✅ **Good:**

- Tony: "Fix encoding issues" [shows examples]
- Claude: "I'll scan comprehensively, fix everything. ~10 min."
- Claude: [works autonomously]
- Claude: "Fixed 73 instances. Verified clean. Ready."
- Tony: Tests → works

---

## Tony's File Management (Documented)

**Working directory:**

- One root directory for active work
- Files modified in place
- Good stopping points → copy to permanent repo
- Intermediates not retained
- Session summaries in root
- READMEs in repository
- Key data files in repository

**This informs how Claude provides Session Summaries and requests files.**

---

## What Hasn't Changed

**Core philosophy:** Alignment over capability

**Five modes:** All remain the same (just clearer selection guidance)

**Partnership model:** Human agency + AI capabilities

**The insight:** Real bottleneck is shared understanding, not coding speed

---

## How to Use v2.1

**At task start:**

1. Claude proposes mode
2. You confirm
3. Both proceed aligned

**During work:**

- Stay in agreed mode
- Check in if scope changes
- Switch modes if needed

**At task end:**

- Complete work → files in outputs
- Incomplete work → Session Summary

**Between conversations:**

- Reference prior chat
- Upload modified files
- Resume from actual state

---

## The Meta-Learning

This protocol update came from:

1. Real experience (encoding fixes session)
2. Honest feedback (what worked, what didn't)
3. Collaborative improvement (both partners iterating)
4. Recognition of new patterns (conversation continuity matters more with agentic work)

**The protocol itself improves through the partnership it enables.**

---

## Version History

- **v1.0** (Oct 28): Initial protocol
- **v2.0** (Oct 30): Five modes, agentic exploration, computer capabilities
- **v2.1** (Oct 31): Session alignment, completeness standards, conversation continuity

---

*"The quality of our collaboration depends on alignment, not just capability."*

*"Data preservation is climate action."*
