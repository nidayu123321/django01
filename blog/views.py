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

# 第二种方法
def index():
    return render_to_response('index.html', {})
