# flask

## pyenv

- 파이썬 버전관리 셋팅
- `pip install flask`

## intro
### app.py 작성
- [플라스크 공식문서](http://flask.pocoo.org/)
- 제일 첫 페이지에 나오는 문장들을 복사 합시다.
```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"
```

### run

- 공식문서 실행 명령
```bash
$ FLASK_APP=hello.py flask run
```
- c9에서 명령
```bash
$ flask run --host 0.0.0.0 --port 8080
```
 - c9 서버에서는 flask run 명령어에 host와 port를 직접 설정해줘야한다.
 - 로컬에서 구동시에는 flask run 만 해도 되며, 접속 url은 http://localhost:5000이 기본이다.
 - flask run 명령어를 실행할 때, 파일명이 app.rb가 아니면 직접 설정해줘야한다. 예) 만약에 위의 코드가 application.rb 로 설정해두었다면 실행코드는 다음과 같다.
 - `$ FLASK_APP=application.rb flask run` 혹은 $ `export FLASK_APP=application.rb` 로 환경변수를 설정하고 `$ flask run`을 실행시킨다.

