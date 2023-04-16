from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Post, Category
from .form import PostForm, CommentForm
from django.utils.text import slugify
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .form import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.core.paginator import Paginator


# Create your views here.
def index(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    blog_posts = paginator.get_page(page_number)
    total_page = blog_posts.paginator.num_pages
    context = {'posts': blog_posts, 'lastpage': total_page, 'category': category,
               'totalpagelist': [n + 1 for n in range(total_page)]}
    return render(request, 'cmsapp/index.html', context)


def category(request, slug):
    posts = Post.objects.all()
    category=None
    categories = Category.objects.all()
    if slug:
        category= get_object_or_404(Category,slug=slug)
        allPosts = posts.filter(category=category)
    context = {'category':category,'categories': categories, 'allPosts':allPosts}
    return render(request, 'cmsapp/category.html', context)


def search(request):
    search = request.GET['search']
    categories = Category.objects.all()
    if len(search) > 78:
        allPosts = []
    else:
        allPosts = Post.objects.filter(title__icontains=search)
    context = {'allPosts': allPosts, 'query': search,'categories': categories}
    return render(request, 'cmsapp/search.html', context)


def detail(request, slug):
    post = Post.objects.get(slug=slug)
    posts = Post.objects.exclude(post_id__exact=post.post_id)[:5]
    comments = post.comments.all()
    new_comment = None
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            # messages.info(request, 'Your Comments is Posted')
            return HttpResponseRedirect(reverse('detail', args=[str(post.slug)]))
    else:
        form = CommentForm()
    context = {'post': post, 'posts': posts, 'form': form, 'comments': comments, 'new_comment': new_comment}
    return render(request, 'cmsapp/detail.html', context)


def createPost(request):
    profile = request.user.userprofiles
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.slug = slugify(post.title)
            post.writer = profile
            post.save()
            messages.info(request, 'Article Created Successfully')
            return redirect('createpost')
        else:
            messages.error(request, 'Article not Created')
    context = {'form': form}
    return render(request, 'cmsapp/create.html', context)


def updatePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.info(request, 'Article Updated Successfully')
            return redirect('detail', slug=post.slug)
    context = {'form': form}
    return render(request, 'cmsapp/create.html', context)


def deletePost(request, slug):
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)

    if request.method == 'POST':
        post.delete()
        messages.info(request, 'Article Deleted Successfully')
        return redirect('createpost')
    context = {'form': form}
    return render(request, 'cmsapp/delete.html', context)


def register_page(request):
    register_form = CreateUserForm()
    if request.method == 'POST':
        register_form = CreateUserForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            redirect('login')
            messages.info(request, "Account Created successfully")
    return render(request, 'cmsapp/register.html', {'register_form': register_form})


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.info(request, "Invalid Credential")

    return render(request, "cmsapp/login.html", {})


def logout_user(request):
    logout(request)
    return redirect('index')
