#created by Ashik
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'home.html')
def removePunc(request):
    djtext=request.GET.get('text','default')
    punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    analyzed=""
    for i in djtext:
        if i not in punctuations:
            analyzed=analyzed+i
    removed={
        'previous_text':djtext,
        'value':analyzed,
    }
    return render(request,'analyze.html',removed)