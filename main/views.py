from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import CreateView
from .forms import ClientForm
from .models import *

# Create your views here.


def example(request):
    return render(request, 'main/example.html')


def main(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('example')
    page_info = Page.objects.all()
    menu = Menu.objects.all()
    context = {
        'page_info': page_info,
        'menu': menu,
        'form': form
    }
    return render(request, 'main/index.html', context)



