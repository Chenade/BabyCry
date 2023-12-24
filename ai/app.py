from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from test_model import model_test_single
import base64

app = Flask(__name__, static_folder='static')
CORS(app)

ALLOWED_EXTENSIONS = {'wav', 'mp3', 'ogg'}
model_path = os.path.join(os.path.dirname(__file__), 'densenet.pth')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload():
    try:
        if 'audio' not in request.files:
            return jsonify({'error': 'No audio file found in the request'})

        audio_data = request.files['audio'].read()

        model_path = os.path.join(os.path.dirname(__file__), 'densenet.pth')
        out = model_test_single(audio_data, model_path)


        # if out[0][0] > out[0][1]:
        #     print(0)
        # else:
        #     print(1)

        return jsonify({
            'message': 'Audio file received and processed',
            'result': out,
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)
