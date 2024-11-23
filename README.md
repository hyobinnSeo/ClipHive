# ClipHive

ClipHive is a web application that enables users to download YouTube videos through a simple web interface. Built with Flask and yt-dlp, it provides an easy-to-use solution for downloading YouTube content in various formats.

## Features

- Clean web interface for video downloads
- Support for multiple video formats
- Downloads directly to user's Downloads folder
- Cross-origin resource sharing (CORS) enabled
- Error handling for failed downloads

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ClipHive.git
cd ClipHive
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Dependencies

- Flask (2.0.1)
- Flask-CORS (3.0.10)
- yt-dlp (2023.7.6)

## Usage

1. Start the server:
```bash
python server.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Enter the YouTube URL and select your preferred format
4. Click download to save the video to your Downloads folder

## Development

The application consists of:
- `server.py`: Flask backend server handling video downloads
- `index.html`: Frontend interface
- `requirements.txt`: Python dependencies

## Error Handling

The application includes error handling for:
- Invalid URLs
- Download failures
- Missing URL parameters
- Server-side exceptions

## License

[Add your chosen license here]
