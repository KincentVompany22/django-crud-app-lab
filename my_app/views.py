from django.shortcuts import render, redirect, reverse
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Stamp, Stop
from.forms import StopForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def stamps_index(request):
    stamps = Stamp.objects.all()
    return render(request, 'stamps/index.html', {'stamps': stamps})

class StampDetail(DetailView):
    model = Stamp
    template_name = 'stamps/detail.html'
    # context_object_name = 'stamp'
    extra_context = {'stop': Stop} # extra_context - how to pass through additional context using a class-based view as opposed to a view function (like 'stamps' above)

class StampCreate(CreateView):
    model = Stamp
    fields = '__all__'

class StampUpdate(UpdateView):
    model = Stamp
    fields = ['days', 'season', 'year', 'description']

class StampDelete(DeleteView):
    model = Stamp
    success_url = '/stamps/'



class StopCreate(CreateView):
    model = Stop
    form_class = StopForm # fields are specified in StopForm in forms.py file
    def form_valid(self, form):
        form.instance.stamp_id = self.kwargs['stamp_id'] # attaches Stop form submission to parent Stamp
        return super().form_valid(form)

class StopUpdate(UpdateView):
    model = Stop
    form_class = StopForm
    
class StopDelete(DeleteView):
    model = Stop
    def get_success_url(self): # since directing to a dynamic URL (referencing stamp.pk) you have to use get_success_url instead of just success_url like in StampDelete
        return reverse("stamp-detail", kwargs={"pk": self.object.stamp.pk}) # have to include object.stamp because by default the current object is stop not stamp. So to access stamp you have to reference object


# Just testing data below - real data defined in model
'''
class Stamp:
    def __init__(self, name, days, season, year, description):
        self.name = name
        self.days = days
        self.season = season
        self.year = year
        self.description = description

stamps = [
    Stamp('Argentina', 12, 'Winter', '2023', 'Was so fun!'),
    Stamp('Japan', 8, 'Spring', '2022', 'Cherry blossoms everywhere, unforgettable!'),
    Stamp('Italy', 15, 'Summer', '2024', 'Ate pasta every single day, zero regrets.'),
    Stamp('Canada', 10, 'Fall', '2021', 'The maple leaves were unreal!'),
]
'''






