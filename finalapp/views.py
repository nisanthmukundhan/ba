from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from finalapp.forms import RegisterrForms
from finalapp.models import District, Branch, Registerr, City


# Create your views here.

def home(request):
    return render(request, 'home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('finalapp:button')
        else:
            messages.info(request, 'invalid')
            return redirect('finalapp:login')

    return render(request, 'login.html')


def registerform(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if cpassword == password:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('finalapp:login')

        else:
            messages.info(request, "password not match")
    return render(request, 'registerform.html')


def logout(request):
    auth.logout(request)
    return redirect('/')


def button(request):
    return render(request, 'button.html')


def registerr(request):
    form = RegisterrForms
    if request.method == 'POST':
        form = RegisterrForms(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'form has been submitted')

    return render(request, 'register.html', {'form': form})


def districtdetail(request, d_slug):
    district = District.objects.get(slug=d_slug)
    return render(request, 'district.html', {'district': district})


def load_branches(request):
    district_id = request.GET.get('district_id')
    branches = Branch.objects.filter(district_id=district_id).all()
    return render(request, 'branchdropdown.html', {'branches': branches})


def person_update_view(request, pk):
    person = get_object_or_404(Registerr, pk=pk)
    form = RegisterrForms(instance=person)
    if request.method == 'POST':
        form = RegisterrForms(request.POST, instance=person)
        if form.is_valid():
            form.save()
            return redirect('person_change', pk=pk)
    return render(request, 'home.html', {'form': form})


# AJAX
def load_cities(request):
    country_id = request.GET.get('country_id')
    cities = City.objects.filter(country_id=country_id).all()
    return render(request, 'city_dropdown_list_options.html', {'cities': cities})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)
