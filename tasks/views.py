from django.views import generic

from tasks.models import Task, Tag


class IndexView(generic.ListView):
    model = Task
    template_name = "tasks/index.html"


class TagView(generic.ListView):
    model = Tag
