# -*- coding: utf-8 -*-
# all the imports

from LoveMemorandum import app, lm
from flask import request, redirect, url_for, render_template, flash, jsonify
# Bootstrap 界面
from flask_bootstrap import Bootstrap
# 用户界面时间本地化
from flask_moment import Moment
# 用户界面时间本地化
# 数据库操作
from database import Entries, init_database, newEntry
# 管理器
from forms import PostForm, LoginForm
from mail import send_email
# 文件上传安全性验证
from file import uploads_directory, upload_file
from user import getUser, getAllUser
from flask_login import login_required, logout_user, current_user

bootstrap = Bootstrap(app)
moment = Moment(app)

app.config['Title'] = u"{str} 的记事本".format(str=u" 和 ".join(getAllUser()))
app.config['users'] = getAllUser()


@app.before_request
def before_request():  # 在执行用户请求之前
    init_database()
    uploads_directory()  # 建立上传目录

# 静态页面部分


@app.errorhandler(404)
@app.errorhandler(500)
@app.route('/about/')
def about(e=None):
    return render_template('about.html')


@app.route('/logout/')
def logout():
    flash(u'再见，亲爱的～')
    logout_user()
    return redirect(url_for('show_entries'))

# 静态页面部分


@app.route('/', methods=['GET'])
@login_required
def show_entries():
    name = request.args["name"] if "name" in request.args else u"all"
    page = int(request.args["page"]) if "page" in request.args else 1
    postform = PostForm()
    entries = Entries.query.order_by(Entries.id.desc())
    if name != u"all":
        entries = entries.filter(Entries.sender == name).paginate(
            page, app.config['POSTS_PER_PAGE'], False)
    else:
        entries = entries.paginate(page, app.config['POSTS_PER_PAGE'], False)
    # 将留言信息编组成字典，返回给渲染模板
    return render_template('show_entries.html', form=postform,
                           entries=entries)


@app.route('/ajax/', methods=['GET'])
@login_required
def show_entries_ajax():
    name = request.args["name"] if "name" in request.args else u"all"
    page = int(request.args["page"]) if "page" in request.args else 1
    entries = Entries.query.order_by(Entries.id.desc())
    if name != u"all":
        entries = entries.filter(Entries.sender == name).paginate(
            page, app.config['POSTS_PER_PAGE'], False)
    else:
        entries = entries.paginate(page, app.config['POSTS_PER_PAGE'], False)
    a = []
    for entry in entries.items:
        a.append({"title": entry.title, "text": entry.text,
                  "sender": entry.sender, "time": entry.time,
                  "url": entry.url})
    # 将留言信息编组成字典，返回给渲染模板
    return jsonify({"items": a})


@app.route('/', methods=['POST'])
@login_required
def new_entry():
    postform = PostForm()
    a = {"title": postform.title.data,
         "text": postform.text.data,
         "sender": current_user.username}
    if postform.photo.has_file():  # 如果有文件
        a["filename"] = upload_file(a, postform.photo.data)
    send_email(a)
    newEntry(a)
    flash(u'新记事已经发布了呢～')
    return redirect(url_for('show_entries'))
# 登录处理部分


@app.route('/login/', methods=['GET'])  # GET方法用于访问登录页、POST方法用于传递信息
def login_page():
    return render_template('login.html', form=LoginForm())


@lm.unauthorized_handler
def main_page():
    return render_template('mainpage.html',
                           form=LoginForm())


@app.route('/login/', methods=['POST'])  # GET方法用于访问登录页、POST方法用于传递信息
def login_submit():
    loginform = LoginForm()
    username = loginform.username.data
    password = loginform.password.data
    print username, password
    if getUser(username, password):
        flash(u'欢迎回来，亲爱的 ' + username + u'。')
        return redirect(url_for('show_entries'))  # 登录成功，返回信息
    else:
        flash(u'用户名或者密码不对劲哦～再试一次？')
    return redirect(url_for("login_page"))
# 登录处理部分
