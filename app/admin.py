from django.contrib import admin
from .models import product,category,User_Signup,Contact,Order,Company_Account,Service,Job,User_Contatact_Job,User_Contatact_Service
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    
    list_display=('name','category','stock','price')





admin.site.register(product,ProductAdmin)
admin.site.register(category)
admin.site.register(User_Signup)
admin.site.register(Contact)
admin.site.register(Order)

admin.site.register(Company_Account)
admin.site.register(Service)
admin.site.register(Job)
admin.site.register(User_Contatact_Service)
admin.site.register(User_Contatact_Job)

