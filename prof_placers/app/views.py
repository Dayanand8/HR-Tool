from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse
from django import template
from authentication.forms import *


@login_required(login_url="/login/")
def index(request):
    context = {}
    context['segment'] = 'index'

    html_template = loader.get_template('index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def candidate_search(request):
    msg = None
    success = False
    if request.method == "POST":
        form = SearchForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("firstname")
            last_name = form.cleaned_data.get("lastname")
    else:
        form = SearchForm()
    return render(request, "candidate_search.html",{"form": form, "msg": msg,"success": success})

@login_required(login_url="/login/")
def candidate_register(request):
    msg = None
    success = False
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data.get("firstname")
            last_name = form.cleaned_data.get("lastname")
    else:
        form = RegisterForm()
    return render(request, "candidate_register.html",{"form": form, "msg": msg,"success": success})