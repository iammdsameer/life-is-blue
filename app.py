import youtube_dl
import os
from flask import Flask, request, send_file
app = Flask(__name__)

@app.route('/')
def root():
  return 'API is working!'

# Test
@app.route('/ls')
def list():
  return os.listdir()

@app.route('/api/<url>')
def home(url):
  title = request.args.get('title')
  filename = f'{title}.mp3'
  ydl_opts = {
      'format': 'bestaudio/best',
      'postprocessors': [{
          'key': 'FFmpegExtractAudio',
          'preferredcodec': 'mp3',
          'preferredquality': '192',
      }],
      'outtmpl': filename
  }

  with youtube_dl.YoutubeDL(ydl_opts) as ydl:
      # info = ydl.extract_info(url, download=False)
      ydl.download([f'https://youtu.be/{url}'])
  return send_file(filename)
