from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileUpdateForm, UserRegistrationForm, UserUpdateForm
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(request):
    if request.method == 'POST':
        u_form = UserRegistrationForm(request.POST)
        if u_form.is_valid():
            u_form.save()
            username = u_form.cleaned_data.get('username')
            messages.success(request, f"Account created {username} !")
            return redirect('livfitprofile')
        else:
            messages.warning(request, f"Error creating account")
    else:
        u_form = UserRegistrationForm()

    context = {
        'form': u_form,
    }
    return render(request, 'user/registration.html', context)


@login_required
def profile_update(request):
    if request.POST:
        m_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if m_form.is_valid() and p_form.is_valid():
            m_form.save()
            p_form.save()
            messages.success(request, f"User Profile Updated Successfully")
            return redirect('livfitprofile')
        else:
            messages.warning(request, "Update Failed")

    else:
        m_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'm_form': m_form,
        'p_form': p_form
    }
    return render(request, 'user/update.html', context)
