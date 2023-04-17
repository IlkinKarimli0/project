import numpy as np;import json
import os 
from fastapi import FastAPI
from pydantic import BaseModel

class_api_dict = {'1':'2','2':'11','3':'15',None:None}

app = FastAPI()

class TextData(BaseModel):
    text: str

@app.post("/api/v1/text")
async def process_text(text_data: TextData):
    text = text_data.text

    response_data = maino(text)
    
    return {"class_id": class_api_dict[response_data]}




curr_dir = os.path.dirname(os.path.abspath(__file__))
id_to_cls_path = os.path.join(curr_dir,"id_to_cls.txt")
bert_path = os.path.join(curr_dir,'bert_classify.model')


with open(id_to_cls_path, "r") as fp:
    # Load the dictionary from the file
    id_to_cls = json.load(fp)



########################BERT PART########################################

import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Load the fine-tuned model
model = BertForSequenceClassification.from_pretrained('bert-base-multilingual-uncased', num_labels=3)
model.load_state_dict(torch.load(bert_path, map_location=torch.device('cpu')))

# Initialize the tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-uncased')


def get_output_bert(input_text):

    # Tokenize the input text   
    input_ids = tokenizer.encode(input_text, add_special_tokens=True, return_tensors='pt')

    # Get the model prediction
    outputs = model(input_ids)
    logits = outputs[0]
    predicted_labels = torch.argmax(logits, dim=1)
    probs = torch.softmax(logits, dim=1)
    return predicted_labels.item(),probs


def maino(input_text):

    text = input_text

    output_bert,probs = get_output_bert(text)
    probs = probs[0, output_bert]
    output_bert += 1

    if probs > 0.8:
        return f'{output_bert}'
    else:
        return None

