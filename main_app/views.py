from django.shortcuts import render


# Create your views here.
def index(request):
    name = "Gold Nugget"
    value = 1000.00
    context = {'treasure_name': name,
               'treasure_val': value}
    return render(request=request, template_name="index.html", context=context)
