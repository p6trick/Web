from flask import Flask
import random

app = Flask(__name__)
#<li><a href="/read/1/">html</a></li>
# <li><a href="/read/2/">css</a></li>
# <li><a href="/read/3/">javascript</a></li>

#li들을 모듈화해보자
topics = [
    {'id':1,'title':'html','body':'html is ...'},
   {'id':2,'title':'css','body':'css is ...'},
    {'id':3,'title':'javascript','body':'javascript is ...'}

]
#화면에 나타날 정보들은 dict에
# 일반적으로 데이터는 데이터베이스에 저장한다.
# 위의 리스트를 데이터베이스에서 읽어온다.

def template(contents,content):
        return f'''<!doctype html>
    <html>
        <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
            {contents}
        </ol>
        {content}
    </body>
</html>
'''

def getContents():
    liTags = ''
    for topic in topics:
        #liTags = liTags + '<li>' + topic['title'] + '</li>'
        liTags = liTags + f'<li><a href="/read/{topic["id"]}/"> {topic["title"]} </a></li>'
    return liTags

@app.route('/')
def index():
    
    
    return template(getContents(),'<h2>Welcome</h2>Hello, WEB')


@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<int:id>/') #자동으로 int로 변환
def read(id):
    title = ''
    body=''
    for topic in topics:
        if id == topic['id']:
            title = topic['title']
            body = topic['body']
            break
   
    return template(getContents(), f'<h2>{title}</h2>{body}')

app.run(debug=True)
