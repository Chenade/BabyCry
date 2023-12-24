# from flask import Flask, render_template, request

# app = Flask(__name__, static_folder='static')

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/upload', methods=['POST'])
# def upload():
#     audio_file = request.files['audio']

#     return '音檔已接收'

# if __name__ == '__main__':
#     app.run(debug=True)

#-------------------------------------------------
from flask import Flask, render_template, request, jsonify , url_for
import random

# from DAI import main as DAI_main
import threading
# from google.cloud import storage

app = Flask(__name__, static_folder='static')

# def get_gcs_url(bucket_name, object_name):
#     storage_client = storage.Client()
#     bucket = storage_client.bucket(bucket_name)
#     blob = bucket.blob(object_name)
#     return blob.generate_signed_url(expiration=600)  # Adjust expiration as needed

@app.route('/')
def index():
    gcs_url = 'https://storage.googleapis.com/baby-cry-music-source/'
    return render_template('index.html', gcs_url=gcs_url)

# @app.route('/')
# def index():
#     print('url: ', url_for('static', filename='music/babyshark.mp3'))
#     return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    audio_file = request.files['audio']
    return jsonify({'message': 'Audio file received and processed'})

@app.route('/play_music', methods=['POST'])
def play_music():
    music_dir = 'static/music'
    selected_music = request.json['music_name']
    music_url = f'{music_dir}/{selected_music}'
    return jsonify({'message': music_url})

@app.route('/get_baby_state', methods=['GET']) # fake api for testing idf
def get_baby_state():
    return {'state': random.choice([True, False])}

@app.route('/get_baby_id', methods=['GET'])
def get_baby_id():
    return {"id": random.choice(["A007", "A008", "A009", "A100", "A101"])}

if __name__ == '__main__':
    # t = threading.Thread(target=DAI_main)
    # t.daemon = True
    # t.start()

    app.run(debug=True, port=8089)



