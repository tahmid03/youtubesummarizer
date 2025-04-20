from flask import Flask, request, jsonify, render_template
from youtube_transcript_api import YouTubeTranscriptApi
from openai import OpenAI
from yt_dlp import YoutubeDL
import logging

app = Flask(__name__)

from dotenv import load_dotenv
load_dotenv()


import os
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Set up logging for debugging
logging.basicConfig(level=logging.DEBUG)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/summarize', methods=['POST'])
def summarize_video():
    try:
        # Step 1: Get the YouTube video URL from the user
        data = request.get_json()
        video_url = data.get('video_url')
        if not video_url:
            return jsonify({"error": "Video URL is required"}), 400

        # Step 2: Fetch video details using yt-dlp
        ydl_opts = {
            'quiet': True,  # Suppress yt-dlp output
            'extract_flat': True,  # Extract metadata without downloading
        }
        with YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
            video_id = info_dict.get('id')
            video_title = info_dict.get('title', 'No title available')
            video_description = info_dict.get('description', 'No description available')

        # Step 3: Get transcript (captions)
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            full_text = " ".join([item['text'] for item in transcript])
        except Exception as e:
            return jsonify({"error": "Captions not available or failed to fetch."}), 500

        # Step 4: Summarize transcript using OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"Summarize the following video transcript in great detail:\n\n{full_text}"}
            ]
        )
        summary = response.choices[0].message.content

        # Step 5: Return the summary as JSON
        return jsonify({
            "title": video_title,
            "summary": summary,
            "description": video_description
        })

    except Exception as e:
        logging.error(f"Error: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)