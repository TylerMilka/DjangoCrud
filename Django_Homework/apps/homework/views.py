from django.shortcuts import render, redirect
from homework.models import CodeSnippets

def index(request):
    newcode = CodeSnippets.objects.all()
    context = {'newcode': newcode}
    return render(request, 'django_homework/index.html', context)

def create(request): 
    print (request.POST) 
    newcode = CodeSnippets(name=request.POST['name'],language=request.POST['language'], code=request.POST['code'])
    newcode.save()
    return redirect('/')  
