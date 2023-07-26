from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.template.loader import get_template

# Create your views here.
def home_page(request):
    template = get_template('home.html')
    
    return HttpResponse(template.render(context={},request=request))

def add_data(request):
    if request.method == 'POST':
        check_keys = ['name','surname','age']
        post_data = request.POST
        
        data = [dict((key,value) for key,value in post_data.items() if key in check_keys)]
        return redirect('show-data', name=data[0]['name'], surname=data[0]['surname'], age=data[0]['age'])
    
    elif request.method == 'GET':
        return render(request,'add.html')

def show_data(request,name=None,surname=None,age=None):
    if name and surname and age != None:
        data = {
            'name' : name,
            'surname' : surname,
            'age' : age
        }
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({},safe=False)

# safe = False - используется когда переданные данные могут быть не безопасным для преобразования в JSON