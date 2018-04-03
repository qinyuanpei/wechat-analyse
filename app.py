from flask import Flask, redirect, url_for
import itchat
app = Flask(__name__)

# loginCallback
def lc():
    return analyse()

# exitCallback
def ec():
    return login()

@app.route('/')
def login():
    return "请先登录"


@app.route("/dashboard")
def analyse():
    return "登录成功"
    

if __name__ == '__main__':
    itchat.auto_login(hotReload=True, loginCallback=lc, exitCallback=ec)
    app.run()