# 🎥 YouTube Video Summarizer 🤖

This is a Flask web app that takes a YouTube video URL, fetches the video transcript, and summarizes it using OpenAI's GPT-3.5 Turbo model.

It includes a modern frontend using TailwindCSS and displays the video thumbnail, a YouTube-style loader, and a clean interface—perfect for showcasing AI + web development skills.

---

## 🚀 Features

- Paste any YouTube link with captions
- Automatically pulls the transcript (if available)
- Sends it to OpenAI's ChatGPT and returns a detailed summary
- Displays the video thumbnail and summary on the page
- Clean, responsive frontend using TailwindCSS

---


## 🛠 How to Run Locally

### 1. Get the Project

You can either **download** the project manually or **clone it** using Git:

#### 📦 Option A – Download as ZIP

1. Go to the repo: https://github.com/tahmid03/youtubesummarizer
2. Click the green **Code** button and choose **Download ZIP**
3. Extract the ZIP file
4. Open a terminal inside the extracted folder

#### 🧪 Option B – Clone using Git 

```bash
git clone https://github.com/tahmid03/youtubesummarizer.git
cd youtubesummarizer

**### 2. Create a Virtual Environment**

This sets up an isolated Python environment for the project.

```bash
python -m venv venv

**### 3. Activate the Virtual Environment**

This activates your local Python environment so installed packages stay project-specific.

```bash
# Windows CMD
venv\Scripts\activate

# Windows PowerShell
.\venv\Scripts\Activate

# macOS/Linux
source venv/bin/activate

**### 4. Install the Requirements**

Install all the Python packages the project depends on.

```bash
pip install -r requirements.txt
