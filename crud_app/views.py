from django.shortcuts import render, redirect
from .models import Member
# Create your views here.
def index(request):
    members = Member.objects.all()
    context = {'members': members} 
    return render(request, 'index.html', context)

def saves(request):
    if request.method=='POST':
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']

        member=Member(first_name=first_name,last_name=last_name,email=email)
        member.save()
        return redirect('/')

def show_edit(request, id):
    members = Member.objects.get(id=id)
    context = {'members': members}
    return render(request, 'show_edit.html', context)
    
def update(request, id):
    member=Member.objects.get(id=id)
    member.first_name=request.POST['firstname']
    member.last_name=request.POST['lastname']
    member.email=request.POST['email']
    member.save()
    return redirect('/')

def delete(request, id):
    members= Member.objects.get(id=id)
    members.delete()
    return redirect('/')

