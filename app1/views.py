from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from app1.models import works,contact_form_info,projects
from django.utils import timezone
def index(request):
    pros=projects.objects.all()
    context={ 
        'projects':pros
    }
    return render(request,'index.html',context)

def my_work(request):
    all_works=works.objects.all()
    context={
        'works':all_works
    }
    return render(request,'my_work.html',context)

def about_me(request):
    context={}
    return render(request,'about_me.html',context)

def contact_me(request):
    context={}
    return render(request,'contact.html',context)
def contact_form(request):
    if request.method =="POST":
        name=request.POST.get("name")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        context={
            "name":name,
            "subject":subject,
            "message":message
        }
        html_template=render_to_string("email.html",context)
        is_error=False
        is_success=False
        error_message=""
        try:
            send_mail(
                subject=subject,
                message=None,
                html_message=html_template,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False
            )
        except Exception as e :
            is_error=True
            error_message=str(e)
            messages.error(request,"There is an error!!!")
        else:
            is_success=True
            messages.success(request,"Email is sent successfully.")
        contact_form_info.objects.create(
            name=name,
            subject=subject,
            message=message,
            action_time=timezone.now(),
            is_error=is_error,
            is_success=is_success,
            error_message=error_message
        )
    return redirect("contact")
def project_details(request):
    context={}
    return render(request,'project_details.html',context)
