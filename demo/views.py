from django.shortcuts import render
from django.http import HttpResponse
from . import model
import os

# Create your views here.
def home(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
'''def search(request):
    if request.method == "GET":
	return render(request, 'inex.html')
    elif request.method == "POST":
        PDB_id = request.POST.get("PDB_id", None)'''
def show(req):
    if req.method == "GET":
        return render(req, 'index.html')
    elif req.method == "POST":
        ID = str.lower(req.POST.get("PDB_id"))
        data = {}
        try:
            datalist = model.Protein.objects.get(id=ID)
            datarefer = model.Reference.objects.get(id=ID)
            data['refer'] = datarefer
            data['list'] = datalist
            return render(req,'result.html',data)
        except model.Protein.DoesNotExist:
            return render(req, 'blank.html')

def blastp(req):
    remind = "Blastp with all the membrane proteins!"
    return render(req,"blastp.html",{'remind':remind})

def blast(req):
    if req.method == "GET":
        remind = "You did not enter any thing!"
        return render(req, "blastp.html",{'remind':remind})
    elif req.method == "POST":
        Seq = req.POST.get("Seq")
        with open("/root/Project/fas/temp.fas","w") as fas_file:
            fas_file.write(Seq)
        os.system("blastp -query /root/Project/fas/temp.fas -out /root/Project/fas/temp.blast -db /root/Project/fas/DB -evalue 70 -outfmt 7")
        sz = os.path.getsize("/root/Project/fas/temp.blast")
        if not sz:
            remind = "Your Sequence Fromat is Wrong!!"
            return render(req, "blastp.html",{'remind':remind})
        #with open("/root/Project/fas/temp.blast","r") as bf:
        #    data = bf.read()
        return render(req, "blast.html")
        #return HttpResponse(data)

def Download(req):
    with open("/root/Project/fas/temp.blast","r") as bf:
        data = bf.read()
    return HttpResponse(data)









