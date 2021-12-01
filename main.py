from fastapi import Request, FastAPI, status
from pydantic import BaseModel
from automation import helper
from textblob import TextBlob
import json
import os 

os.environ['PATH_TO_DRIVER'] = './automation/chromedriver_win32/chromedriver.exe'

app = FastAPI()

@app.get('/test', status_code=status.HTTP_200_OK)
def test():
    return { 'msg': 'up and running' }

@app.post('/translate/')
async def translate(request: Request):
    req = await request.json()
    print(req)
    try:
        if type(req.get('text')) == str:
            return { 
                'original_text': req.get('text'),
                'translated_text': helper.translate(req.get('text')) 
            }
        else:
            return {
                'msg': 'text must be a string'
            }
    except Exception as e:
        msg = 'missing text parameter' if bool(e) else e
        return {
            'msg': msg
        }

@app.post('/spellcheck/')
async def spellcheck(request: Request):
    req = await request.json()
    txtBlb = TextBlob(req.get('text'))
    try:
        if type(req.get('text')) == str:
            return { 
                'original_text': req.get('text'),
                'correct_text': str(txtBlb.correct()) 
            }
        else:
            return {
                'msg': 'text must be a string'
            }
    except Exception as e:
        msg = 'missing text parameter' if bool(e) else e
        return {
            'msg': msg
        }