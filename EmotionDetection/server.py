from flask import Flask
from flask import render_template
from flask import request

from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Analyze text emotions.
    """

    text_to_analyze = request.args.get("textToAnalyze")

    response = emotion_detector(text_to_analyze)

    if response is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}, "
        f"'sadness': {response['sadness']}. "
        "The dominant emotion is "
        f"<b>{response['dominant_emotion']}</b>."
    )


@app.route("/")
def render_index_page():
    """
    Render main page.
    """

    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
