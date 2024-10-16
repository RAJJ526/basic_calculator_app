from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def jod(request):
    if request.method=="POST":
        number_1=request.POST['number_1']
        number_2=request.POST['number_2']
        operation=request.POST['operation']
    if operation=="add":
        result=float(number_1)+float(number_2)
        return render(request, 'index.html', {"result":result})
    
    elif operation=="subtract":
        result=float(number_1)-float(number_2)
        return render(request, 'index.html', {'result':result})
    
    elif operation=="multiply":
        result=float(number_1)*float(number_2)
        return render(request, 'index.html', {'result':result})
    
    elif operation=="divide":
        result=float(number_1)/float(number_2)
        return render(request, 'index.html', {'result':result})

    else:
        
        return render(request, 'index.html')

    
