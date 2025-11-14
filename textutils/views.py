#created by Ashik
from django.shortcuts import render

def index(request):
    return render(request, 'home.html')

def analyzer(request):
    djtext = request.GET.get('text', 'default')
    action = request.GET.get('action', 'none')
    new_line=""
    # UPPERCASE
    if action == "uppercase":
        new_line = djtext.upper()

    # lowercase
    elif action == "lowercase":
        new_line = djtext.lower()
    elif(action=="removePunc"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        new_line = ""
        for char in djtext:
            if char not in punctuations:
                new_line = new_line + char
    # REMOVE spaces
    elif action == "extraSpace":
        
        for i in djtext:
            if i==" ":
                new_line=new_line+""
            else:
                new_line=new_line+i
    elif action=="newLine":
        for j in djtext:
            if j=="\n" or j=="\r":
                new_line=new_line+""
            else:
                new_line=new_line+j
    else:
        l=0
        for i in djtext:
            l=l+1
        new_line="Total characters are: "+str(l)

    context = {
        'previous_text': djtext,
        'value': new_line,
    }

    return render(request, 'analyze.html', context)
