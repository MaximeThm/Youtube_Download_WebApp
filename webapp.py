from flask import Flask, render_template, request
from app.download import download_audio

app = Flask(__name__)

app.static_folder = 'static'

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/download", methods=['POST'])
def download():
    video1_url = request.form['firstvideo']
    download_audio(video1_url)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
