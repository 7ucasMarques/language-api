from flask import Flask, request, jsonify
from langdetect import detect, DetectorFactory

DetectorFactory.seed = 0  # To ensure consistent results
app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect_language():
    # Get the text from the request
    data = request.get_json()
    text = data.get('text', '')

    if not text:
        return jsonify({'error': 'No text provided'}), 400

    try:
        language = detect(text)
        return jsonify({'language': language}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
