#!/usr/bin/python
# -*- coding: UTF-8 -*-
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response


# 第一种方法
'''
def index(req):
    t = loader.get_template('index.html')
    c = Context({})
    return HttpResponse(t.render(c))
    # return HttpResponse('<h1>welcome to django!</h1>')
'''


class Person(object):
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say(self):
        return 'my name is ' + self.name


# 第二种方法
def index(req):
    user = Person('倪达玉', 24, '男')
    book_list = ['python', 'java', 'php', 'C++']
    zidian = {
        'name': 'tom',
        'age': '22',
        'school': 'ldu'
    }
    # 传递参数
    return render_to_response('index.html', {
        'title': 'django_test',
        'user': user,
        'book_list': book_list,
        'zidian': zidian
    })
