from django.shortcuts import render
from django.views import View

from PollApp.models import Poll

# Create your views here.


class HomeView(View):

    def get(self, request):
        polls = Poll.objects.all()
        return render(
            request,
            template_name="PollApp/home.html",
            context={
                "polls": polls,
            }
        )


class PollView(View):

    def get(self, request, poll_id):
        poll = Poll.objects.get(id=poll_id)
        return render(
            request,
            template_name="PollApp/poll.html",
            context={
                "poll": poll,
            }
        )
