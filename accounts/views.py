from django.contrib.auth.models import User
from .models import Balance
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

def signup(request):
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            instance = Balance(user=user, balance=0)
            instance.save()
            login(request, user)
            return redirect('profile')

    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form':form}) 
    
    
def profile(request):
    msg = ""
    if request.method == 'POST':
        try:
            username = request.POST['username']
            amount = request.POST['amount']
            senderUser = User.objects.get(username=request.user.Username)
            recieverUser = User.objects.get (usename=username)
            sender = Balance.objects.get(user=senderUser)
            receiver = Balance.objects.get(user=recieverUser)
            sender.Balance = sender.Balance - int(amount)
            receiver.Balance = receiver.Balance + int(amount)
            sender.save()
            receiver.save()
            msg = "Transaction Success"
        except Exception as E :
            print(E)
            msg = "Transaction Failure, Please check and try again"  
    
    user = Balance.objects.get(user= request.user)
    return render(request, 'profile.html', {'balance':user.balance})
        