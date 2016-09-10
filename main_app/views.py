from django.shortcuts import render
from .models import Treasures


# Create your views here.
def index(request):
    treasures = Treasures.objects.all()
    context = {"treasures": treasures}
    return render(request=request, template_name="index.html", context=context)
