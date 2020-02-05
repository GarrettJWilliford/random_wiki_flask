from flask import Flask
from flask import render_template
from flask import request
import random
import requests
from bs4 import BeautifulSoup
from bs4 import Tag
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')


@app.route('/search_results', methods=['POST'])
def sr_index():
    data = pickle.load(open('/Users/garrettwilliford/wiki_articles.p', 'rb'))
    result = requests.get('https://en.wikipedia.org/wiki/' + random.choice(data))
    soup = BeautifulSoup(result.content, 'html.parser')
    return result.content

