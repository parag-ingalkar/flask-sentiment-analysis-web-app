import json
import requests

def sentiment_analyzer(text_to_analyze):
    '''The function gives the label and score of the input text'''
    url= 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    headers= {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    input_json= { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json=input_json, headers=headers, timeout=30)
    blank_input = False

    formatted_response = json.loads(response.text)
    if text_to_analyze == "":
        blank_input = True 
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:
        label = None
        score = None

    return {'label' : label, 'score' : score, 'blank_input':blank_input}
