# -*- coding: utf-8 -*-
# all the imports
import os
from werkzeug import secure_filename
from datetime import datetime as dt
from LoveMemorandum import app
# 文件


def uploads_directory():  # 创建上传目录
    a = app.config['UPLOAD_FOLDER']
    if not os.path.exists(a):
        os.makedirs(a)


def upload_file(a, photo):
    filename = u'({time} by {name}) {file}'.format(
        name=a["sender"],
        time=str(dt.utcnow()).replace(":", "_"),
        file=secure_filename(photo.filename))
    fileroute = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    photo.save(fileroute)
    return filename
