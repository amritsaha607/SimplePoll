from django.shortcuts import render
from django.views import View

from PollApp.models import Choice, Poll, Vote

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

    def get_poll_results(self, poll):
        poll_results = []
        for choice in poll.choices.all():
            voteCount = Vote.objects.filter(poll=poll, choice=choice).count()
            poll_results.append([choice.name, voteCount])
        return poll_results

    def get(self, request, poll_id):
        poll = Poll.objects.get(id=poll_id)
        poll_results = self.get_poll_results(poll)
        return render(
            request,
            template_name="PollApp/poll.html",
            context={
                "poll": poll,
                "poll_results": poll_results,
            }
        )

    def post(self, request, poll_id):
        requestData = request.POST

        choice_id = requestData.get('choice_id')

        poll = Poll.objects.get(id=poll_id)
        choice = Choice.objects.get(id=choice_id)
        Vote.objects.create(
            poll=poll,
            choice=choice,
        )

        poll_results = self.get_poll_results(poll)

        return render(
            request,
            template_name="PollApp/poll.html",
            context={
                "poll": poll,
                "success_message": "Voted Successfully",
                "poll_results": poll_results,
            }
        )
