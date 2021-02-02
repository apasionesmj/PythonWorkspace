from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_jobs
from exporter import save_to_file

app = Flask("SuperScrapper")

db = {}

# 누군가가 /에 접속하면 home 메소드 실행
# @는 바로 아래에 있는 함수만을 찾음. 함수를 decorate 해주는 역할
@app.route("/")
def home():
    return render_template("home.html")

# @app.route("/<username>")
# def contact(username):
#     return f"Hello {username} how are you doing?"

#검색 후 결과 화면
@app.route("/report")
def report():
    # print(request.args.get('word'))#딕셔너리 형태로 args 뽑아내기
    word = request.args.get('word')
    if word:
        word = word.lower() # 입력값을 소문자로 표기
        existingJobs = db.get(word)
        if existingJobs:
           jobs = existingJobs
        else :
            jobs = get_jobs(word)
            db[word] = jobs
    else:
        return redirect("/")
    return render_template(
        "report.html", 
        searchingBy = word, 
        resultsNumber = len(jobs),
        jobs = jobs
    )

# 다운로드 받을 수 있는 페이지
@app.route("/export") # export 페이지에 word 없이 접속한다면  exception으로 보내서 홈화면으로 redirect 시킨다.
def export():
    try: # 실행 후 에러 발생시 except 실행
        word = request.args.get('word')
        if not word: # 만약 word가 존재하지 않는다면 아래 코드 실행.
            raise Exception() # raise로 에러 발생시 바로 except 실행
        word = word.lower()
        jobs = db.get(word)
        if not jobs:
            raise Exception()
        save_to_file(jobs)
        return send_file("jobs.csv")
    except:
        return redirect("/")



# 웹 서버 만들기
app.run(host="127.0.0.1")