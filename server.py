"""
Flask web server for the Emotion Detection application.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """Renders the main application interface."""
    return render_template('index.html')

@app.route("/emotionDetector")
def detect_emotion():
    """
    Receives text from the HTML interface, runs it through the
    emotion detector, and formats the output for the user.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Pass text to the imported function
    response = emotion_detector(text_to_analyze)

    # Task 7: Handle blank input errors
    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    # Format output for the web interface
    output = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']} and "
        f"'sadness': {response['sadness']}. "
        f"The dominant emotion is {response['dominant_emotion']}."
    )
    return output

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

