from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from auth_app.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def registerView(request):
    form = UserCreationForm()
    template_name = 'auth_app/register.html'
    context = {"form": form}
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login_urls')

    return render(request, template_name, context)

def loginView(request):
    template_name = 'auth_app/login.html'
    context = {}
    if request.method == 'POST':
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        #print(un,pw)
        user = authenticate(username=un, password=pw)
        if user is not None:
            login(request, user)
            return redirect('showemp_urls')
        else:
            messages.error(request,"Invalid Credentials!")
    
    return render(request, template_name, context)

def logoutView(request):
    logout(request)
    return redirect('login_urls')