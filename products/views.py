from django.shortcuts import render

# Create your views here.
def home(request):
    template_name = 'products/main.html'
    return render(request,template_name)