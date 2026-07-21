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