from django.shortcuts import render
from .models import student
from .forms import studentform
# Create your views here.
def insert(request):
    st=studentform()
    if request.method=='POST':
        obj=request.POST
        name=obj.get('name')
        age=obj.get('age')
        student.objects.create(name=name,age=age)
        return render(request,'done.html')
    return render(request,'insert.html',{'form':st})

    

def view(request):
    data=student.objects.all()
    return render(request,'view.html',{'data':data})
