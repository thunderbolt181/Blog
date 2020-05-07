from django.shortcuts import render, redirect
from django.http  import HttpResponse
from blog.models import Post
from blog.forms import BlogCreateForm, BlogUpdateForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db import models
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.contrib.auth.models import User

def search_fun(request):
    if request.method == "GET":
        if request.GET.get('q') != None and request.GET.get('q') != "":
            search = request.GET['q']
            lookup = Q(username__icontains = search)
            result = User.objects.filter(lookup).distinct()
            if len(result) !=0:
                content = {
                    'results':result,
                    'search':search,
                    'title':"Home",
                }
                return render(request, 'blog/search.html',content)
            else:
                content = {
                'no_result':"No Search Results Found",
                'title':"Home",
                }
            return render(request, 'blog/search.html',content)
        else:
            return redirect('blog-home')

def about(request):
    return render(request, 'blog/about.html',{"title":"About"})

@login_required
def home(request):
    post = Post.objects.all()[::-1]
    page = request.GET.get('page', 1)

    paginator = Paginator(post, 10)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    content = {
        "posts": posts ,
        'title':"Home",
    }
    return render(request, 'blog/home.html',content)

@login_required
def PostCreate(request):
    if request.method=="POST":
        c_form = BlogCreateForm(request.POST, request.FILES)
        if c_form.is_valid():
            post = c_form.save(commit=False)
            post.author=request.user
            post.date=timezone.now()
            post.status='Posted an Update'
            post.save()
            return redirect('blog-home')
    else:
        c_form = BlogCreateForm()
    return render(request, 'blog/Create_post.html',{'c_form':c_form})

@login_required
def PostDetailView(request, post_id):
    try :
        post_object = Post.objects.get(id=post_id)
    except:
        raise Http404("Post Does Not Exist")
    return render(request, 'blog/detail_view.html',{"object":post_object})

@login_required 
def UpdatePost(request, post_id):
    try : 
        if Post.objects.get(id=post_id).author.id == request.user.id:      
            post_object = Post.objects.get(id=post_id)
            if request.method == "POST":
                u_form = BlogUpdateForm(request.POST,request.FILES, instance=post_object)
                if u_form.is_valid():
                    u_form.save()
                    return render(request, 'blog/detail_view.html',{"object":post_object})
            else:
                u_form = BlogUpdateForm( instance=post_object)
                return render(request, 'blog/update_post.html',{"u_form":u_form,"object":post_object})
        else:
            raise Http500("Post Does Not Exist 1")
    except:
        raise Http404("Post Does Not Exist 2")
    

@login_required
def PostDelete(request, post_id):
    try : 
        post_object = Post.objects.get(id=post_id)
        post_object.delete()
    except:
        raise Http404("Post Does Not Exist")
    return redirect('blog-home')

