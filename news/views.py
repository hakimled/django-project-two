from django.shortcuts import render , redirect , get_object_or_404
from django.contrib.auth.models import User
from .models import Group  , Group_member
from django.http import HttpResponseRedirect



def greet(request):
    group= Group.objects.get(id=1)
    new_member = Group_member.objects.get()
    new = Group_member.objects.get
    print("created"  ,  group)
    
    
    
    
def add_member(request):
    members = Group_member.objects.filter(group_id=2).order_by('-id')
    context = {'members': members}
    
    if request.method == 'POST':
        user = request.user
        group = Group.objects.get(id=2)
        new = Group_member(group_id =group, member= user)
        new.save()
        return HttpResponseRedirect('/news/create/')
    else:
        return render(request, 'news/greet.html' , context )

    




def news(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']  
        user = User.objects.create_user( username=username, email=email , password=password , is_active=True , is_staff=True , is_superuser= True) 
        user.save()
        return redirect('/')    
    return render(request, 'news/news.html')

def news_detail(request, news_id):
    news_detail = get_object_or_404(Group , pk=news_id)
    context = {'news': news_detail}
    
    return render(request, 'news/detail.html'  , context)