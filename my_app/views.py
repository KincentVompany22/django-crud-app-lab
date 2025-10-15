from django.shortcuts import render, redirect
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Stamp
from .forms import StopForm


# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def stamps_index(request):
    stamps = Stamp.objects.all()
    return render(request, 'stamps/index.html', {'stamps': stamps})

def add_stop(request, stamp_id):
    form = StopForm(request.POST)
    if form.is_valid():
        new_stop = form.save(commit=False)
        new_stop.stamp_id = stamp_id
        new_stop.save()
    return redirect('stamp-detail', pk=stamp_id) # since my stamp details is a class-based view, need to route using pk instead of stamp_id 

class StampDetail(DetailView):
    model = Stamp
    template_name = 'stamps/detail.html'
   # context_object_name = 'stamp'
    extra_context = {'stop_form': StopForm()} # extra_context - how to pass through additional context using a class-based view as opposed to a view function (like 'stamps' above)

class StampCreate(CreateView):
    model = Stamp
    fields = '__all__'

class StampUpdate(UpdateView):
    model = Stamp
    fields = ['days', 'season', 'year', 'description']

class StampDelete(DeleteView):
    model = Stamp
    success_url = '/stamps/'
    



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






