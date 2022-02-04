from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.db import transaction
from django.template import context
from instagram.models.like import Like

from instagram.models.stream import Stream
from instagramUser.models import Profile, Following, following
from instagram.models import Post, Post_detail, post, Comment

# Create your views here.
@login_required(login_url='user_login')
def like(request):
    user = request.user
    post_id = request.POST.get('post')
    post = Post.objects.get(id=post_id)
    current_likes = post.like
    liked = Like.objects.filter(user=user, post=post).count()
    son1 = request.POST.get('son')
    if not liked:
        post_like = 0
        if son1 != '0':
            print("1-ishlayapdi")
            like = Like.objects.create(user=user, post=post)
            current_likes = current_likes + 1
            post_like = 1
    else:
        post_like = 1
        if son1 != '0':
            print("2-ishlayapdi")
            Like.objects.filter(user=user, post=post).delete()
            current_likes = current_likes - 1
            post_like = 0
    post.like = current_likes
    print(type(son1), "llllllll",post_like)
    post.save()

    return render(request, "like.html", {'post':post, 'post_like':post_like, 'current_likes':current_likes})

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
def story_modal(request):
    click_id = request.POST.get('click_id')
    post = Post.objects.get(id=click_id)
    rasm = Like.objects.filter(post=post).order_by("id")[:3]
    d = len(rasm)
    if d>=3:
        rasm1 = rasm[0]
        rasm2 = rasm[1]
        rasm3 = rasm[2]
    elif d==2:
        rasm1 = rasm[0]
        rasm2 = rasm[1]
        rasm3 = 0
    elif d==1:
        rasm1 = rasm[0]
        rasm2=0
        rasm3=0
    else:
        rasm1=0
        rasm2=0
        rasm3=0
    print(len(rasm), "lllllllllllllllllllll")
    return render(request, "story-modal.html", {"post":post, "rasm1":rasm1, "rasm2":rasm2, "rasm3":rasm3})

# comment
@login_required(login_url='user_login')
def commentList(request):
    post_id = request.POST.get('post')
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        text = request.POST.get('comment')
        if text:
            form_comment = Comment()
            form_comment.text=text
            form_comment.profile=request.user
            form_comment.post=post
            form_comment.save()
    comments = post.comment_set.all().order_by("-id")
    return render(request, "commentlist.html", {"comments":comments})

# profile
@login_required(login_url='user_login')
def profile(request, username):
    prof = Profile.objects.get(username=username)
    profile_posts = Post.objects.filter(profile=prof)

    #follow
    following_count = Following.objects.filter(follower=prof).count()
    follower_count = Following.objects.filter(following=prof).count()
    follow_status = Following.objects.filter(following=prof, follower=request.user).exists()

    #post
    post_detail = Post_detail.objects.filter(kirib_turgan=request.user.username).exists()
    
    context = {
        "profile":prof,
        "profile_posts":profile_posts,
        "follow_status":follow_status,
        "following_count":following_count,
        "follower_count":follower_count,
        "post_detail":post_detail
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

