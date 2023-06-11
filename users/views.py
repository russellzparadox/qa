from django.shortcuts import render,redirect,HttpResponse,get_object_or_404
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy,reverse
from . import models
from .forms import question_form

def BlogPostLike(request, pk):
    post = get_object_or_404(models.Question, id=request.POST.get('blogpost_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)

    return HttpResponseRedirect(reverse('blogpost-detail', args=[str(pk)]))


def home(request):
    if request.method == 'POST':
        q = models.Question.objects.get(pk=request.POST.get('q_id'))
        q.like.add(request.user)
        return redirect('/')
    else:
        allQ = models.Question.objects.all()
        allQ = sorted(allQ, key=lambda x:x.tootal_likes(),reverse=True)

        return render(request,'home.html',context={'questions':allQ,'user':request.user})
def logout_view(request):
    logout(request)
    return redirect('/')
def likeView(request):
    usr = request.user
    if request.method == 'POST':
        q_id = request.POST.get('q_id')
        q = models.Question.objects.get(id=q_id)
        if usr in q.like.all():
            q.like.remove(usr)
            pass
        else:
            q.like.add(usr)
        return redirect('/')            



def add_question(request):
    if request.method == "GET":
        form = question_form()
        return render(request, 'addQuestion.html', {'form': form})
    if request.method == "POST":
        txt = request.POST.get('text')
        q = models.Question(body=txt)
        q.save()
        return redirect('/')

def index(request):
    if request.method == "GET":
        allQ = models.Question.objects.all().order_by("-like_num")
        return render(request,'index.html',context={'questions':allQ})
        pass
        
    
    return HttpResponse()