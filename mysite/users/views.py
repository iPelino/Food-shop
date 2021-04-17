from django.shortcuts import redirect,render
from django.contrib import messages
from django.contrib.auth.decorators import login_required 
from .forms import RegisterForm

def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f' welcome {username}, account has created')
            return redirect('login')
    else:
       form = RegisterForm()
    return render(request, 'users/register.html', {'form':form})
@login_required
def profilepage(request):

    return render(request, 'users/profile.html')