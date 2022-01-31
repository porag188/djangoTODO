
# from django.shortcuts import render
# from django.http import HttpRequest

# def taskList(request):
#     return HttpRequest('Todolist')
# from django.http import HttpResponse
# Create your views here.
from asyncio import Task
from dataclasses import field, fields
from pyexpat import model
from re import template
from statistics import mode
from django.forms import models
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from.models import Task

class CustomLoginView(LoginView):
    template_name='base/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('tasks')
class TaskList(ListView):
    model=Task
    context_object_name='tasks'
class TaskDetail(DetailView):
    model=Task
    context_object_name='task'
    template_name= 'base/task.html'
class TaskCreate(CreateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')
class TaskUpdate(UpdateView):
     model=Task
     fields='__all__'
     success_url=reverse_lazy('tasks')
class DeleteView(DeleteView):
    model=Task
    context_object_name='task'
    success_url=reverse_lazy('tasks')