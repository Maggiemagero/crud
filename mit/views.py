from django.shortcuts import render

from mit.models import Student


# Create your views here.
def home(request):
    d = Student.objects.all()
    return render(request, 'home.html', {"d": d})


def insert(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        school = request.POST.get('school')
        print(name, email, school)
        data = Student(name=name, email=email, school=school)
        data.save()
    return render(request, 'home.html')
