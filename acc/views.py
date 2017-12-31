from django.shortcuts import render

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse




from django.shortcuts import render
from acc.models import customer 
from django.http import HttpResponse
from .forms import NameForm, LoginForm
from django.http import HttpResponseRedirect

def create(request): 
   #Creating an entry   
   cust = customer(name="algorithm",mail="a@gmail.com",course="python",phonenumber="8987877898")
   cust.save()
   #Read ALL entries 
   objects = customer.objects.all() 
   res ='Printing all customers details in the DB : <br>'

   for elt in objects: 
      res += elt.name
      res += elt.mail
      #res += elt.accnumber
      #res += elt.phonenumber
   return HttpResponse(res)

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)

def delete(request):
    obj = customer.objects.all().delete()
    
   # res += 'Printing One entry <br>' 
   

    #Delete an entry
    #res += '<br> Deleting an entry <br>' 


    return HttpResponse("")

def query(request):
    obj = customer.objects.all()
    res = 'Printing One entry <br>' 
    dic={}
    files=["a.dif","b.dif","c.dif","d.dif","e.dif"]
    count=0
    for i in files:
       dic[count]=i
       count=count+1
    print(dic)
    res ='Printing all customers details in the DB : <br>'

    for elt in obj: 
      res += elt.name
      res += elt.mail
    return render(request, 'display.html', {'obj': obj,  'dic':dic})
 

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            user=form.cleaned_data['your_name']
            print("valid Data:",user)
            #return
            return render(request,'result.html',{'user':user})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
    print("render form")
    return render(request, 'name.html', {'form': form})

def display(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
            user=form.cleaned_data['user']
            passwd=form.cleaned_data['password']
            print("valid user:",user)
            print("valid passwd:",passwd)
            #return
            return render(request,'result.html',{'user':user})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()
    print("render form")
    return render(request, 'index.html', {'form': form})
