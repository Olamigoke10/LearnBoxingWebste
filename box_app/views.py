from django.shortcuts import render, redirect
from .forms import SignUPForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Video

# Create your views here.
def get_video():
    return Video.objects.all()


def home(request):
    videos = get_video()  # Fetch videos
    context = {
        'videos': videos,  # Add videos to context
    }
    return render(request, 'base/home.html', context)


def Signup(request):
    if request.method == 'POST':
        form = SignUPForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            
            user = authenticate(username=username, password=raw_password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome, {username}! Your account was successfully created.")
                return redirect('home')  # Redirect to a home or profile page
            else:
                messages.error(request, "Authentication failed. Please try again.")
        else:
            # Form is invalid, display errors
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field}: {error}")

    else:
        form = SignUPForm()

    return render(request, 'base/register.html', {'form': form})


def loginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
            user = authenticate(request, username=user.username, password=password)
        except User.DoesNotExist:
            user = None
        
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful")
            return redirect('home')
        else:
            messages.error(request, "Invalid email or password")
            
    return render(request, 'base/register.html')


def logoutUser(request):
    logout(request)
    return redirect('home')



def video_list(request):
    videos = get_video()
    context = {
        'videos': videos
    }
    return render(request, 'base/video.html', context)