from django.db import models


# Create your models here.

class favicon(models.Model):
    favicon=models.ImageField(upload_to='icon')
    appletouchicon=models.ImageField(upload_to='icon')
 
class title(models.Model):
    title= models.CharField(max_length=100)
    page_name=models.CharField(max_length=100,default=None,null=True)
    
    #def _str_(self):
       # return f"{self.title, self.page_name}"
       
class topbar(models.Model):
    email= models.EmailField(max_length=200)
    phoneno=models.CharField(max_length=10)
        
    
class logo(models.Model):
    logo= models.ImageField(upload_to='logo')
    logo_text=models.CharField(max_length=100,default='')
    
class welcome(models.Model):
     heroimg=models.ImageField(upload_to='welcome',null=True)
     title=models.CharField(max_length=50)
     desc=models.TextField(default=None,null=True)
     
class why(models.Model):
     title=models.CharField(max_length=100)
     desc=models.TextField(default=None,null=True)
     
class keyservice(models.Model):
     title=models.CharField(max_length=100)
     desc=models.TextField(default=None,null=True)   
     
class AboutUsVideoImage(models.Model):
     videoLink=models.CharField(max_length=200)
     videoimg=models.ImageField(upload_to='about_us')

class AboutUsdesc(models.Model):
     desc=models.TextField()           
     
class AboutUskservice(models.Model):
    kservice_icon=models.CharField(max_length=100, null= True)
    kservice_title=models.CharField(max_length=200, null=True)
    kservice_desc=models.TextField()     
    
class statitem(models.Model):
    stat_icon= models.CharField(max_length=100)    
    stat_counter=models.CharField(max_length=100)
    stat_label=models.CharField(max_length=100)        
    
class service(models.Model):
    service_icon=models.CharField(max_length=100, null= True)
    service_title=models.CharField(max_length=200,null=True)
    service_desc=models.TextField() 
    
class appointment(models.Model):
    name= models.CharField(max_length=100)
    email= models.CharField(max_length=100)
    phone= models.CharField(max_length=100)
    date= models.CharField(max_length=100)
    department= models.CharField(max_length=100)
    doctor= models.CharField(max_length=100)
    
class department(models.Model):
    name=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    desc=models.TextField()    
    img=models.ImageField(upload_to='department',default='')    
    
class doctor(models.Model):
    name=models.CharField(max_length=100)
    designation=models.CharField(max_length=100)
    desc=models.TextField()    
    img=models.ImageField(upload_to='doctor',default='')    
    XLink=models.CharField(max_length=100,default='')
    fbookLink=models.CharField(max_length=100,default='')
    instaLink=models.CharField(max_length=100,default='')
    linkedInLink=models.CharField(max_length=100,default='')

class faq(models.Model):
    ques= models.CharField(max_length=100)
    ans= models.TextField()
    
class testimonial(models.Model):
    name= models.CharField(max_length=100)
    title_position=models.CharField(max_length=100)
    img=models.ImageField(upload_to='img_testimonial')
    rating=models.IntegerField()
    content=models.TextField()
    
class gallery(models.Model):
    img=models.ImageField(upload_to='gallery')
    
class address(models.Model):
    H_Name= models.CharField(max_length=100)
    address=models.TextField(max_length=500)
    email=models.EmailField(max_length=100)
    phoneNo=models.CharField(max_length=100)
    XLink=models.CharField(max_length=100,default='')
    fbookLink=models.CharField(max_length=100,default='')
    instaLink=models.CharField(max_length=100,default='')
    linkedInLink=models.CharField(max_length=100,default='')
        
    
      
        
           
