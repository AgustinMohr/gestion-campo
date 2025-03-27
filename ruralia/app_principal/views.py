from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def app(request):
    return render(request, 'app_principal/app.html')

def index_view(request):
    return render(request, 'app_principal/index.html')