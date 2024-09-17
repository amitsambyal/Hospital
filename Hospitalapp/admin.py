from django.contrib import admin
from . import models

admin.site.site_header='MEDLIB ADMIN PANEL'
admin.site.site_title='Medlib Admin'
# Register your models here.
@admin.register(models.favicon)
class faviconAdmin(admin.ModelAdmin):
    list_display=['favicon','appletouchicon']
    
@admin.register(models.title)
class titleAdmin(admin.ModelAdmin):
    list_display=['title','page_name']
    
@admin.register(models.logo)
class logoAdmin(admin.ModelAdmin):
    list_display=['logo','logo_text']   

@admin.register(models.topbar)    
class topbarAdmin(admin.ModelAdmin):
    list_display=['email', 'phoneno']     
    
@admin.register(models.welcome)
class welcomeAdmin(admin.ModelAdmin):
    list_display=['title','desc','heroimg']    
    
@admin.register(models.why)
class whyAdmin(admin.ModelAdmin):
    list_display=['title','desc']    
    
@admin.register(models.keyservice)
class keyservicesAdmin(admin.ModelAdmin):
    list_display=['title','desc']       
  
    
@admin.register(models.AboutUsdesc)
class AboutUsdescAdmin(admin.ModelAdmin):
    list_display=['desc'] 
    
@admin.register(models.AboutUsVideoImage)
class AboutUsVideoImageAdmin(admin.ModelAdmin):
    list_display=['videoLink','videoimg']        
    
@admin.register(models.AboutUskservice)  
class AboutUskservicesAdmin(admin.ModelAdmin):
    list_display=['kservice_icon','kservice_title','kservice_desc']  
    
@admin.register(models.service)
class serviceAdmin(admin.ModelAdmin):
    list_display=['service_title','service_icon','service_desc']   
    
@admin.register(models.statitem)
class statitemsAdmin(admin.ModelAdmin):
    list_display=['stat_icon','stat_counter','stat_label']
    
@admin.register(models.appointment)  
class appointmentAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','date','department','doctor']
    
@admin.register(models.department)
class departmentsAdmin(admin.ModelAdmin):
    list_display=['name','title','desc','img']    
    
@admin.register(models.doctor)
class doctorAdmin(admin.ModelAdmin):
    list_display=['name','designation','desc','img','XLink','fbookLink','instaLink','linkedInLink']
    
@admin.register(models.faq)
class faqAdmin(admin.ModelAdmin):
    list_display=['ques','ans']    
    
@admin.register(models.testimonial)
class testimonialAdmin(admin.ModelAdmin):
    list_display=['name','title_position','img','content']    
        
@admin.register(models.gallery)
class galleryAdmin(admin.ModelAdmin):
    list_display=['img']    
    
@admin.register(models.address)
class addressAdmin(admin.ModelAdmin):
    list_display=['H_Name','address','email','phoneNo','XLink','fbookLink','instaLink','linkedInLink']    
     
            
        
      
        
        
        
      
    
            
    
    
   