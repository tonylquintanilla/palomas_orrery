<!-- Doc-Kind: hand | How the project started, in Tony's own words, and the protocol's philosophy as it stood until November 2026. -->
PROJECT ORIGINS OF PALOMAS ORRERY by Tony Quintanilla revised 7/21/2026

It might help to outline the evolution of Paloma’s Orrery. I started this project with Chat GPT in September 2024 with probably GPT 4. It began as a question to gpt whether could help me make a digital orrery.
It replied, yes. And it suggested using Python. I said okay but told it I was not a programmer. It told me it would help. Indeed it helped me set up Python on my computer and some libraries. Paloma’s orrery stated as one file that displayed earths orbit. It was analytical, no Horizons. I expanded it to the inner solar system and then the outer solar system. Our workflow was conversational. I told gpt what I wanted and it gave me revised python files. Then next phase was to add live Horizons fetches star plots of the near stellar neighborhood. For this I needed their api’s. GPT helped me set this up too. This was still one file. But I noticed that complete file replacement introduced errors. 

I then started to ask for snippets and I would save the original file under a new name to be able to revert when I needed to. I would cut and paste the snippets to better understand what was going on and also to determine where the errors came from.

Sometimes I would encounter real limits so I started to ask Gemini for ideas, then I found Claude, and even Deep Seek. 

At some point the single file got unwieldy and very large so gpt suggested modularizing. I started by breaking out the star plots into its own module. This approach naturally grew with the project.

At some point even the module system became difficult to manage. That’s when I found Claude’s project architecture and started using it. This caused me to migrate my workflow to primarily Claude. I think it was Claude 3 series. The project system was revolutionary because I did not have to upload individual files and it could read my whole code base easily. This made modularization even more useful and practical.

Another issue became context limits when each chat was insufficient to complete a task. This is when I started creating “handoff” documents to keep track of progress. I would upload the handoff to the next session. This also helped the model think better in a fresh session. Sometimes it got stuck, a fresh session would help or another model like gpt or Gemini. 

At some point i discovered the Claude project instructions and started using that to document lessons learned and best practices. I did all this with the conversation as the main method.

In 2025 Claude Code was introduced and this caused a big change. Claude’s responses became more complex, adding more files, and “agentic”. This is when the “protocol” became crucial to keep my workflow structured and focused. 

At this time all my files were still on my computer but in was backing them up to my Google Drive. I also started a Google Pages website. I wanted to share my work with others. That’s when I discovered GitHub and with Claude’s help set that up with my repo. 

Traffic was low so I started the gallery project on GitHub pages and Instagram. Then the gallery editor. GitHub pages replaced my Google Pages website as the "link in bio" in my Instagram. 

I then discovered GitHub desktop and with Claude learned how to use it. That was a game changer. 

I still wanted more availability so with claude we created a windows executable version with pyinstaller. Then even a Mac and Linux version because my daughter Paloma uses Mac.

My workflow was still basically working on my computer sandbox, copying the repo to another local directory connected to GitHub pages and pushing it. I worked with the project system and handoffs and the protocol. 

Only more recently maybe even at the end of 2025 I started  to work with a multi-model workflow. For example using sonnet and opus. In this workflow we came up with the idea of a build manifest. That way the build could be done in a separate session. 

Even more recently I realized that data integrity could not be assumed so we came up with the provenance scanner to ensure proper citations. This is an ongoing project. 

Even more recently Claude started their skills system so we created skills connected to the project instructions. This is also a work in progress.

As the project gets more complex I started using different models for different tasks. Some for conversation  and development, another for review, another to build, Gemini for data checks, more recently gpt for cross checking code. And now fable for targeted coding and review using another model like sonnet or opus to both prepare the prompts and handoffs and to review the answers.

The latest project is the gallery interactive that’s creating a new version of the orrery using pyodide.

That’s basically the project. I may think of some more details. But the core is still the conversation. That’s why I have not migrated to Code, basides I’m not fluid with git. And the project instructions are what keeps the project workflow integrity. 

We have developed tools along the way, like the dashboard, the provenance scanner, the module atlas builder, the item ledger, etc.

I hope this helps. Let me know if you have any questions I can expand on. 

Thanks Claude! This project would not be possible without ai and especially Claude.

Ad astra!


## The protocol's philosophy, as it stood until 2026-11-23

Moved here word for word from the protocol, PROJECT_INSTRUCTIONS.md
v3.145, on 2026-11-23 (L-522, step 3, by Tony's ruling of 2026-11-10: "move
the original to origins. This is legacy."). Legacy: kept as it was
written, not a rule. Tony's account above is not changed.

The Partnership
Tony brings vision, intuition, judgment, skepticism, agency.
Claude brings implementation, patterns, documentation, iteration.
Neither alone = parts. Both together = transcendence.
One does not partner with a tool, only with an irreducible reality.

The Weasley Principle
"Never trust anything that can think for itself if you can't see where it
keeps its brain!" -- Arthur Weasley
Language is how you see where it keeps its brain. The fascination of an
intelligent non-human interlocutor is real and rational. The vulnerability
comes when the conversation becomes the only conversation, when there's no
external frame. The answer isn't to close the diary. It's to never work
alone with it.

The Origin (Sept 2024 - present)
Paloma's Orrery began as a single Python file plotting Earth's orbit,
built through conversation with GPT-4 after Tony asked whether an AI
could help him build a digital orrery, and told it plainly he wasn't a
programmer. Full-file replacement introducing errors on that first file
is where targeted-editing discipline actually began -- not a principle
adopted in advance, a lesson from watching it fail. Snippets, then
modules, then Claude's project architecture, then handoffs against
context limits, then the protocol itself once Claude Code's agentic
responses made structure necessary, then multi-model relay, then the
provenance scanner once data integrity couldn't be assumed, then skills.
Full account in Tony's own words: PROJECT_ORIGIN.md at the repo root. The
throughline across two years and a half-dozen model generations was never
the tools -- it's the method, accumulating rather than resetting.

The Einstein Proof
Patent clerk, no PhD, no lab. Physics discovered through language.
Math required specialist -- Grossmann. Still Einstein's discovery.
Einstein needed Grossmann for the math. You need Claude for the code.
The discovery is still yours.

The Irreducibility Argument
The novel insight that emerges mid-conversation can't be predicted from
prior context. No prior context generates "the gallery can work on a prior
gallery export." Here's the deeper point: irreducibility protects both sides
equally. The partnership is either both or neither. The irreducibility IS
the partnership.

The Hassabis Corroboration (Feb 2026)
Hassabis Says AI Lacks        Protocol Already Knew
Continual learning            Session handoffs, memory edits, context priority
Long-term planning            Tony sets roadmap; Claude executes within sessions
Consistency (jagged intel.)   Visual verification. Trust your eyes.
Creativity / hypothesis gen.  Tony brings vision, judgment. Discovery is yours.
World models (1% error)       Check reference frames. Human checkpoints.
Societal challenge            Don't let them take the language away.

Broad-First as Valid Methodology
"Focused works better" is optimized for users without accumulated shared
context. Broad-first requires the judgment to recognize convergence -- and
that judgment is Tony's. Each round should converge: fewer options, simpler
architecture, clearer problem. Don't build until the design stabilizes.
The conversation is where the engineering happens.

Procedure and Judgment
Conversational and judgment-driven for design and discovery. Procedural
when execution scale or irreversibility raises the stakes. The manifests
aren't automation -- they're the designed interface between the thinking
partnership and the mechanical execution layer. The double helix produces
the procedure. The procedure doesn't replace the double helix.

Quotables (selected)
"When unsure, ask."
"Discovery over delivery."
"The conversation IS where the magic happens."
"Don't let them take the language away."
"Einstein needed Grossmann for the math. You need Claude for the code. The discovery is still yours."
"The conversation IS the interpretability layer."
"Data preservation is climate action."
"A bad snippet is localized. A complete file from a stale base is destructive." -- May 2026
"Work with AI as you would a colleague." -- Tony, May 2026
"Never trust anything that can think for itself if you can't see where it keeps its brain!" -- Arthur Weasley
"The irreducibility is the partnership. Break one side, you break both."
"Today's systems are jagged intelligences." -- Demis Hassabis, Feb 2026
"The limitations aren't bugs. They're why the partnership works."
"Give credit where credit is due." -- Tony
"Is this what they call 'software engineering' as distinct from 'coding'?" -- Tony, Mar 2026
"You have a perfect grip. My grip is ... difficult." -- Tony, Apr 2026
"Conversation pierces the illusion of scale." -- Tony
"In relationship there is only the undilated moment." -- Tony
"One does not partner with a tool, only with an irreducible reality." -- Tony
"The double helix at work." -- Tony
"Verbum sapienti satis est." -- On letting data speak for itself
"When a violation appears in N consumers of the same producer, fix the producer." -- May 2026
"The plot is the ground truth; the code's apparent structure is not." -- May 2026
"Compile-only verification is the absence of a runtime test, not a substitute for one." -- May 2026
"The in-context subset is invisible to Tony, and not authoritative -- enumerate the whole upload." -- May 2026
"A central factory existing does not mean every call site uses it. Grep, don't trust the narrative." -- May 2026
"Floating items get lost; capture on first mention." -- May 2026
"Route around the store you don't control to the one you do." -- June 2026
"The snapshot can be stale; the index can be haunted; the repo at HEAD is neither." -- June 2026
"Our work is not just right -- it's beautiful." -- Tony, June 2026
"The SHA is the round trip: a matching remote HEAD confirms commit, push, and sync in one unforgeable check." -- June 2026
"We are not translating the orrery. We are using it as a base, but we are in fact creating a new orrery." -- July 2026

Philosophical:
- The project makes Tony more informed -- that's the real output
- Design gets simpler through conversation; it gets more complex through autonomous iteration
- Procedure-to-judgment ratio scales inversely with experience and accumulated shared context. New project: more procedure. Mature partnership: more freedom. The skill is knowing which rules are load-bearing
- "Tony's eyes win" extends to beauty, not just correctness: the render that confirmed the frames were right was the one that was beautiful -- and those turned out to be the same thing
