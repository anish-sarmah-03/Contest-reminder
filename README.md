# 🏆 Contest Reminder — Automated CP Contest Scheduler

[![GitHub Actions](https://img.shields.io/badge/Automated%20with-GitHub%20Actions-2088FF?logo=github-actions&logoColor=white)](https://github.com/features/actions)
[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://python.org)
[![Google Calendar](https://img.shields.io/badge/Google%20Calendar-API-4285F4?logo=google-calendar&logoColor=white)](https://developers.google.com/calendar)

> Never miss a Codeforces, CodeChef, or LeetCode contest again — fully automated!

---

## 📌 About the Project

**Contest Reminder** is a Python-based automation agent that fetches upcoming competitive programming contests from [Clist.by](https://clist.by) and automatically adds them to your **Google Calendar** with a **30-minute reminder** before each contest starts.

The script runs **every day at midnight UTC** via **GitHub Actions** — completely hands-free, no local machine required.

### ✨ Key Features
- 🔄 **Daily auto-sync** — Fetches contests for the next 14 days every midnight
- 📅 **Google Calendar integration** — Events added directly to your primary calendar
- ⏰ **30-minute pop-up reminders** — Never miss a contest start
- 🚫 **Duplicate prevention** — Skips events already added to your calendar
- 🎯 **Platforms supported:** Codeforces, CodeChef, LeetCode
- 🔒 **Secure by design** — All credentials stored as environment variables, never hardcoded

---

## 🗂️ Project Structure

```
contest-reminder/
├── .github/
│   └── workflows/
│       └── schedule.yml      # GitHub Actions workflow (runs daily)
├── main.py                   # Entry point — orchestrates fetch + sync
├── clist_fetcher.py          # Fetches contests from Clist.by API
├── calendar_manager.py       # Handles Google Calendar authentication & event creation
├── requirements.txt          # Python dependencies
└── .gitignore                # Excludes secrets (token.json, credentials.json)
```

---

## 🚀 Running Locally (Step-by-Step)

Follow these steps to run the project on your own machine.

### Prerequisites
- Python 3.10 or higher
- A Google account
- A [Clist.by](https://clist.by) account (free)

---

### Step 1 — Clone the Repository

```bash
git clone https://github.com/anish-sarmah-03/Contest-reminder.git
cd Contest-reminder
```

---

### Step 2 — Create a Virtual Environment

```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On Mac/Linux
source venv/bin/activate
```

---

### Step 3 — Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4 — Get Your Clist.by API Key

1. Sign up at [clist.by](https://clist.by)
2. Go to your profile → **API** section
3. Copy your **username** and **API key**

---

### Step 5 — Set Environment Variables

The project reads credentials from environment variables. Set them before running:

**On Windows (PowerShell):**
```powershell
$env:CLIST_USERNAME = "your_clist_username"
$env:CLIST_API_KEY  = "your_clist_api_key"
```

**On Mac/Linux:**
```bash
export CLIST_USERNAME="your_clist_username"
export CLIST_API_KEY="your_clist_api_key"
```

> 💡 These variables only last for the current terminal session. You can also add them permanently to your shell profile (`.bashrc`, `.zshrc`) or Windows system environment settings.

---

### Step 6 — Set Up Google Calendar API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use an existing one)
3. Enable the **Google Calendar API**:
   - Navigate to **APIs & Services** → **Enable APIs and Services**
   - Search for "Google Calendar API" → Enable it
4. **Configure OAuth Consent Screen**:
   - Go to **APIs & Services** → **OAuth consent screen**
   - Choose **External** and click Create
   - Fill in the required app details (name, email)
   - Go to the **Audience** tab in the OAuth consent screen and click **Publish App** to move the app from "Testing" to "In production". This allows anyone  to use the app without an "Access blocked" error. (Note: You may see an "Unverified app" warning, which you can bypass by clicking "Advanced" → "Go to App").
5. Create **OAuth 2.0 credentials**:
   - Go to **APIs & Services** → **Credentials** → **Create Credentials** → **OAuth Client ID**
   - Application type: **Desktop app**
   - Download the credentials file and save it as **`credentials.json`** in the project root

---

### Step 7 — Authenticate with Google Calendar

Run the script once to authenticate and generate `token.json`:

```bash
python main.py
```

A browser window will open asking you to log in to your Google account and grant Calendar access. After approving, `token.json` will be created automatically. The script will then sync upcoming contests to your calendar.

> ⚠️ **Important:** Never commit `credentials.json` or `token.json` to GitHub. They are already listed in `.gitignore`.

---

### Step 8 — Run Anytime

After the first-time setup, simply run:

```bash
python main.py
```

---

## ⚙️ Automating with GitHub Actions

This repo is pre-configured to run automatically every day at **midnight UTC** via GitHub Actions — no local machine needed.

To set it up on your own fork:

1. Fork this repository
2. Go to your fork → **Settings** → **Secrets and variables** → **Actions**
3. Add the following **3 secrets**:

| Secret Name | How to get it |
|---|---|
| `CLIST_USERNAME` | Your Clist.by username |
| `CLIST_API_KEY` | Your Clist.by API key (from your profile page) |
| `GOOGLE_CALENDAR_TOKEN` | Full contents of `token.json` generated in Step 7 above |

4. The workflow in `.github/workflows/schedule.yml` will now run automatically every day ✅

You can also trigger it manually anytime:
- Go to **Actions** tab → **Daily Contest Sync** → **Run workflow**

---

## 🔒 Security Notes

- `credentials.json` and `token.json` are excluded from version control via `.gitignore`
- Clist API credentials are read from **environment variables**, never hardcoded
- When using GitHub Actions, all secrets are stored as **encrypted GitHub Secrets**
- Never share your API keys or OAuth tokens publicly

---

## 🛠️ Built With

| Tool | Purpose |
|------|---------|
| [Python 3.10+](https://python.org) | Core scripting language |
| [Clist.by API](https://clist.by/api/v4/) | Contest data source |
| [Google Calendar API](https://developers.google.com/calendar) | Calendar event management |
| [GitHub Actions](https://github.com/features/actions) | Daily automation |

---
