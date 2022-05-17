from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from . models import Post
from .forms import PostForm
from cloudinary.forms import cl_init_js_callbacks


def index(request):
   if request.method == 'POST':
      form = PostForm(request.POST, request.FILES)
      if form.is_valid():
         form.save()
         return HttpResponseRedirect('/')
      else:
         return HttpResponseRedirect(form.errors.as_json())
   posts = Post.objects.all().order_by('-created_at')[:20]

   return render(request, 'posts.html',
               {'posts':posts}) 

def delete(request, post_id):
   post1 = Post.objects.get(id=post_id)
   post1.delete()
   return HttpResponseRedirect('/')

def edit(request, post_id):
    posts = Post.objects.get(id=post_id)
    if request.method == 'GET':
        posts=Post.objects.get(id=post_id)
        return render(request, "edit.html", {"posts":posts})
    if request.method == 'POST':
        #editposts= posts.objects.get(id=post_id)
        form = PostForm(request.POST, request.FILES, instance=posts)

        # If the form is valid
        if form.is_valid():
            # yes, save
             form.save()
               
            # Redirect to Home
             return HttpResponseRedirect('/')
          
           
        else:
            # No, Show Error
            return HttpResponseRedirect('not valid')

def likes(request, id):
    Likedtweet = Post.objects.get(id=id)
    new_value = Likedtweet.like_count +1
    Likedtweet.like_count = new_value
    Likedtweet.save()
    return HttpResponseRedirect('/')









