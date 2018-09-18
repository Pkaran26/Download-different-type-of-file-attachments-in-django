from django.shortcuts import render
from django.http import HttpResponse
from .models import Employee
import csv
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import json
import datetime
import pandas as pd

def index(request):
    #return HttpResponse("Hello")
    return render(request, "index.html")

def insert(reuqest):
    return render(reuqest, "insert.html")

def add(request):
    try:
        name = request.POST['name']
        post = request.POST['post']
        dob = request.POST['dob']
        salary = request.POST['salary']
        e = Employee(name=name, post=post, dob=dob, salary=salary)
        e.save()
        return HttpResponse("<script>alert('save'); window.location.href='./';</script>")

    except ValueError:
        return HttpResponse("<script>alert('field are blank! try again'); window.location.href='./';</script>")

def disp(request):
    context = {}
    try:
        context['emplist'] = Employee.objects.all()
        return render(request, "disp.html", context)
    except:
        return HttpResponse("<script>alert('try again!'); window.location.href='./';</script>")

def download_csv(request):
    try:
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition'] = "attachment;filename=Employee List.csv"
        writer = csv.writer(response)
        emp = Employee.objects.all()
        for e in emp:
            x = []
            x.append(e.name)
            x.append(e.post)
            dob = datetime.datetime.strptime(str(e.dob), '%Y-%m-%d').strftime('%d-%b-%Y')
            x.append(dob)
            join_date = datetime.datetime.strptime(str(e.join_date), '%Y-%m-%d').strftime('%d-%b-%Y')
            x.append(join_date)
            x.append(e.salary)
            
            writer.writerow(x)
        return response
    except:
        return HttpResponse("<script>alert('try again!'); window.location.href='./';</script>")

def download_pdf(request):
    #try:
    response = HttpResponse(content_type='application/pdf')
    response['content-Disposition'] = "attachment;filename=Employee List1.pdf"
    emp = Employee.objects.all()
    p = canvas.Canvas(response)
    PAGE_WIDTH, PAGE_HEIGHT = A4
    #aW = PAGE_WIDTH - 1*inch  
    aH = PAGE_HEIGHT - 1*inch

    p.drawString(20,aH,"Name")
    p.drawString(70,aH,"Post")
    p.drawString(140,aH,"Date of Birth")
    p.drawString(220,aH,"Joining date")
    p.drawString(300,aH,"Salary")
    aHh = aH -40
    for e in emp:
        p.drawString(20,aHh,e.name)
        p.drawString(70,aHh,e.post)
        dob = datetime.datetime.strptime(str(e.dob), '%Y-%m-%d').strftime('%d-%b-%Y')
        p.drawString(140,aHh,dob)
        join_date = datetime.datetime.strptime(str(e.join_date), '%Y-%m-%d').strftime('%d-%b-%Y')
        p.drawString(220,aHh,join_date)
        p.drawString(300,aHh,e.salary)
        aHh -=20
    p.showPage()
    p.save()
    return response
    #except:
     #   return HttpResponse("<script>alert('try again!'); window.location.href='./';</script>")

def download_json(request):
    try:
        emp = Employee.objects.all()
        emplist = []
        for e in emp:
            x = []
            x.append(e.name)
            x.append(e.post)
            dob = datetime.datetime.strptime(str(e.dob), '%Y-%m-%d').strftime('%d-%b-%Y')
            x.append(dob)
            join_date = datetime.datetime.strptime(str(e.join_date), '%Y-%m-%d').strftime('%d-%b-%Y')
            x.append(join_date)
            x.append(e.salary)
            emplist.append(x)
        js = json.dumps(emplist)
        return HttpResponse(js)
    except:
        return HttpResponse("<script>alert('try again!'); window.location.href='./';</script>")

def download_excel(request):
   # try:
    response = HttpResponse(content_type='text/csv')
    response['content-Disposition'] = "attachment;filename=Employee List.xlsx"
    emplist = []
    emp = Employee.objects.all()
    for e in emp:
        x = []
        x.append(e.name)
        x.append(e.post)
        dob = datetime.datetime.strptime(str(e.dob), '%Y-%m-%d').strftime('%d-%b-%Y')
        x.append(dob)
        join_date = datetime.datetime.strptime(str(e.join_date), '%Y-%m-%d').strftime('%d-%b-%Y')
        x.append(join_date)
        x.append(e.salary)
        emplist.append(x)
    pd.DataFrame(emplist).to_excel(response, header=['Name', 'Post', 'Date of Birth', 'Joining Date', 'Salary'], index=False)
    return response
    #except:
     #   return HttpResponse("<script>alert('try again!'); window.location.href='./';</script>")