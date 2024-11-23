from flask import Flask, request, jsonify
import yt_dlp
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def serve_index():
    with open('index.html', 'r') as f:
        return f.read()

@app.route('/download', methods=['POST'])
def download_video():
    try:
        data = request.json
        url = data.get('url')
        format_option = data.get('format')

        if not url:
            return jsonify({'error': 'No URL provided'}), 400

        # Set download options
        download_path = os.path.join(os.path.expanduser('~'), 'Downloads')
        ydl_opts = {
            'format': format_option,
            'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
        }

        # Download the video
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return jsonify({'message': 'Download successful'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
