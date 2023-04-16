from django.shortcuts import render,redirect
from .models import UserProfiles
from .forms import UpdateProfileForm
from django.contrib import messages


# Create your views here.
def profile(request, pk):
    user_profile = UserProfiles.objects.get(profile_id=pk)
    context = {'profile': user_profile}
    return render(request, 'profiles/profile.html', context)


def account(request):
    user_account = request.user.userprofiles
    context = {'account': user_account}
    return render(request, 'profiles/account.html', context)

def UpdateProfile(request):
    profile =request.user.userprofiles
    form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        form=UpdateProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            messages.info(request,"you updated your profile")
            return redirect('account')
    context = {'form': form}
    return render(request, 'profiles/updateprofile.html', context)

def deleteProfile(request):
    profile=request.user.userprofiles
    form = UpdateProfileForm(instance=profile)
    if request.method == 'POST':
        profile.delete()
        user=request.user
        user.delete()
        # messages.error(request,"your Profile has been Deleted")
        # return redirect('index')

    context={'form': form}
    return render(request, 'profiles/deleteprofile.html', context)
