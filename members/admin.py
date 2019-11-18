from django.contrib import admin
from .models import Member
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


class MemberInline(admin.StackedInline):
    model = Member
    # form = UserEmployeeForm
    can_delete = False
    fk_name='user'
    extra = 1
    max_num = 1
    min_num = 1

class MemberUserAdmin(UserAdmin):
    inlines = (MemberInline,)
    list_select_related = ('profile',)
    
    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(MemberUserAdmin, self).get_inline_instances(request, obj)

# UserAdmin.list_display = ('email', )

# Register your models here.
admin.site.unregister(User)
admin.site.register(User, MemberUserAdmin)