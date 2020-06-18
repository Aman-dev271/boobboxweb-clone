from django.shortcuts import render

# Create your views here.
from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def home (request):
    user =  User.objects.count()
    return render(request , 'home.html', {'user':user})





def signup(request):
    if request.method == 'POST':


        form = UserCreationForm(request.POST)




        if form.is_valid():
            form.save()


            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html',{'form':form})



































