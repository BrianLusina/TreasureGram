from django.shortcuts import render
from .models import Treasures


# home page for the main app
def index(request):
    treasures = Treasures.objects.all()
    context = {"treasures": treasures}
    return render(request=request, template_name="index.html", context=context)


# displays the detail view for each treasure
def detail(request, treasure_id):
    context = {"treasure": Treasures.objects.get(id=treasure_id)}
    return render(request=request, template_name='detail.html', context=context)

