#created by Ashik
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'home.html')
def analyzer(request):
    djtext=request.GET.get('text','default')
    removePunc=request.GET.get('removePunc',"off")
    print(removePunc)
    CapitalLetter=request.GET.get('CapitalLetter','off')
    upperCase=request.GET.get('upperCase','off')
    LowerCase=request.GET.get('lowerCase','off')
    if(removePunc=='on'):
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i
    elif(CapitalLetter=='on'):
        analyzed=djtext.capitalize()
    elif(upperCase=='on'):
        analyzed=djtext.upper()
    elif(LowerCase=='on'):
        analyzed=djtext.lower()
    elif(removePunc=='on' and CapitalLetter=='on'):
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i
                analyzed=analyzed.capitalize()
    elif(removePunc=='on' and upperCase=='on'):
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i
                analyzed=analyzed.upper()
    elif(removePunc=='on' and LowerCase=='on'):
        punctuations='''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed=""
        for i in djtext:
            if i not in punctuations:
                analyzed=analyzed+i
                analyzed=analyzed.lower()
    else:
        analyzed=djtext
    removed={
        'previous_text':djtext,
        'value':analyzed,
    }
    return render(request,'analyze.html',removed)