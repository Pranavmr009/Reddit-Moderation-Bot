# 🛠️ NEET-Subreddit Moderation Bot

A Python bot that uses PRAW and Google Gemini (2.0 Flash) API to automatically moderate the **r/NEET** subreddit by filtering out posts about the Indian NEET exam and notifying moderators for review.

---

## 🚀 Features

- **Live post monitoring** using `subreddit.stream.submissions()`
- **AI-based classification** via Gemini API to distinguish NEET (Not in Employment, Education, or Training) posts
- **Selective moderation**, flagging only off-topic submissions with `.report()` to notify mods
- **Mod log stream listener** that sends modmail notifications when posts are removed
- **Lightweight and cost-efficient**: ~30 posts/day remain within Gemini’s free tier

---

## 🧩 Components

- `main.py`:  
  - Loads environment variables  
  - Connects to Reddit with PRAW  
  - Streams live posts  
  - Calls `ai_backend.Moderate_Sub(title, body)` to classify content  
  - Reports non-relevant posts to the moderator queue  
  - Sends modmail notifications on removals

- `ai_backend.py`:  
  - Wraps Gemini API calls  
  - Implements prompt engineering to check if a post is on-topic for r/NEET

---

## ⚙️ Setup & Usage

1. **Clone this repo**
   ```bash
   git clone https://github.com/youruser/neet-moderation-bot.git
   cd neet-moderation-bot

2. **Install dependencies**
    ```bash
    pip install praw python-dotenv google-generativeai

3. **Create .env file and add necessary environment variables**
    ```bash
    CLIENT_ID=<Reddit client id>
    CLIENT_SECRET=<Reddit client secret>
    USERNAME=<bot username>
    PASSWORD=<bot password>
    USER_AGENT="script:NEETbot:1.0 (by u/YourName)"
    GEMINI_API_KEY=<Your Gemini API key>
    SUBREDDIT_NAME=<The subreddit you want to run this bot on>

4. **Invite bot as moderator**
     *On Reddit: Mod Tools → Moderators → Invite Mod

     *Grant “posts & comments” permission

     *Accept the invite on the bot account via PRAW or manually

5. **Run the bot**
    ```bash
    python3 main.py
