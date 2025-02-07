import requests, json

default_response = {
    "anger": None, 
    "disgust": None, 
    "fear": None, 
    "joy": None, 
    "sadness": None, 
    "dominant_emotion": None
}

def emotion_detector(text_to_analyze):
    if not text_to_analyze or not len(text_to_analyze):
        return default_response
        
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    data = {
        "raw_document": {
            "text": text_to_analyze 
        }
    }

    res = requests.post(url, json=data, headers=headers)
    res_dict = json.loads(res.text)
    emotions = res_dict['emotionPredictions']
    if len(emotions):
        emotions = emotions[0]['emotion']
    else: 
        emotions = {}
    
    emotions['dominant_emotion'] = get_dominant_emotion(emotions)
    
    return emotions

def get_dominant_emotion(emotions):
    dominant_emotion = ''
    dominant_emotion_score = 0
    for emotion, score in emotions.items():
        if score > dominant_emotion_score:
            dominant_emotion = emotion
            dominant_emotion_score = score

    return dominant_emotion