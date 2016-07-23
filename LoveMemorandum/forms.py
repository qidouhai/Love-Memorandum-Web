# -*- coding: utf-8 -*-
# all the imports

# 表单处理
from flask_wtf import Form
from flask_wtf.file import FileAllowed, FileField
from wtforms import StringField, PasswordField, SubmitField, TextAreaField


class PostForm(Form):  # 定义发送表单
    title = StringField(u'标题')
    text = TextAreaField(u'正文')
    photo = FileField(u'图片', validators=[FileAllowed(['jpg', 'gif', 'png'])])
    submit = SubmitField(u'记录')


class LoginForm(Form):  # 定义登录表单
    username = StringField(u'请输入用户名')
    password = PasswordField(u'请输入密码')
    submit = SubmitField(u'登录')
