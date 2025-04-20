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


**### 1. Get the Project**

You can either **download** the project manually or **clone it** using Git:

#### 📦 Option A – Download as ZIP
1. Go to the repo: https://github.com/tahmid03/youtubesummarizer  
2. Click the green **Code** button and choose **Download ZIP**  
3. Extract the ZIP file  
4. Open a terminal inside the extracted folder

#### 🧪 Option B – Clone using Git 
git clone https://github.com/tahmid03/youtubesummarizer.git
cd youtubesummarizer

### 2. Create a Virtual Environment

This sets up an isolated Python environment for the project.

python -m venv venv

### 3. Activate the Virtual Environment

# Windows CMD
venv\Scripts\activate

# Windows PowerShell
.\venv\Scripts\Activate

# macOS/Linux
source venv/bin/activate

### 4. Install the Requirements

Install all the Python packages the project depends on.
pip install -r requirements.txt

### 5. Create Your .env File
🗂️ Copy the `.env.example` file and rename the copy to `.env`, then paste your OpenAI key inside:
OPENAI_API_KEY=sk-proj-your-real-api-key

🔑 You can get your API key at: https://platform.openai.com/account/api-keys

### 6. Run the App

Start the Flask development server.

python app.py
You should see:
 * Running on http://127.0.0.1:5000/

 * ### 7. Open the App in Your Browser

Go to:
http://127.0.0.1:5000/







## 🧰 Troubleshooting

**❌ ModuleNotFoundError: No module named 'flask'**

You probably forgot to install the required packages.

pip install -r requirements.txt
Or install Flask directly:
pip install flask

❌ ModuleNotFoundError: No module named 'dotenv'

You need to install the python-dotenv package for loading your .env file:
pip install python-dotenv

❌ ModuleNotFoundError: No module named 'openai'

Install the OpenAI package:
pip install openai

❌ Error: OPENAI_API_KEY is None or missing

Make sure you have created a .env file in your project root and that it contains your API key like this:

OPENAI_API_KEY=sk-proj-your-openai-key
Also double-check:

That the file is named .env (not .env.txt)

That you've restarted your terminal after creating the file

That you've activated your virtual environment

❌ Nothing happens when I run python app.py

Make sure your virtual environment is activated first:

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

## 👨‍💻 Author

Built with ❤️ by [Tahmid Rahman](https://github.com/tahmid03)  
Feel free to connect with me on [LinkedIn]([https://www.linkedin.com/in/tahmid-rahman2/])

