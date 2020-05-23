from django.shortcuts import render
from django.views.generic import ListView, CreateView # новый
from django.urls import reverse_lazy # новый
from django.http import JsonResponse, HttpResponse

from .forms import FaceFinderForm # новый
from .models import FaceFinder

class HomePageView(ListView):
    model = FaceFinder
    template_name = 'home.html'

class LoadDataView(CreateView): # новый
    model = FaceFinder
    form_class = FaceFinderForm
    template_name = 'home.html'
    success_url = reverse_lazy('home')


def processing_run(request):
    if request.method == 'POST':
        submit_btn = request.POST.get("submit")

        name = ''
        image = ''
        video = ''
        
        form = FaceFinderForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data.get('title')
            image = form.cleaned_data.get('imageIn')
            video = form.cleaned_data.get('videoIn')
        # name = request.POST.get('title')
        # image = request.POST.get('imageIn')
        # video = request.POST.get('videoIn')
        # userform = FaceFinderForm()
        return HttpResponse(name,';', image,';', video)
        name = ("_".join(name.split()))
        from subprocess import Popen
        Popen(['python3', 'multiproc.py', video, image, name])
