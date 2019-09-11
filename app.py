# import the Flask class from the flask module
from flask import Flask, render_template
from flask import request
import os
import jieba
# create the application object
app = Flask(__name__)
PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app.config['UPLOAD_FOLDER']= PEOPLE_FOLDER


# use decorators to link the function to a url
@app.route('/')
def home():
    test = os.listdir(os.getcwd())
    input = "flask功能测试"
    list = jieba.lcut(input)
    return "Hello, World!" + str(list)  # return a string

@app.route('/login', methods=["GET", "POST"])
def login():
    str1 = "test"
    username = ""
    if request.method == "POST":
        username = request.form.get("username")
        userage = request.form.get("userage")
        list = jieba.lcut(username)
        str1 = str(list)
        print(str1)
        return render_template("index.html",message=str1)
    return render_template("login.html")

@app.route('/indesx')
def index():
    user = {'nickname': 'Miguel'} # fake user
    return render_template("index.html",
        title = 'Home',
        user = user)     #这里模块里的第一个user指的是html里面的变量user，而第二个user指的是函数index里面的变量user


@app.route('/test')
def show_index():
    full_filename1 = os.path.join(app.config ['UPLOAD_FOLDER'],'4.png')
    full_filename2 = os.path.join(app.config ['UPLOAD_FOLDER'],'7.png')
    app_finished = "width: 80%;"
    return render_template("test.html",user_image1 = full_filename1,user_image2 = full_filename2)

@app.route('/test2')
def test2():
    return render_template('test2.html')  # render a template


# start the server with the 'run()' method
if __name__ == '__main__':
    app.run('0.0.0.0',8890)
