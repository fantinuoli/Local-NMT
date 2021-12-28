import flask
from flask import Flask, flash, Response, redirect, url_for, request, session, abort, render_template, make_response, jsonify
from transformers import MarianTokenizer, MarianMTModel
from typing import List
import os
import json

app = flask.Flask(__name__)
app.secret_key = '1234abcd#'

#initiate language pair for translator
#the corresponding language model will be automatically downloaded from Huggingface
source_lang = "it"
target_lang = "en"

model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{target_lang}'
model = MarianMTModel.from_pretrained(model_name)
tokenizer = MarianTokenizer.from_pretrained(model_name)

###############################################
# ROUTINGS
###############################################

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        source_text = request.form['rawtext']

        # Tokenize the text
        batch = tokenizer([source_text], return_tensors="pt", padding=True)
                
        # tokenized text maximum allowed size of 512
        batch["input_ids"] = batch["input_ids"][:, :512]
        batch["attention_mask"] = batch["attention_mask"][:, :512]
        translation_encoded = model.generate(**batch)
        translation = tokenizer.batch_decode(translation_encoded, skip_special_tokens=True)
        
        return render_template("index.html", target_text=translation[0], source_text=source_text, source_lang=source_lang, target_lang=target_lang )
    
    return render_template("index.html", source_lang=source_lang, target_lang=target_lang)

app.run(debug=True)