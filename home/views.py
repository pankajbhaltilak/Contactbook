from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Contact
from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView
from .serializers import ContactSerializer
from rest_framework import permissions

class ContactList(ListCreateAPIView):

    serializer_class=ContactSerializer
    permission_classes=(permissions.IsAuthenticated)

    def perform_create(self, serializer):
        serializer.save(FirstName=self.request.user)

    def get_queryset(self):
        return Contact.objects.filter(FirstName=self.request.user)


class ContactDetailsView(RetrieveUpdateDestroyAPIView):

    serializer_class=ContactSerializer
    permission_classes=(permissions.IsAuthenticated)
    lookup_field="id"

    def get_queryset(self):
        return Contact.objects.filter(FirstName=self.request.user)


def saveinfo(request):
    if request.method == "POST":
        FirstName = request.POST['firstname']
        LastName = request.POST['lastname']
        Email = request.POST['email']
        ContactNumber = request.POST['phone']
        add = Contact(FirstName=FirstName, LastName=LastName, Email=Email, ContactNumber=ContactNumber)
        add.save()
    Data = Contact.objects.all()
    return render(request, "index.html", {'Data': Data})


def index(request):
    Data = Contact.objects.all()
    return render(request, "index.html", {'Data': Data})


def formupdate(request, id):
    if request.method == "POST":
        add = Contact.objects.get(id=id)
        add.FirstName = request.POST["firstname"]
        add.LastName = request.POST["lastname"]
        add.Email = request.POST["email"]
        add.ContactNumber = request.POST['phone']
        add.save()
        return redirect("index")


def edit(request, id):
    Data = Contact.objects.get(id=id)
    return render(request, 'edit.html', {'Data': Data})


def delete(request, id):
    add = Contact.objects.get(id=id)
    add.delete()
    return redirect('index')


def search(request):
    query = request.GET["query1"]
    Data = Contact.objects.filter(FirstName__icontains=query)
    params = {'Data': Data}
    return render(request, 'search.html', params)
