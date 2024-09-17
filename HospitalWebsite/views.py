from django.shortcuts import render,redirect
from Hospitalapp import models
from django.contrib import messages
from datetime import datetime

def index(request):
    favicon=models.favicon.objects.all()
    title=models.title.objects.all()
    service= models.service.objects.all()
    topbar=models.topbar.objects.all()
    logo=models.logo.objects.all()
    welcome=models.welcome.objects.all()
    why=models.why.objects.all()
    keyservices=models.keyservice.objects.all()
    aboutusvideoimg=models.AboutUsVideoImage.objects.all()
    aboutusdesc=models.AboutUsdesc.objects.all()
    aboutuskservice=models.AboutUskservice.objects.all()
    statitems=models.statitem.objects.all()
    if request.method == 'POST':
       name= request.POST['name']
       email= request.POST['email']
       phone= request.POST['phone']
       date= request.POST['date']
       department= request.POST['department']
       doctor= request.POST['doctor']       
       apointment=models.appointment(name=name, email=email,phone=phone,date=date,department=department,doctor=doctor)
       apointment.save()
       messages.success(request,"Your appointment has been successfully scheduled.")
       date_time_obj = datetime.strptime(date, '%Y-%m-%dT%H:%M')
       date_str = date_time_obj.strftime('%Y-%m-%d') 
       time_str = date_time_obj.strftime('%I:%M %p')
       request.session['data'] = {'name':name,'email':email,'phone':phone,'date':date_str,'time': time_str,'department':department,'doctor':doctor}
       return redirect("success")
    department=models.department.objects.all()
    doctor=models.doctor.objects.all()
    faq=models.faq.objects.all()
    gal=models.gallery.objects.all()
    testimonial=models.testimonial.objects.all()
    address=models.address.objects.all()
               
    data={
        'services':service,
        'topbar':topbar,
        'welcome':welcome,
        'why': why,
        'keyservices':keyservices,
        'title':title,
        'aboutusdesc':aboutusdesc,
        'aboutusvideoimg':aboutusvideoimg,
        'aboutuskservice':aboutuskservice,
        'statitem':statitems,
        'department':department,
        'doctor':doctor,
        'faq':faq,
        'img':gal,
        'testimonial':testimonial,
        'address':address,
        'logo':logo,
        'favicon':favicon,        
    }
    
    return render(request, 'index.html',data)

def success(request):
  data = request.session.get('data', None)
  return render(request, 'appointment_sucess.html',{'data':data})



