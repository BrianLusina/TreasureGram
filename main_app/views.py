from django.shortcuts import render


# Create your views here.
def index(request):
    context = {'treasures': treasures}
    return render(request=request, template_name="index.html", context=context)


class Treasures(object):
    def __init__(self, name, value, material, location):
        self.name = name
        self.value = value
        self.material = material
        self.location = location


treasures = [
    Treasures("Gold Nugget", 1000, 'gold', 'Curlys creek, NM'),
    Treasures("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO"),
    Treasures("Coffee Can", 20, 'tin', 'ACME, CA'),
    Treasures("Diamond", 5000, 'diamond', 'Peak Valley, NO'),
]