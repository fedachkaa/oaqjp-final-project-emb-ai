"""
Emotion detection module
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    """
    base view
    """
    return render_template('index.html')

@app.route('/emotionDetector', methods=['GET'])
def emotion_detector_main():
    """
    function for emotion detector
    """
    text_to_analyze = request.args.get('textToAnalyze')

    emotions = emotion_detector(text_to_analyze)

    if set(emotions.values()) == set([None]):
        return 'Invalid text! Please try again!'

    dominant_emotion = emotions.pop('dominant_emotion')
    sadness = emotions.pop('sadness')

    emotion_text = 'For the given statement, the system response is '
    for emotion, score in emotions.items():
        emotion_text += emotion + ': ' + str(score) + ', '

    emotion_text += (
        'and sadness: ' + str(sadness) + '. ' 
         'The dominant emotion is ' + dominant_emotion + '.'
    )

    return emotion_text

if __name__ == "__main__":
    app.run(debug=True)
