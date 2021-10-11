from django.contrib import admin
from .models import Post,PostQuery
from django.contrib.admin import AdminSite #built own customize djzmgo admin
from django.contrib.auth.models import Group,User

class ServiceAdmin(admin.ModelAdmin):
    date_hierarchy = 'timeStamp' #filter by date
    list_display=('name','provider')
    list_filter = ('provider',) #filteration in book table
    search_fields = ('name','provider')


class Serviceadminsite(AdminSite):
    title_header = "Local Community Admin"
    site_header = "Local Community Administrator Panel"
    index_title = "Local Community Site Admin"
    site_title = "Community Admin Panel"
admin.site=Serviceadminsite(name="localcommunity") #calling

# Register your models here.
admin.site.register(Post,ServiceAdmin)
admin.site.register(PostQuery)

admin.site.register(User)
admin.site.register(Group)
