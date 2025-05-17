import requests
import json

def sentiment_analyzer(text_to_analyze):
    URL= 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers= {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    input_json= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(URL, json=input_json, headers=headers)

    formatted_response = json.loads(response.text)
    label = formatted_response['documentSentiment']['label']
    score = formatted_response['documentSentiment']['score']

    return {'label' : label, 'score' : score}
