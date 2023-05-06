from django.shortcuts import render
from django.http import HttpResponse
from.models import student
from.models import register
from.models import login
def display(request):
    # print("hello rahman")
    # return HttpResponse("..<h1>hi rahman</h1>")
    x = "rahman"
    u=5
    y=4
    z=u+y
    return render(request,'index.html')
def display1(request,a):
    if a%2==0:
            return HttpResponse("<h1><span style=color:red>entered number is even</span></h1>")
    else:
        return HttpResponse("entered number is odd")
def vowels(request,b):
    c=0
    for i in b:
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            c=c+1
    return HttpResponse("<h1><span style=color:#15BCA8>vowels count is "+str(c)+"</span></h1")
def display3(request):
    return render(request,'2ndhme.html')
def display4(request):
    if request.method=="POST":
        x=int(request.POST['n1'])
        y=int(request.POST['n2'])
        z = int(request.POST['n3'])
        if x>y and x>z:
            return render(request,'2ndhme.html',{'data':x,'dat':y,'da':z,'d':x})
        elif y>x and y>z:
            return render(request, '2ndhme.html', {'data': x, 'dat': y, 'da': z, 'd': y})
        else:
            return render(request, '2ndhme.html', {'data': x, 'dat': y, 'da': z, 'd': z})
def palindrome(request):
    if request.method=="POST":
        x=request.POST['n1']
        t="is palindrome"
        u="not palindrome"
        y=""
        for i in x:
            y=i+y
        if y==x:
            return render(request, 'test.html', {'dat': t})
        else:
            return render(request, 'test.html', {'dat': u})
    else:
        return render(request,'test.html')
def numberv(request):
    if request.method=="POST":
        x=int(request.POST['n2'])
        l=[]
        for i in range(x+1):
            l.append(i)
        return render(request,'test.html',{'data':l})
    else:
        return render(request,'test.html')
def multi(request):
    if request.method=="POST":
        x=int(request.POST['n1'])
        l = []
        for i in range(1,x+1):

            for j in range(1,11):
                y=j*i
                n=str(j)+"x"+str(i)+"="+str(y)
                l.append(n)

        return render(request, 'test2.html', {'data': l})
    else:
        return render(request, 'test2.html')

def prime(request):
    if request.method=="POST":
        x=int(request.POST['n1'])
        y=int(request.POST['n2'])
        l = []
        for i in range(x,y+1):
            if i>1:
                for j in range(2,i):
                    if(i%j)==0:
                        break
                else:
                    l.append(i)
        return render(request, 'test3.html', {'data': l})
    else:
        return render(request, 'test3.html')

def currentbill(request):
    if request.method=="POST":
        x=int(request.POST['id'])
        y=request.POST['na']
        z=float(request.POST['cr'])
        t = float(request.POST['or'])
        u=z-t
        if u<=50:
            a=u*3
            return render(request, 'currentbill.html', {'data': a,'data2':x,'data3':y,'data4':z})
        elif u>50 and u<=100:
            a=50*3+(u*5)
            return render(request, 'currentbill.html', {'data': a,'data2':x,'data3':y,'data4':z})
        elif u>100 and u<=150:
            a=(50*3)+(50*5)+(u-100)*7
            return render(request, 'currentbill.html', {'data': a,'data2':x,'data3':y,'data4':z})
        elif u>150:
            a=(50*3)+(50*5)+(50*7)+(u-150)*10
            return render(request, 'currentbill.html', {'data': a,'data2':x,'data3':y,'data4':z})
    else:
        return render(request, 'currentbill.html')
def about(request):
    return render(request, 'about.html')


globals()
d={'rahman':[23,'ekm'],'rashid':[24,'ekm']}
def pc(request):
    return render(request,'dic.html')
def stud(request):
    if request.method=="POST":
        x=int(request.POST['roll'])
        y=request.POST['nam']
        z=int(request.POST['age'])
        data=student.objects.create(roll=x,name=y,age=z)
        data.save()

        return render(request, 'student.html',{'x':"Created "})
    else:
        return render(request, 'student.html')

def studv(request):
    if request.method=="GET":
        data=register.objects.all()
        return render(request,"student views.html",{"x":data})
def studsearch(request):
    if request.method=="POST":
        x=request.POST["n1"]
        data=student.objects.filter(roll=x)
        return render(request, 'student.html',{"y":data})
    else:
        return render(request, 'student.html')

def studdel(request):
    if request.method=="POST":
        x=request.POST["roll"]
        data=student.objects.filter(roll=x)
        data.delete()
        dat=student.objects.all()
        return render(request, 'studentview.html',{'x':dat})
    else:
        return render(request, 'studentview.html')
def studsandu(request):
    if request.method == "POST":
        t = request.POST['roll']
        y = request.POST['nam']
        z = request.POST['age']
        student.objects.filter(roll=t).update(name=y,age=z)
        return render(request, 'student.html', {"u": "updated"})
    else:
        return render(request, 'student.html')

def regist(request):
    if request.method=="POST":
        x=int(request.POST['roll'])
        y=request.POST['nam']
        z=int(request.POST['age'])
        a=int(request.POST['mark'])
        b=request.POST['usnam']
        c=request.POST['password']
        d=request.FILES['image']
        data=register.objects.create(roll=x,name=y,age=z,mark=a,username=b,password=c,image=d)
        data.save()
        data1=login.objects.create(username=b,password=c)
        data1.save()
        return render(request, 'rlhome.html', {'x': "Created "})
    else:
        return render(request, 'rlhome.html')

# Create your views here.
