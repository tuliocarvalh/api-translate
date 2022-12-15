# coding: utf-8
from cgitb import text
from googletrans import Translator
import json
import traceback
from flask import Blueprint, jsonify, make_response, request

bp_trans = Blueprint('api', __name__, url_prefix='/traducao')


def trans():
    urls = ["translate.google.com", "translate.google.com.ar", "translate.google.com.br",]
    user = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
    return Translator(service_urls=urls, user_agent=user, raise_exception=False, timeout=None)


def trans_pt(self) :
    frase = str(self)
    traducao = trans().translate(str(frase), dest='en').text
    return traducao

def trans_(self) :
    frase = str(self)
    traducao = trans().translate(str(frase), dest='pt').text
    return traducao


@bp_trans.route('/')

def traducao():
    frase = request.args.get('tr')
    traduction = trans_(frase)
    return traduction
