from django.shortcuts import render

def home(request):
    context = locals()
    template = 'index.html'
    return render(request, template, context)

