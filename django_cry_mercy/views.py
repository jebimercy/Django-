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
        amount = request.POST.get('amount')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')

        query = Student(name=name, email=email, age=age, gender=gender, country=country, city=city, amount=amount)
        query.save()
        return redirect("/")

        return render(request, 'index.html')


def deleteData(request, id):
    d = Student.objects.get(id=id)
    d.delete()
    return redirect("/")
    return render(request, "index.html")


def updateData(request, id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        age = request.POST.get('age')
        amount = request.POST.get('amount')
        gender = request.POST.get('gender')
        country = request.POST.get('country')
        city = request.POST.get('city')

        update_info = Student.objects.get(id=id)
        update_info.name = name
        update_info.email = email
        update_info.age = age
        update_info.amount = amount
        update_info.gender = gender
        update_info.country = country
        update_info.city = city
        update_info.save()


        return redirect("/")


    d = Student.objects.get(id=id)
    context = {"d": d}
    return render(request, "index.html", context)

