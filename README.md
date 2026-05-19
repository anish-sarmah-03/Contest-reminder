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
4. Open `clist_fetcher.py` and replace:
   ```python
   USERNAME = 'your_clist_username'
   API_KEY  = 'your_clist_api_key'
   ```

---

### Step 5 — Set Up Google Calendar API

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or use an existing one)
3. Enable the **Google Calendar API**:
   - Navigate to **APIs & Services** → **Enable APIs and Services**
   - Search for "Google Calendar API" → Enable it
4. Create **OAuth 2.0 credentials**:
   - Go to **APIs & Services** → **Credentials** → **Create Credentials** → **OAuth Client ID**
   - Application type: **Desktop app**
   - Download the credentials file and save it as **`credentials.json`** in the project root

---

### Step 6 — Authenticate with Google Calendar

Run the script once to authenticate and generate `token.json`:

```bash
python main.py
```

A browser window will open asking you to log in to your Google account and grant Calendar access. After approving, `token.json` will be created automatically. The script will then sync contests to your calendar.

> ⚠️ **Important:** Never commit `credentials.json` or `token.json` to GitHub. They are already listed in `.gitignore`.

---

### Step 7 — Run Anytime

After the first-time setup, simply run:

```bash
python main.py
```

---

## ⚙️ Automating with GitHub Actions (Optional)

Want it to run automatically every day without opening your laptop? Use GitHub Actions:

1. Push your code to GitHub (without `credentials.json` or `token.json`)
2. Go to **Settings** → **Secrets and variables** → **Actions**
3. Add a secret named `GOOGLE_CALENDAR_TOKEN` with the contents of your `token.json`
4. The workflow in `.github/workflows/schedule.yml` will run daily at midnight UTC automatically

---

## 🔒 Security Notes

- `credentials.json` and `token.json` are excluded from version control via `.gitignore`
- When using GitHub Actions, the token is stored securely as an **encrypted GitHub Secret**
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

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

<p align="center">Made with ❤️ by <a href="https://github.com/anish-sarmah-03">anish-sarmah-03</a></p>
