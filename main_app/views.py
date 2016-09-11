from django.shortcuts import render, HttpResponseRedirect
from .models import Treasures
from .forms import TreasureForm


# home page for the main app
def index(request):
    treasures = Treasures.objects.all()
    form = TreasureForm()
    context = {"treasures": treasures, "form": form}
    return render(request=request, template_name="index.html", context=context)


# displays the detail view for each treasure
def detail(request, treasure_id):
    context = {"treasure": Treasures.objects.get(id=treasure_id)}
    return render(request=request, template_name='detail.html', context=context)


def post_treasure(request):
    """
    Create a form and link it to the posted data
    check if form is valid then clean the data before saving the data in the database
    Redirect to home page even if the form is not valid.
    :param request:
    :return:
    """
    form = TreasureForm(request.POST)
    # check if the form is valid
    if form.is_valid():
        # reads all the form data and saves it to the database
        form.save(commit=True)
        # altenatively, if subclassing TreasureForm to Form
        # treasure = Treasures(name=form.cleaned_data['name'],
        #                      value=form.cleaned_data['value'],
        #                      material=form.cleaned_data['material'],
        #                      location=form.cleaned_data['location'],
        #                      img_url=form.cleaned_data['img_url'])
        #treasure.save()
    return HttpResponseRedirect('/')
