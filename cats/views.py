from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone
from django.http import JsonResponse
import requests
i = 0
def index(request):
    global i
    i += 1
    return render(request, "cats/index.html", {"url": "https://cataas.com/cat","result":i})