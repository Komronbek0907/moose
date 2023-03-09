from django.shortcuts import render, redirect
from .models import Blog, Contact, Comment


def home_view(request):
    posts = Blog.objects.filter(is_published=True)
    context = {
        'posts': posts
    }

    return render(request, 'index.html', context)


def blog_view(request):
    posts = Blog.objects.filter(is_published=True)
    context = {
        'posts': posts
    }
    return render(request, 'blog.html', context)


def blog_single_view(request, pk):
    post = Blog.objects.get(id=pk)
    if request.method == "POST":
        data = request.POST
        name = data.get("name")
        email = data.get("email")
        website = data.get("website")
        message = data.get("message")
        obj = Comment.objects.create(name=name, email=email, website=website, message=message, post=post)
        obj.save()
        return redirect(f'/blog/{pk}/')

    comments = Comment.objects.filter(post=post.id)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'blog-single.html', context)


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    if request.method == "POST":
        data = request.POST
        full_name = data.get("full_name")
        subject = data.get("subject")
        email = data.get('email')
        message = data.get("message")
        obj = Contact.objects.create(full_name=full_name, subject=subject, email=email, message=message)
        obj.save()
        return redirect('/contact')
    return render(request, 'contact.html')
