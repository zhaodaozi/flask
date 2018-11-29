# encoding: utf-8
from flask import Flask,render_template,request,redirect,url_for,session
import config
from models import User
from exts import db

app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/login/",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return  render_template("login.html")
    else:
        telephone_or_username = request.form.get("telephone_or_username")
        password = request.form.get("password")
        user = ""
        if telephone_or_username.isdigit():
            user = User.query.filter(User.telephone==telephone_or_username,User.password==password).first()
        else:
            user = User.query.filter(User.username==telephone_or_username,User.password==password).first()
        if user:
            session["user_id"] = user.id
            session.permanent = True
            return redirect(url_for("index"))
        else:
            return "bad telephone or bad password~"


@app.route("/regist/",methods=["GET","POST"])
def regist():
    if request.method == "GET":
        return render_template("regist.html")
    else:
        telephone = request.form.get("telephone")
        username = request.form.get("username")
        password = request.form.get("password")
        repeat_password = request.form.get("repeat_password")
        #If the phone number has been registered, it cannot be registered
        user = User.query.filter(User.telephone == telephone).first()
        if user:
            return "手机号已被注册"
        else:
            if password != repeat_password:
                return "两次密码不相同"
            else:
                user = User(telephone=telephone,username=username,password=password)
                db.session.add(user)
                db.session.commit()
                #if regist success
                return redirect(url_for("login"))
@app.route("/logout/")
def logout():
    session.pop("user_id")
    return redirect(url_for("login"))

@app.route("/question/",methods=["GET","POST"])
def question():
    if request.method == 'GET':
        return render_template("question.html")
    else:
        pass

@app.context_processor
def my_context_processor():
    user_id = session.get("user_id")
    if user_id:
        user = User.query.filter(User.id == user_id).first()
        if user:
            return {"user": user}
    return {}


if __name__ == '__main__':
    app.run(debug=True)
