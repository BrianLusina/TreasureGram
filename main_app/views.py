from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse

from .models import Treasures
from .forms import TreasureForm, LoginForm


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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
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
    user = get_object_or_404(User.objects, username=username)
    treasures = Treasures.objects.filter(user=user)
    context = {"username": username, "treasures": treasures}
    return render(request=request, template_name="profile.html", context=context)


# handles login view
def login_view(request):
    """
    Performs 2 functions,
        1. checks whether the request is a post, then authenticate username ana password
            pass in the POST request to the loginform
            check if the form is valid, then clean data for username and password before authenticating
        2. else display the loginform
    :param request: the request to be handles by this view
    :return: the rendered template
    """
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            u = form.cleaned_data["username"]
            p = form.cleaned_data["password"]
            user = authenticate(username=u, password=p)
            if user is not None:
                if user.is_active:
                    # if user is active, use a built in function to login the user
                    print("User is valid, active and authenticated")
                    login(request=request, user=user)
                    # redirect to home page
                    return HttpResponseRedirect('/')
                else:
                    print("The password is valid, but the account has been disabled!")
                    return HttpResponse("user was disabled")
            else:
                print("The username and password were incorrect.")
                return HttpResponse("The username and password are incorrect")
    else:
        form = LoginForm
        context = {"form": form}
        return render(request=request, template_name="login.html", context=context)


def signup_view(request):
    """
    Handles the sign up view, creates a new user using the User object
    :param request:
    :return:
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # create the new user
            user = form.save()
            user = authenticate(username=form.cleaned_data.get('username'),
                                password=form.cleaned_data.get('password1'))
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            context = {"form": form}
            return render(request=request, template_name="signup.html", context=context)
    else:
        form = UserCreationForm()
        context = {"form": form}
        return render(request=request,template_name="signup.html", context=context)


# logs out the user
def logout_view(request):
    """
    Logs out the user and redirects to the home page
    :param request:
    :return: redirect to the home page
    """
    logout(request=request)
    return HttpResponseRedirect('/')


# handles like treasure requests sent from AJAX
def like_treasure(request):
    """
    Get the treasure id from the AJAX request and check for it in the database, if if exists add 1 to it
    save the entry
    :param request: request received from AJAX
    :return: HttpResponse passing in the likes since AJAX is expecting that
    """
    treasure_id = request.POST.get("treasure_id", None)
    likes = 0
    if treasure_id:
        treasure = Treasures.objects.get(id=int(treasure_id))
        if treasure is not None:
            likes = treasure.likes + 1
            treasure.likes = likes
            treasure.save()
    return HttpResponse(likes)
