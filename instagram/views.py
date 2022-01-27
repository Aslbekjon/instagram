from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import transaction
from django.template import context

from instagram.models.stream import Stream
from instagramUser.models import Profile, Following, following
from instagram.models import Post
# Create your views here.

@login_required(login_url='user_login')
def index(request):
    user = request.user
    posts = Stream.objects.filter(user=user)

    group_ids = []

    for post in posts:
        group_ids.append(post.post_id)
    
    post_items = Post.objects.filter(id__in = group_ids).all().order_by('-created_at')
    context = {
        'post_items':post_items
    }
    return render(request, 'index.html', context)

@login_required(login_url='user_login')
def profile(request, username):
    prof = Profile.objects.get(username=username)
    profile_posts = Post.objects.filter(profile=prof)

    #follow
    following_count = Following.objects.filter(follower=prof).count()
    follower_count = Following.objects.filter(following=prof).count()
    follow_status = Following.objects.filter(following=prof, follower=request.user).exists()
    
    context = {
        "profile":prof,
        "profile_posts":profile_posts,
        "follow_status":follow_status,
        "following_count":following_count,
        "follower_count":follower_count
    }
    return render(request, "profile.html", context)

@login_required(login_url='user_login')
def follow(request, username, option):
    user = request.user
    following = get_object_or_404(Profile, username=username)

    try:
        f, created = Following.objects.get_or_create(follower=user, following=following)

        if int(option) == 0:
            f.delete()
            Stream.objects.filter(following=following,user=user).all().delete()
        else:
            posts = Post.objects.all().filter(profile=following)[:10]

            with transaction.atomic():
                for post in posts:
                    stream = Stream(post=post, user=user, date=post.created_at, following=following)
                    stream.save()
        return HttpResponseRedirect(reverse('profile', args=[username]))
    except Profile.DoesNotExist:
        return HttpResponseRedirect(reverse('profile', args=[username]))

