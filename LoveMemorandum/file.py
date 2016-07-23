# -*- coding: utf-8 -*-
# all the imports
import os
from werkzeug import secure_filename
from LoveMemorandum import app
# 文件


def uploads_directory():  # 创建上传目录
    a = app.config['UPLOAD_FOLDER']
    if not os.path.exists(a):
        os.makedirs(a)


def upload_file(a, photo):
    filename = u'({name}){file}'.format(
        name=a["sender"],
        file=secure_filename(photo.filename))
    fileroute = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    photo.save(fileroute)
    return filename
