from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Avatar
from .forms import *
from django.views.generic import ListView
from django.views.generic.edit import  UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


#-----------------------------------------------------------------------------------------------------------------------------------------------

# Registrar usuario / register user
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            form.save()
            return render(request, 'BlogHome/home.html')
        else:
            return render(request, 'BlogLogin/register.html', {'messaje':'Error registering user, plase check the data'})
    else:
        form = UserRegistrationForm()
        return render(request, 'BlogLogin/register.html', {'form':form})


# Ingresar ussuario / login user
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            userauth=form.cleaned_data.get('username')
            passwordauth=form.cleaned_data.get('password')
            
            user=authenticate(username=userauth, password=passwordauth)

            if user is not None:
                login(request, user)
                return render(request, 'BlogHome/home.html', {'userlogin':userauth, 'messaje':f'Welcome {userauth} to Mikrotik Blog!!'})
            else:
                return render(request, 'BlogLogin/login.html', {'form':form, 'messaje':'User incorrect'})
        else:
            return render(request, 'BlogLogin/login.html', {'form':form, 'messaje':'Invalid credentials, please check'})
    
    else:
        form=AuthenticationForm()
        return render(request, 'BlogLogin/login.html', {'form':form})


# Cambiar contraseña usuario / change password usuario
@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user) 
            return redirect('profile/<user_id>')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'BlogLogin/changepass.html', {'form': form})

# Editar usuario / edit user
class UserUpdate(LoginRequiredMixin, UpdateView):
    model = UserUpdate
    success_url = reverse_lazy('home')
    fields = ['username', 'email', 'first_name', 'last_name']
    def get_object(self):
        return self.request.user

# Lista de usuarios / list usuarios
class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'BlogLogin/listuser.html'

#visualizar perfil de usuario / view profile user
@login_required
def profile(request, user_id):    
    user = request.user
    try:
        avatar = Avatar.objects.get(user=request.user.id)
        avatar = avatar.avatar.url
    except:
        avatar = 'https://www.gravatar.com/avatar/00000000000000000000000000000000?d=mp&f=y'
    context = {'avatar': avatar}
    return render(request, 'BlogLogin/detailuser.html', context)

