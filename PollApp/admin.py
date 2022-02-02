from django.contrib import admin

from PollApp.models import Choice, Poll

# Register your models here.

admin.site.register(Choice)
admin.site.register(Poll)
