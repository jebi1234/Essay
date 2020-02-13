from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Essay2 ,Essay3

# Create your views here.
def essaysignupcomponent(request):
    return render(request,'essaysignupcomponent.html')
def submit(request):
    if request.method == 'POST':
        name = request.POST['name']
        date = request.POST['date']
        phone = request.POST['phone']
        email=request.POST['email']
        state = request.POST['state']
        language = request.POST['language']
        gender = request.POST['gender']
        category = request.POST['category']
        subcategory = request.POST['subcategory']
        
        
        essay = Essay2(name=name,date=date,phone=phone,email=email,state=state,language=language,gender=gender,category=category,subcategory=subcategory)
        #user =User.objects.create_user(first_name=first_name,last_name=last_name,username=username)

        essay.save();
        messages.info(request,'Succefully submited')
        return redirect('essaysubmitcomponent.html')
    else:
        return render(request,'submit')
def essaysubmitcomponent(request):
    if request.method =="POST":
        title = request.POST['title']
        lang = request.POST['lang']
        essay = request.POST['essay']

        essay1=Essay3(title=title,lang=lang,essay=essay)
        essay1.save();
        return redirect('essaysignupcomponent.html')
        

    else:
        return render(request,'essaysubmitcomponent.html')