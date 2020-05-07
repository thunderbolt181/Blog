from django.contrib.auth.models import models
from django.db import models
from django.utils import timezone
from .forms import EditProfileForm, EditUserForm, registraionform
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, redirect
from blog.models import Post
from django.contrib.auth.models import User
import os

def register(request):
    if request.method == "POST":
        form = registraionform(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')
    else:
        form = registraionform()
    return render(request, 'users/register.html', {'form':form})

@login_required
def profile(request, post_author_id):
    if int(post_author_id) == request.user.id:
        edit_show=True
        user = User.objects.get(id=int(post_author_id))
    else:
        edit_show=False
        user = User.objects.get(id=int(post_author_id))
    post = Post.objects.filter(author=int(post_author_id))
    page = request.GET.get('page', 1)
    paginator = Paginator(post, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context ={'user':user,'posts':posts[::-1],'edit_show':edit_show,"title":request.user.username}
    return render(request,'users/profile.html',context)

@login_required
def profile_update(request):
    if request.method == "POST":
        image_url=request.user.profile.image.path
        u_form = EditUserForm(request.POST, instance=request.user)
        p_form = EditProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            os.remove(image_url)
            u_form.save()
            p_form.save()
            if "media"+str(p_form.cleaned_data['image']) not in request.user.profile.image.url:
                Post(image=p_form.cleaned_data['image'],
                   status='Updated Proile Picture',
                   Date=timezone.now(),
                   author=request.user).save()
            return redirect('profile',post_author_id=request.user.id)
    else:
        u_form = EditUserForm(instance=request.user)
        p_form = EditProfileForm(instance=request.user.profile)
    form = {'u_form':u_form,'p_form':p_form}
    return render(request, 'users/profile_update.html', form)

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('profile',request.user.id)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'users/change_password.html', {'form': form})