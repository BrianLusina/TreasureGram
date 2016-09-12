from django.shortcuts import render, HttpResponseRedirect
from .models import Treasures, User
from .forms import TreasureForm, LoginForm
from django.contrib.auth import authenticate, login, logout


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
    provide form with access to uploaded files to save image
    check if form is valid then clean the data before saving the data in the database
    The form will not commit the changes until it assigns a user to the particular changes
    Redirect to home page even if the form is not valid.
    :param request:
    :return:
    """
    form = TreasureForm(request.POST, request.FILES)
    # check if the form is valid
    if form.is_valid():
        # reads all the form data and saves it to the database
        treasure = form.save(commit=False)
        treasure.user = request.user
        treasure.save()
        # alternatively, if subclassing TreasureForm to Form
        # treasure = Treasures(name=form.cleaned_data['name'],
        #                      value=form.cleaned_data['value'],
        #                      material=form.cleaned_data['material'],
        #                      location=form.cleaned_data['location'],
        #                      img_url=form.cleaned_data['img_url'])
        # treasure.save()
    return HttpResponseRedirect('/')


# routes user to a particular user profile
def profile(request, username):
    """
    We look up the user object in the User Model by its username
    get all the treasures associated with that user by using a QuerySet filter to look up all the treasures
    associated with that user.
    Then pass the username and treasures to the template for rendering
    :param request: the request being handled
    :param username: the user name to check for
    :return:
    """
    user = User.objects.get(username=username)
    treasures = Treasures.objects.filter(user=user)
    context = {"username": username, "treasures": treasures}
    return render(request=request, template_name="profile.html", context=context)


# handles login view
def login_view(request):
    """
    Performs 2 functions,
        1. checks whether the request is a post, then authenticate username ana password
        2. else display the loginform
    :param request: the request to be handles by this view
    :return: the rendered template
    """
    if request.method == "POST":

    else:
        form = LoginForm
        context = {"form": form}
        return render(request=request, template_name="login.html", context=context)
