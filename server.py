from flask import *
import os
import openai
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv(override=True)

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/ask', methods=['GET'])
def ask():
    args = request.args
    q = args.get('q')
    serial_code = args.get('sc')
    openai.api_key = os.getenv('OPENAI_API_KEY')

    if serial_code != os.getenv('SERIAL_CODE'):
        return jsonify({'error': 'Forbidden'}), 403
    
    response = openai.Completion.create(
        model = "text-davinci-003",
        prompt = q,
        temperature = 0,
        max_tokens = 1000
    )
    return response.choices[0].text.replace('\n', '')
