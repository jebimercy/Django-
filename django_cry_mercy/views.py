from django.shortcuts import render, redirect
from .model import Student


def index_page(request):
    data = Student.objects.all()
    context = {"data": data}
    return render(request, "index.html", context)





def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')

        query = Student(name=name, email=email, age=age, gender=gender, country=country, city=city)
        query.save()
        return redirect("/")

        return render(request, 'index.html')
