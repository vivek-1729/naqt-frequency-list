import pickle, random, scraper
from flask import Flask, render_template, url_for, request
from random import randint
import webbrowser
scraper.getLists('https://www.naqt.com/you-gotta-know/american-plays.html')

with open('allVals','rb') as file:
    allVals = pickle.load(file)
with open('data','rb') as file:
    data = pickle.load(file)
dictionary = dict(zip(data, allVals))

app = Flask('testapp')
@app.route('/')
def index():
    labelVal = random.randint(0, len(dictionary)-1)
    label = data[labelVal]
    values = dictionary[label]
    selector = random.randint(0, len(values)-1)
    question = values[selector]
    return render_template('index.html', num=question, ans=label, time=5000, delay=1000)
browser = webbrowser.get('Safari')
browser.open('http://127.0.0.1:5000')
if __name__ == '__main__':
    app.run()
