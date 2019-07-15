from django.http import Http404
from django.shortcuts import render, redirect
from django.db import IntegrityError

from contact_manager.models import Contact, Country
from contact_manager.forms import CountryModelForm


def c_form(request):
    if request.method == 'GET':
        template = 'contact.html'
        x = Contact.objects.all()
        print(x)
        data = {'contact_list': x}
        return render(request, template, data)

    elif request.method == 'POST':
        name = request.POST['name']
        mobile = request.POST['mobile']
        email = request.POST['email']
        if len(name) > 3 and 10 <= len(mobile):
            x = Contact(name=name, mobile=mobile, email=email)
            x.save()
            return redirect('c_home')
        else:
            return Http404("Error: Invalid Entry")


def c_form_edit(request, contact_id):
    try:
        x = Contact.objects.get(id=contact_id)
    except Contact.DoesNotExsist:
        return redirect('c_form')
    else:
        if request.method == 'GET':
            template = 'contact.html'
            x = Contact.objects.get(id=contact_id)
            data = {'contact_list': Contact.objects.order_by('name'), 'edit_data': x}
            return render(request, template, data)
        elif request.method == 'POST':
            x = Contact.objects.get(id=contact_id)
            x.name = request.POST['name']
            x.mobile = request.POST['mobile']
            x.email = request.POST['email']
            x.save()
            return redirect('c_home')


def c_form_delete(contact_id):
    try:
        x = Contact.objects.get(id=contact_id)
    except Contact.DoesNotExsist:
        return redirect('c_home')
    else:
        x.delete()
        return redirect('c_form')


def c_forms_form(request):
    if request.method == 'GET':
        template = 'country_form.html'
        data = {'form': CountryModelForm, 'country_list': Country.objects.all()}
        return render(request, template, data)
    elif request.method == 'POST':
        form = CountryModelForm(request.POST)
        if form.is_valid():
            fx = form.cleaned_data
            x = Country(
                name=fx['name'],
                capital=fx['capital'],
                population=fx['population'],
                sea=fx['sea'],
                currency=fx['currency'],
            )
            try:
                x.save()
            except IntegrityError:
                return Http404("Integrity Error")
            else:
                return redirect('c_home')
        else:
            template = 'country_form.html'
            data = {'form': CountryModelForm(), 'country_list': Country.objects.all()}
            return render(request, template, data)
