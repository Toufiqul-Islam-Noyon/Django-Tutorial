# I have created this file -  Noyon
from django.http import HttpResponse
from django.shortcuts import render


def analyze(request):
    got = request.POST.get('text', 'default')
    countCheckbox = request.POST.get('check', '!got')
    upperCheckbox = request.POST.get('check2', 'Get')
    punctuations = ''' ,.`/\;:"|[]<>~?()!#$%^&*_ '''
    analyzed = ''
    getPunctuations = ''
    upperValue = ''
    
    #conditions 
    if countCheckbox  == 'on':
        for char in got:
            if char not in punctuations:
                analyzed = analyzed + char
            else:
                getPunctuations = getPunctuations + char
    if upperCheckbox == 'on':
        for char in got:
            if char not in punctuations:
                upperValue += char
        upperValue = upperValue.upper()
    else:
        pass
    


    value = { 'text': got, 'purpose': 'Remove Punctuation', 'FinalValue': analyzed, 'punctuationsText': getPunctuations, 'UpperValue': upperValue}
    return render(request, 'removepunc.html', value)
def Back(request):
    return HttpResponse('')

def index(request):
    return render(request, 'index.html')

def About(request):
    return render(request, 'about.html')

    