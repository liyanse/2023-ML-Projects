from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import os
import openai
import json
import numpy as np
from numpy.linalg import norm
import re
from time import time,sleep
from uuid import uuid4
import datetime
import pinecone

app = FastAPI()

from mm import (
    open_file,
    save_file,
    load_json,
    save_json,
    timestamp_to_datetime,
    gpt3_embedding,
    gpt3_completion,
    load_conversation,
)

class Message(BaseModel):
    input: str

@app.post('/generate-response', response_class=JSONResponse)
async def generate_response(message: Message):
    content = message.dict()
    a = content['input']
    convo_length = 30
    openai.api_key = open_file('key_openai.txt')
    pinecone.init(api_key=open_file('key_pinecone.txt'), environment='us-east-gcp')
    vdb = pinecone.Index("lalomvp")
    payload = list()
    timestamp = time()
    timestring = timestamp_to_datetime(timestamp)
    message = a
    vector = gpt3_embedding(message)
    unique_id = str(uuid4())
    metadata = {'speaker': 'USER', 'time': timestamp, 'message': message, 'timestring': timestring, 'uuid': unique_id}
    save_json('nexus/%s.json' % unique_id, metadata)
    payload.append((unique_id, vector))
    results = vdb.query(vector=vector, top_k=convo_length)
    conversation = load_conversation(results)
    prompt = open_file('prompt_response.txt').replace('<<CONVERSATION>>', conversation).replace('<<MESSAGE>>', a)
    output = gpt3_completion(prompt)
    timestamp = time()
    timestring = timestamp_to_datetime(timestamp)
    message = output
    vector = gpt3_embedding(message)
    unique_id = str(uuid4())
    metadata = {'speaker': 'LALO', 'time': timestamp, 'message': message, 'timestring': timestring, 'uuid': unique_id}
    save_json('nexus/%s.json' % unique_id, metadata)
    payload.append((unique_id, vector))
    vdb.upsert(payload)
    response = {'output': output}
    return response
