from django.shortcuts import render,get_object_or_404,redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ServiceForm,ContactForm,SearchForm
from .models import Post,PostQuery
from django.templatetags.static import static
from io import BytesIO
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from PIL import Image
from datetime import datetime
from django.contrib.auth.models import User
from django.core.files.images import ImageFile
from django.contrib import messages
from django.core.files.images import ImageFile
# Create your views here.
def index(request):
    return render(request, "body.html")
@login_required()
def serviceHome(request):
    allPosts= Post.objects.all()
    context={'allPosts': allPosts}
    return render(request, "serviceHome.html", context)
@login_required()
def servicePost(request,slug):
    post=Post.objects.filter(slug=slug).first()
    comments=PostQuery.objects.filter(post=post,parent=None)
    replies=PostQuery.objects.filter(post=post).exclude(parent=None)
    if request.method=="POST":
        post.delete()
    replyDict={}
    for reply in replies:
        if reply.parent.sno not in replyDict.keys():
            replyDict[reply.parent.sno]=[reply]
        else:
            replyDict[reply.parent.sno].append(reply)

    context={"post":post,"comments":comments, 'user':request.user,'replyDict':replyDict}
    return render(request, "servicePost.html", context)

@login_required()
def postComment(request):
    if request.method == "POST":
        query_type = request.POST.get('comment')
        query_detail = request.POST.get('querydetail')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno')
        if parentSno=="":
            query = PostQuery(query_type=query_type,query_detail=query_detail, user=user, post=post)
            query.save()
            messages.success(request, "Your comment has been posted successfully")
        else:
            parent=PostQuery.objects.get(sno=parentSno)
            query=PostQuery(query_type=query_type,user=user,post=post,parent=parent)
            query.save()
            messages.success(request, "Your reply has been posted successfully")

    return redirect('servicePost', post.slug)


@login_required()
def serviceadd(request):

        if request.method == "POST":
            form = ServiceForm(request.POST,request.FILES)
            if form.is_valid():

                form.save(commit=True)

                if 'cover' in request.FILES:
                    form.cover=request.FILES['cover']
                form.save()

                return redirect('serviceHome')

        else:
            form = ServiceForm()

        return render(
            request, "service-form.html",
            {
                "form": form,
                "is_file_uploaded": True
            }
        )
@login_required()
def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPosts= Post.objects.filter(name__icontains=query)
    if allPosts.count() == 0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts,'query':query}
    return render(request, 'book_search.html', params)


def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_mail']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['serviceadd9977@gmail.com', from_email])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "email.html", {'form': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

def aboutUs(request):
    return render(request, "aboutUs.html")


