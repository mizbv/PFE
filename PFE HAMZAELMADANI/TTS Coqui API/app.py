import os
import json
from flask import Flask, request, jsonify, send_from_directory
from text_to_speech import TextToSpeech

app = Flask(__name__)
# Set the COQUI_TOS_AGREED environment variable to avoid the prompt

os.environ["COQUI_TOS_AGREED"] = "1"

# Charger le dictionnaire d'abréviations et de corrections
#with open('dictionnaire.json', 'r', encoding='utf-8') as f:
    #corrections = json.load(f)
    
text_to_speech = TextToSpeech()

@app.route('/addtext', methods=['POST'])
def add_text():
    data = request.json
    if 'text' not in data:
        return jsonify({"error": "Text field is required"}), 400
    text = data['text']

    # Get the audio_file from the request data
    audio_file_choice = data.get('audio_file', 'audio3')  # Default audio file is audio3

    # Use a dictionary to map the audio_file_choice to the actual file path
    audio_files = {
        'audio1': 'static/input_audio/audio1.mp3',
        'audio2': 'static/input_audio/audio2.mp3',
        'audio3': 'static/input_audio/audio3.mp3',
        'audio4': 'static/input_audio/audio4.mp3'
    }
    
    # Get the actual file path based on the user's choice
    audio_file = audio_files.get(audio_file_choice, 'static/input_audio/audio3.mp3')

    # Replace abbreviations and incorrect words
    
    #for incorrect, correct in corrections.items():
     #   text = text.replace(incorrect, correct)

    language = data.get('language', 'fr')  # Default language is French
    output_file = "static/audio_generated/output.wav"
    text_to_speech.run_tts(text, audio_file, language, output_file)
    # Generate the audio_url
    audio_file_path = "static/audio_generated/output.wav"
    if not os.path.exists(audio_file_path):
        return jsonify({"error": "No audio file generated yet"}), 400
    audio_url = request.url_root + audio_file_path

    # Return the audio_url and the transformed text
    return jsonify({"audio_url": audio_url, "transformed_text": text}), 200


@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)

if __name__ == '__main__':
    debug_mode = os.environ.get('FLASK_DEBUG', 'False') == 'True'
    app.run(host='0.0.0.0', port=5000, debug=debug_mode)
