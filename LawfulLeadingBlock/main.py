from flask import Flask, render_template
import speech_recognition as sr
from summarization import run_summarization
from keywords import get_keyword 
from transcript import trans
# from text_summarizer.text_summarizer import summarizer

app = Flask('app')

trans = trans

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/transcript')
def transcript():
  return render_template('transcript.html', t=trans)
    
@app.route('/summary')
def summary():
  summar = run_summarization(trans)
  print(summar)
  return render_template('summary.html', summary=summar)

@app.route('/translation')
def tranlsation():
  pass

@app.route('/keywords')
def kewords():
  keys = get_keyword()
  return render_template('keyword.html', key=keys)

if __name__=='__main__':
  app.run(host='0.0.0.0', port=8080)



