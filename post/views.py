from django.shortcuts import render, HttpResponse

# Create your views here.


def post_index(request):
    return HttpResponse("Welcome to index page")


def post_detail(request):
    return HttpResponse("Welcome to detail page")


def post_create(request):
    return HttpResponse("Welcome to create page")


def post_update(request):
    return HttpResponse("Welcome to update page")


def post_delete(request):
    return HttpResponse("Welcome to delete page")