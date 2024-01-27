from django.contrib import admin
from. models import  *
# Register your models here.

class contactusAdmin(admin.ModelAdmin):
    list_display = ('id','Name','Mobile','Email','Message')
admin.site.register(contactus,contactusAdmin)
#######################################################################
class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','Name','CPic')
admin.site.register(category,categoryAdmin)
########################################################################
class maincateAdmin(admin.ModelAdmin):
    list_display = ('id','Name','picture','cdate')
admin.site.register(maincate,maincateAdmin)
######################################################################
class myproductAdmin(admin.ModelAdmin):
    list_display = ('id','mcategory','pcategory','pprice','dprice','pcolor','pdes','pdel','ppic','pdate','psize')
admin.site.register(myproduct,myproductAdmin)

########################################################################
class registerAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','ppic','passwd','address')
admin.site.register(register,registerAdmin)

########################################################################
class mcartAdmin(admin.ModelAdmin):
    list_display = ('id','userid','pid','status','cdate')
admin.site.register(mcart,mcartAdmin)

########################################################################
class morderAdmin(admin.ModelAdmin):
    list_display =('id','userid','status','odate','pid','remarks')
admin.site.register(morder,morderAdmin)