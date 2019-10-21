# import the Flask class from the flask module
from flask import Flask, render_template
from flask import request
from tool import *
import os
import jieba
import jieba.posseg as pseg
from database_temp import *



# create the application object
app = Flask(__name__)
PEOPLE_FOLDER = os.path.join('static', 'people_photo')
app.config['UPLOAD_FOLDER']= PEOPLE_FOLDER
x_d = {}
name_list = keyword_from_file("name_file.txt")
for x in name_list:
    a = x.split(",")
    #print(a)
    b = a[0].split(" ")
    name1 =b[0]
    if len(b) > 1:
        name2 = b[1]
    name3 = name1 + name2
    eng_name = a[1]
    
    if (x_d.__contains__(name1)):
        x_d[name1] = x_d[name1]  + "," + a[1]
    else:
        x_d[name1] = eng_name
    
    if (x_d.__contains__(name2)):
        x_d[name2] = x_d[name2]  + "," + a[1]
    else:
        x_d[name2] = eng_name
    
    if (x_d.__contains__(name3)):
        x_d[name3] = x_d[name3]  + "," + a[1]
    else:
        x_d[name3] = eng_name




# use decorators to link the function to a url
@app.route('/')
def home():
    return render_template("statmoss.html")

@app.route('/show_ciku', methods=["POST"])
def show_ciku():
    if request.method == "POST":
        keywords = keyword_from_file("test_dict.txt")
        return render_template("login.html",keywords=keywords)


@app.route('/statmoss', methods=["GET", "POST"])
def show_statmoss():
    return render_template("statmoss.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        fencis = request.form.get("input_fenci")
        add_cikus = request.form.get("input_ciku")
        print(type(fencis))
        if fencis.isspace():
            print("shabimani")
        if add_cikus is None:
            print("shabimani2323")
        if (fencis.isspace() is not True):
            print("jinxifenci is:")
            jieba.load_userdict("test_dict.txt")
            result_flags = []
            result = []
            words = pseg.lcut(fenci)
            for word,flag in words:
                result.append(word)
                result_flags.append(flag)
            return render_template("login.html",result_flags=result_flags,result=result)
        if (add_cikus.isspace() is not True):
            print("tianjaiciku is:" )
            what = open("test_dict.txt",'a+',encoding='utf-8')
            write_word = add_ciku + "\n"
            what.write(write_word)
            what.close()
        #print(result_flags)
    return render_template("login.html")

@app.route('/add_ciku', methods=["GET", "POST"])
def login1():
    if request.method == "POST":
        add_cikus = request.form.get("input_ciku")
        if (len(add_cikus) is not 0):
            keywords = keyword_from_file("test_dict.txt")
            what = open("test_dict.txt",'a+',encoding='utf-8')
            write_word = add_cikus + "\n"
            what.write(write_word)
            what.close()
        #print(result_flags)
    return render_template("login.html")

@app.route('/delete_ciku', methods=["GET", "POST"])
def login3():
    if request.method == "POST":
        add_cikus = request.form.get("shanchu_ciku")
        if (len(add_cikus) is not 0):
            keywords = keyword_from_file("test_dict.txt")
            what = open("test_dict.txt",'w+',encoding='utf-8')
            for element in keywords:
                if (element != add_cikus):
                    print(element)
                    print(add_cikus)
                    write_word = element + "\n"
                    what.write(write_word)
            what.close()
        #print(result_flags)
    return render_template("login.html")

@app.route('/fenci', methods=["GET", "POST"])
def login2():
    if request.method == "POST":
        fencis = request.form.get("input_fenci")
        if (len(fencis) is not 0):
            print("jinxifenci is:" + fencis)
            jieba.load_userdict("test_dict.txt")
            result_flags = []
            result = []
            words = pseg.lcut(fencis)
            for word,flag in words:
                result.append(word)
                result_flags.append(flag)
            words_all = jieba.lcut(fencis,cut_all = True)
            result_all = []
            for word in words_all:
                result_all.append(word)

            return render_template("login.html",result=result,result_flags=result_flags,result_all = result_all)
    return render_template("login.html")

@app.route('/input_question', methods=["GET", "POST"])
def input_question():
    answer = "我不知道啊，什么破问题"
    if request.method == "POST":
        fencis = request.form.get("input_question")
        if (len(fencis) is not 0):
            print("jinxifenci is:" + fencis)
            result_flags = []
            result = []
            words = pseg.lcut(fencis)
            for word,flag in words:
                result.append(word)
                result_flags.append(flag)
            words_all = jieba.lcut(fencis,cut_all = True)
            result_all = []
            for word in words_all:
                result_all.append(word)
            answer = analyse_question(result + result_all)
            return render_template("statmoss.html",question = fencis, answer = answer)
#return render_template("statmoss.html",result=result,result_flags=result_flags,result_all = answer)
    return render_template("statmoss.html")

@app.route('/index')
def index():
    return render_template("index.html",
        message = 'Home')     #这里模块里的第一个user指的是html里面的变量user，而第二个user指的是函数index里面的变量user


def analyse_question(question_fenci):
    target_name = ""
    target_column = ""
    target_condition = ""
    #target_name_list = {"哈登":"Harden","詹姆斯":"Lebron","库里":"Stephen Curry","泡椒":"Paul George","莱恩纳德":"Kawhi Leonard","杜兰特":"Kevin Durant"}
    target_name_list = x_d
    target_condition_list = ["最","最多","最高"]
    target_column_list = ["分","篮板","助攻","失误","盖帽","抢断","板","得分","最高分","几分"]
    print(question_fenci)
    for x in question_fenci:
        print("ci is:" + x)
        if x in target_name_list:
            target_name = x
            print(target_name)
        if x in target_column_list:
            target_column = x
            print(target_column)
        if x in target_condition_list:
            target_condition = x
        print(target_condition)
    if len(target_name) == 0 or len(target_column) == 0 or len(target_condition) == 0:
        return "什么破问题，我不会"
    else:
        return get_a_game_data(target_name,target_column,target_condition)


def get_a_game_data(playername,column,condition):
    #temp_dict = {"哈登":"Harden","詹姆斯":"Lebron","勒布朗":"Lebron","库里":"Stephen Curry","泡椒":"Paul George","小卡":"Paul George","莱恩纳德":"Kawhi Leonard","伦纳德":"Kawhi Leonard","小卡":"Kawhi Leonard","杜兰特":"Kevin Durant"}
    temp_dict = x_d
    player_name = temp_dict[playername]
    player_name = player_name.split(",")[0]
    temp_dict2 = {"得分":"pts","篮板":"reb","助攻":"ast","板":"reb","分":"pts","最高分":"pts","抢断":"stl","失误":"tov","盖帽":"BLK","几分":"pts"}
    column = temp_dict2[column]
    test = get_player_record_data(player_name,column,condition = "DESC")
    print(test)
    result = test[0][2] + "在" + test[0][7] + "对阵" + test[0][8][-3:] + "的比赛中出场" +  test[0][10] + "分钟，狂砍" +test[0][11] + "分" + test[0][23] + "板" + test[0][24] + "助攻" + test[0][25] +  "抢断" + test[0][26] + "盖帽" + test[0][27] + "失误"
    return result;
#将中文翻译成sql语句
#使用sql语句从数据库中提取数据
#讲数据库结果翻译回自然语言


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
