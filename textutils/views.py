from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def contacts(request):
    return render(request, 'contacts.html')

def analyze(request):

    dtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    charcount = request.POST.get('charcount', 'off')
    

    if removepunc =='on' and fullcaps == 'off' and charcount == 'off':
        punctuations = '''!@#$%^&*()_+-'";:.,<>\|/}{[]?'''
        analyzed = ""

        for char in dtext:

            if char not in punctuations:
                analyzed = analyzed+char

        params = {'purpose': ' Remove Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    

    elif fullcaps == 'on' and removepunc == 'off'and charcount == 'off':
        analyzed = ""

        for char in dtext:
            analyzed = analyzed +char.upper()
            
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)  
     
    
    elif removepunc == 'on' and fullcaps == 'on' and charcount == 'off':
        punctuations = '''!@#$%^&*()_+-'";:.,<>\|/}{[]?'''
        analyzed = ""
        analyzed2 = ""

        for char in dtext:
            analyzed2 = analyzed2+char.upper()
            
        for char in analyzed2:

            if char not in punctuations:
                analyzed += char
           
        params = {'purpose': 'Remove Punctuations and Change to Uppercase', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params) 


    elif removepunc == 'on' and fullcaps == 'on'and charcount == 'on':

        punctuations = '''!@#$%^&*()_+-'";:.,<>\|/}{[]?'''
        analyzed = ""
        analyzed2 = ""

        for char in dtext:
            countWSP = len(dtext)
            analyzed2 = analyzed2+char.upper()
            
        for char in analyzed2:
            if char not in punctuations:
                analyzed += char
                countWSWtP = len(analyzed)

        params = {'purpose': 'Character count with removed Punctuation and change to Uppercase', 'analyzed_text': analyzed, 'countWSWtP_text': countWSWtP, 'countWSP_text': countWSP}
        return render(request, 'analyze.html', params) 
    

    elif removepunc == 'off' and fullcaps == 'on'and charcount == 'on':

        punctuations = '''!@#$%^&*()_+-'";:.,<>\|/}{[]?'''
        analyzed = ""
        analyzed2= ""

        for char in dtext:
            countWSP = len(dtext)
            analyzed = analyzed+char.upper()

        for char in analyzed:
            if char not in punctuations:
                analyzed2 += char
                countWSWtP = len(analyzed2)

        params = {'purpose': 'Character count and converting to Uppercase', 'analyzed_text': analyzed, 'countWSWtP_text': countWSWtP, 'countWSP_text': countWSP}
        return render(request, 'analyze.html', params) 
            

    elif removepunc == 'on' and fullcaps == 'off'and charcount == 'on':

        punctuations = '''!@#$%^&*()_+=-'";:.,<>\|/}{[]?'''
        analyzed = ""
        analyzed2= ""

        for char in dtext:
            countWSP = len(dtext)
            if char not in punctuations:
                analyzed += char
        
        for char in analyzed:
            countWSWtP = len(analyzed)

        params = {'purpose': 'Character count and removing the punctuation', 'analyzed_text': analyzed, 'countWSWtP_text': countWSWtP, 'countWSP_text': countWSP}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")
    

    
   





