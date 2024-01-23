from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Subscription)
admin.site.register(Permissions)

admin.site.register(UserProfile)
admin.site.register(MemoryPage)

admin.site.register(ExtendedMemoryPageInfo)

admin.site.register(Award)
admin.site.register(Education)
admin.site.register(FamilyMember)
admin.site.register(HobbyInterest)
