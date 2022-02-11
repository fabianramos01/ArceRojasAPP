from django.shortcuts import render, redirect
from django.core.paginator import Paginator

from apps.properties.forms import OwnerForm, PropertyForm
from apps.properties.models import Property


def home(request):
    paginator = Paginator(Property.objects.all(), 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'properties': page_obj})

def owner(request):
    form, errors = OwnerForm(), None
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('properties:home')
        errors = form.errors
    return render(request, 'owner_form.html', {'form': form, 'errors': errors})

def property(request):
    form, errors = PropertyForm(), None
    if request.method == 'POST':
        form = PropertyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('properties:home')
        errors = form.errors
    return render(request, 'property_form.html', {'form': form, 'errors': errors})