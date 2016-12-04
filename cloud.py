# coding: utf-8

from leancloud import Engine
from leancloud import LeanEngineError
import requests
from app import app
import time
import smtplib  
import os
from proxies import qiandao_115_proxy

engine = Engine(app)

@engine.before_save('Todo')
def before_todo_save(todo):
    content = todo.get('content')
    if not content:
        raise LeanEngineError('内容不能为空')
    if len(content) >= 240:
        todo.set('content', content[:240] + ' ...')

@engine.define
def qiandao_115_p4():
    qiandao_115_proxy()