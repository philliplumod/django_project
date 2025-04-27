from django.contrib import admin
from .models import Member

# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    list_display = ("member_id", "firstname", "lastname")
    search_fields = ("firstname",)


admin.site.register(Member, MemberAdmin)
