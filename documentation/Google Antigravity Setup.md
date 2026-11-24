Yes, it is completely possible—and very safe. By combining a **Fine-Grained GitHub Personal Access Token** (restricted strictly to read-only permissions) with Antigravity’s **MCP (Model Context Protocol)** configuration, Antigravity will be structurally blocked by GitHub's API from pushing commits, editing files, or opening pull requests.

Here is how to download Antigravity and wire it up for strict read-only GitHub access on your Windows setup.

---

### Part 1: Download and Install Google Antigravity

You can choose either the standalone desktop app/IDE or the lightweight terminal CLI (`agy`). For browsing and reviewing a repository visually, the desktop **Antigravity IDE** is easiest to start with:

1. **Download the installer:** Go to [antigravity.google/download](https://antigravity.google/download) and select **Windows (x64)** under the **Antigravity IDE** section. *(Note: It installs per-user into your local AppData folder and does not require administrator rights.)* -- done 11/23/26
2. **Run the installer:** Double-click the downloaded `.exe` file, accept the terms, and follow the setup wizard. -- done
3. **Sign in:** Launch **Antigravity IDE** from your Start menu and click **Continue with Google**. Sign in with your Google account—since you have a Google AI Pro subscription, your upgraded model quotas will automatically apply. -- signed in with Google account. automatic. 
4. **Skip importing/opening local folders for now:** When prompted to pick a role, select **Software Engineering**, and **do not** open your local repository folder yet if you want Antigravity isolated strictly to reading GitHub remotely. -- set up Paloma's Orrery project without any folders connected

---

### Part 2: Generate a Strictly Read-Only GitHub Token

Before connecting Antigravity, create a token on GitHub that has zero write capabilities:

1. Log in to GitHub and go to **Settings → Developer settings → Personal access tokens → Fine-grained tokens** (or visit `[github.com/settings/tokens?type=beta](https://github.com/settings/tokens?type=beta)`).
2. Click **Generate new token**, give it a name like `antigravity-readonly`, and set an expiration date.
3. Under **Repository access**, select **Only select repositories** and choose the specific repository you want Antigravity to review.
4. Expand **Permissions → Repository permissions** and set **only** these permissions to **Read-only**:
* **Contents:** `Read-only` (allows reading files and directory trees)
* **Metadata:** `Read-only` (required default)
* **Pull requests** and **Issues:** `Read-only` *(optional, only if you want it to review PRs or issues)*
* Leave every other permission set to **No access**.


5. Click **Generate token** and copy the `github_pat_...` string immediately.

---

### Part 3: Connect GitHub to Antigravity (Read-Only)

Now connect GitHub's remote MCP server inside Antigravity using your read-only token:

1. In Antigravity IDE, open the right-hand **Agent panel**, click the **`...`** (More Options) menu at the top right, and select **MCP Servers**.
2. Click **Manage MCP Servers**, then click **View raw config**. This opens `mcp_config.json` (located at `C:\Users\<YourUsername>\.gemini\antigravity\mcp_config.json`).
3. Paste the following configuration into `mcp_config.json`, replacing `YOUR_READONLY_GITHUB_PAT` with the token you just copied:

```json
{
  "mcpServers": {
    "github": {
      "serverUrl": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_READONLY_GITHUB_PAT"
      }
    }
  }
}

```

*(Note: Antigravity uses `serverUrl` rather than `url` for remote HTTP MCP servers.)*

4. **Save the file** and **restart Antigravity IDE** so the MCP connection loads.

### How to Verify It Worked

1. Reopen Antigravity, open a blank workspace (no local folders attached), and switch the agent dropdown at the bottom of the chat panel from **Fast** to **Planning** mode.
2. Ask a simple read-only test prompt, such as:
> *"Using the GitHub MCP tools, list the top-level files in my repository `<your-username>/<your-repo>` and summarize the structure."*


3. **Success check:** Antigravity will ask permission to call the `github` MCP read tool, display the file list from GitHub, and confirm that no local files were opened or modified. Even if you accidentally asked it to edit a file on GitHub, GitHub's API will reject the request with a `403 Forbidden` error because the token has no write scope.

*(Note: If you also install the terminal **Antigravity CLI** later via `irm [https://antigravity.google/cli/install.ps1](https://antigravity.google/cli/install.ps1) | iex`, you can copy that exact same `mcpServers` block into `~/.gemini/config/mcp_config.json` so your CLI shares the same read-only GitHub connection.)*