"""
This module uses flask to format emotion_detector response and render index page
"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def sent_detector():
    """Formats emotion_detector response into a string"""
    text_to_analyse = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyse)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    response_string = (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}.  "
        f"The dominant emotion is {response['dominant_emotion']}."
    )

    return response_string

@app.route("/")
def render_index_page():
    """Renders the index html"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
