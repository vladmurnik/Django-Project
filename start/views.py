from django.shortcuts import render

def index(request):
    return render(request,"start/index.html")
def index_haha(request):
    return render(request,"start/index_haha.html")