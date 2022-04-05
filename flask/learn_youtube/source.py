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

@app.route('/')
def index():
    liTags = ''
    for topic in topics:
        #liTags = liTags + '<li>' + topic['title'] + '</li>'
        liTags = liTags + f'<li>><a href="/read/{topic["id"]}/"> {topic["title"]} </a></li>'
    return f'''<!doctype html>
    <html>
        <body>
        <h1><a href="/">WEB</a></h1>
        <ol>
            {liTags}
        </ol>
        <h2>Welcom</h2>
        Hello, Web
    </body>
</html>
'''


@app.route('/create/')
def create():
    return 'Create'

@app.route('/read/<id>/')
def read(id):
    print(id)
    return 'Read '+id

app.run(debug=True)
