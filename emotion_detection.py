import requests
import json

def emotion_detector(text_to_analyze):
    # Task 7: Handle blank entries
    if not text_to_analyze or text_to_analyze.isspace():
        return {
            'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None,
            'dominant_emotion': None
        }

    # Task 2: Watson NLP API integration
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=myobj, headers=headers)
    
    # Task 7: Handle 400 Bad Request
    if response.status_code == 400:
        return {
            'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None,
            'dominant_emotion': None
        }
    
    # Task 3: Formatting the output
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    # Find the dominant emotion
    dominant_emotion = max(emotions, key=emotions.get)
    
    return {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness'],
        'dominant_emotion': dominant_emotion
    }

