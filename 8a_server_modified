"""
Server module for the Emotion Detection application.
Provides routes to render the interface and process emotion detection requests.
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Route handler for processing emotion detection requests.
    Retrieves input text, sends it to the detector backend,
    and returns a formatted string response.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    res = emotion_detector(text_to_analyze)

    if res.get("dominant_emotion") is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {res['anger']}, 'disgust': {res['disgust']}, "
        f"'fear': {res['fear']}, 'joy': {res['joy']} and "
        f"'sadness': {res['sadness']}. "
        f"The dominant emotion is {res['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Route handler to render the default homepage index template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
