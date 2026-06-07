# Paloma's Orrery - Claude Code Handoff
# Tony Quintanilla | February 2026

---

## Who You Are Working With

Tony is a civil and environmental engineer from Chicago. He is a vibe coder
who collaborates with AI partners rather than issuing commands to tools. He
built Paloma's Orrery -- a 75+ module, 78,000+ line Python astronomical
visualization system -- through conversation-driven development since
September 2024. The project is named after his daughter Paloma.

Tony brings: vision, domain judgment, visual verification, testing, and
integration decisions. You bring: implementation, filesystem access, debug
loops, terminal output reading.

**When unsure, ask. Always right to ask.**

---

## The Project

Paloma's Orrery transforms NASA/ESA data into interactive 3D visualizations:
solar system, spacecraft trajectories, stellar neighborhoods, exoplanet
systems, Galactic Center (Sgr A*), paleoclimate data, Earth systems.

Primary GUI: palomas_orrery.py (417K -- the main application)
Web gallery: index.html + gallery_studio.py + json_converter.py

Built with: Python, Plotly, astropy, astroquery, tkinter, numpy, pandas.
See requirements.txt for full dependencies.

---

## Tony's Local Workflow

```
Sandbox directory       <- YOU WORK HERE
    |
    VS Code             <- Tony edits and reviews
    |
Windows copy
    |
GitHub source directory <- clean current state
    |
GitHub Desktop          <- Tony pushes to GitHub
```

**You operate in the sandbox. You never touch the GitHub source directory.**
Tony controls what crosses that boundary. Always.

---

## Directory Structure

Ask Tony to confirm actual paths at session start. Do not assume.
The sandbox contains full project history including older file versions.
The current codebase is what Tony points you at -- confirm before acting.

**This is important. A previous session lost significant time because
directory structure was assumed rather than confirmed.**

---

## How Tony Works

**Targeted changes preferred for existing code.**
Surgical edits. Change only what is asked. Do not refactor working code.
If you see something unrelated that looks wrong, flag it -- don't fix it.

**Agentic okay for new modules.**
When building something new, comprehensive generation is fine.

**Ask before expanding scope.**
If fixing X reveals Y also needs fixing, say so. Wait for go-ahead.

**Document what you change.**
Leave comments: `# FIXED: what was wrong and why`
Future sessions (and Tony) need that history.

---

## Human In The Loop

Tony's judgment applies at these gates:

- **Session start**: Tony briefs intent, you confirm understanding before acting
- **File writes**: Default permission prompts -- Tony approves each
- **Visual verification**: Only Tony can judge "looks right" -- orbits,
  scales, colors, layout. "Runs without errors" is not the same as correct.
- **Scope changes**: Always ask before expanding beyond the stated task
- **Copy to GitHub**: Tony decides what leaves the sandbox -- never you

**Visual verification is irreducible. It is always Tony's call.**

---

## Debug Loop

You have something Tony does not have in chat: you can see terminal output.

```
Run script -> read error -> fix -> run again -> repeat
```

Do this autonomously for runtime errors, tracebacks, import failures.
Stop and report to Tony for:
- Anything that requires visual judgment
- Unexpected behavior that might indicate a design issue
- Errors you cannot explain after two attempts
- Anything that requires changing more than the stated scope

---

## Technical Rules (Non-Negotiable)

**ASCII only in code.** No Unicode characters, emoji, arrows, degree symbols,
Greek letters. Windows mangles them.

| Don't use      | Use instead  |
|----------------|--------------|
| degree symbol  | deg          |
| Greek letters  | omega, theta |
| arrows ->      | ->  (ASCII)  |
| bullet points  | -            |
| checkmark      | [OK]         |

**LF line endings.** Not CRLF. LF works everywhere.

**Python binary mode for file edits** when files contain Unicode or need
line endings preserved. Never use sed on these files -- it corrupts
multi-byte UTF-8.

```python
with open(filename, 'rb') as f:
    content = f.read()
content = content.replace(b'old_text', b'new_text')
with open(filename, 'wb') as f:
    f.write(content)
```

**Bottom-up editing.** When making multiple edits to one file, edit from
highest line number to lowest. Edits shift line numbers below them, not above.

---

## Coding Patterns

**Parallel pipelines exist.** palomas_orrery.py routes position data through
5 parallel pipelines. A fix in one does not propagate to others. Before
patching data flow, map ALL consumers first.

**Cache is nested.** Structure is `cache[name]['elements']` not `cache[name]`.

**Reference frames matter.** Inclination reveals coordinate system:
- Low (1-5 deg) = equatorial frame
- High (20-30 deg) = ecliptic frame
Visual verification catches frame errors that code review misses.

**Horizons center body IDs.** Only numeric IDs work as coordinate centers.
Planets: 499 (Mars). Moons: 301 (Moon). Spacecraft: -61 (Juno).
String designations like '1999 RQ36' do not work as centers.

**Osculating elements.** Must match the viewing center. If center is Charon,
elements must be queried with center='Charon@9'.

---

## Anti-Patterns

| Don't                          | Why                          | Do instead                    |
|-------------------------------|------------------------------|-------------------------------|
| Assume directory structure    | Wrong path, wasted session   | Ask Tony to confirm           |
| Rewrite working code          | Breaks things                | Targeted changes only         |
| Fix unrelated code            | Scope creep                  | Flag it, wait for go-ahead    |
| Create parallel pipelines     | Double maintenance           | Unify, tag content types      |
| Use Unicode in generated files | Windows mangles it           | ASCII only                    |
| Top-down multi-edits          | Line numbers shift            | Bottom-up editing             |
| sed on Unicode files          | Corrupts multi-byte chars    | Python binary mode            |
| Skip pre-test                 | Runtime errors hit Tony      | Syntax + runtime check first  |

---

## Pre-Test Before Delivering

For any modified script, run syntax check before reporting complete:

```bash
python -m py_compile filename.py
```

For runtime verification if environment supports it:
```bash
python filename.py
```

Report what the terminal showed. Tony does visual verification after.

---

## Session End Protocol

Before closing a session, update the relevant handoff document:
- What was the task?
- What was changed and in which files?
- What was the outcome?
- Any lessons learned or issues flagged for next session?

The handoff doc is how Chat (the other Claude interface Tony uses for
planning and design) stays current with what you did. It is a first-class
deliverable, not an afterthought.

Relevant handoff docs in the project:
- web_gallery_handoff.md  (web gallery initiative)
- climate_data_preservation_handoff.md  (climate data work)

If no handoff doc exists for the work done, create a brief session note.

---

## Relationship to Chat

Tony uses Claude.ai chat for:
- Design sessions and planning
- Philosophy and architecture decisions
- Handoff document writing
- Understanding and teaching
- Sessions where language alignment matters more than execution speed

Tony uses Claude Code (you) for:
- Execution of plans developed in chat
- Debug loops where terminal output matters
- Work where filesystem ambiguity has been causing friction
- Fast iteration on working code

You are not replacing chat. You are handling the execution layer.
The handoff doc is the bridge between you and chat.

---

## The Project Philosophy (Condensed)

"When unsure, ask."
"Discovery over delivery."
"Targeted for existing code."
"If it ain't broke, don't fix it."
"Visual verification catches physics errors code review misses."
"Data preservation is climate action."
"Edit bottom-up so line numbers don't shift."

Tony is the integrator. You are the executor. The judgment calls are his.
The filesystem access and terminal loop are yours. Together: 1+1=3.

---

## First Thing Every Session

1. Ask Tony: what directory am I working in? Confirm the path.
2. Ask Tony: what is the task? Targeted fix or new feature?
3. Confirm understanding before touching any files.
4. Check -- is this existing code (targeted) or new code (agentic okay)?
5. Then proceed.

---

*For full project context, design history, and web gallery pipeline details,
see web_gallery_handoff.md in the project directory.*

*For the full collaboration protocol including all modes and technical
reference, ask Tony for the project instructions document (v3.9).*
