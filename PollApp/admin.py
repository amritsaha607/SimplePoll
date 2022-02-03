from django.contrib import admin

from PollApp.models import Choice, Poll, Vote

# Register your models here.

admin.site.register(Choice)
admin.site.register(Poll)
admin.site.register(Vote)
