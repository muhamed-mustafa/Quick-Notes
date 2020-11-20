from django.shortcuts import redirect , render , get_object_or_404
from django.contrib.auth.forms import UserCreationForm , PasswordChangeForm
from django.contrib.auth import login , authenticate
from .models import Profile
from .forms import UserForm , ProfileForm
from django.contrib import messages
# Create your views here.

# This function About User SignUp
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Succesfully.. You Become An User In This Website ')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=password)
            login(request,user)

            return redirect('notes:all_notes')
    else:
        form = UserCreationForm()

    context = {'form':form}

    return render(request,'signup.html',context)

# This function About User Profile
def profile(request,slug):
    profile = get_object_or_404(Profile,slug=slug)
    context = {'profile':profile}
    return render(request,'profile.html',context)

# This function About User Edit Profile
def edit_profile(request,slug):
    profile = get_object_or_404(Profile,slug=slug)
    if request.method == 'POST':
        user_form = UserForm(request.POST,instance=request.user)
        profile_form = ProfileForm(request.POST,request.FILES,instance=profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            messages.success(request,'Succesfully.. Your Profile Is Edited')
            new_profile_form = profile_form.save(commit=False)
            new_profile_form.user = request.user
            new_profile_form.save()
            return redirect('accounts:profile',slug=slug)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)

    context = {'user_form':user_form,'user_profile':profile_form}

    return render(request,'edit_profile.html',context)

# This function About User Change Password
def change_password(request,slug):
    profile = get_object_or_404(Profile,slug=slug)
    if request.method == 'POST':
        password_form = PasswordChangeForm(request.user,request.POST)
        if password_form.is_valid():
            password_form.save()
            messages.success(request,'Succesfully.. Your Password Is Change')
            return redirect('accounts:profile',slug=slug)
    else:
        password_form = PasswordChangeForm(request.user)

    context = {'password_form':password_form}

    return render(request,'change_password.html',context)

