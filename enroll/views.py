from django.shortcuts import render, HttpResponseRedirect
from .forms import Employee
from .models import register


# Create your views here.
def show(request):
    if request.method == 'POST':
        form = Employee(request.POST)
        if form.is_valid():
            fr = form.cleaned_data['First_name']
            lr = form.cleaned_data['Last_name']
            em = form.cleaned_data['Email']
            pw = form.cleaned_data['Password']
            reg = register(First_name=fr, Last_name=lr, Email=em, Password=pw)
            reg.save()
            form = Employee()
    else:
        form = Employee()
    emp = register.objects.all()
    return render(request, 'enroll/addshow.html', {'form': form, 'emp': emp})


# This function will delete data
def delete(request, id):
    if request.method == 'POST':
        pi = register.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')


# This function will update data
def update(request, id):
    if request.method == 'POST':
        pi = register.objects.get(pk=id)
        form = Employee(request.POST, instance=pi)
        if form.is_valid():
            form.save()
    else:
        pi = register.objects.get(pk=id)
    form = Employee(instance=pi)
    return render(request, 'enroll/update.html', {'form': form})
