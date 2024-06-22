from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from .models import Post, Account, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AccountForm, ContactUsForm, CommentForm
from django.core.mail import send_mail
from django.contrib import messages
from taggit.models import Tag
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank, TrigramSimilarity


def postlist(request, tag_slug=None):
    posts = Post.objects.filter(status='published')
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 2)  # Show 2 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'page': page,
        'tag': tag
    }

    return render(request, 'blog/post/list.html', context)


def index(request):
    return HttpResponse('سلام')


def postdetail(request, slug, pk, post=None):
    if post is None:
        post = get_object_or_404(Post, status='published', slug=slug, id=pk)
    comments = post.comment_set.filter(published="Published")
    new_comment = None
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.user = request.user
            new_comment.save()
            messages.success(request, 'کامنت شما با موفقیت ارسال شد.')
            return redirect('blog:post_detail', slug=post.slug, pk=post.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'blog/post/detail.html',
                  {'post': post, 'comments': comments, "new_comment": new_comment, 'comment_form': comment_form, })


def useraccount(request):
    user = request.user
    try:
        account = Account.objects.get(user=user)
    except Account.DoesNotExist:
        account = Account.objects.create(user=user)
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            account.gender = form.cleaned_data['gender']
            account.address = form.cleaned_data['address']
            account.birth = form.cleaned_data['birth']

            user.save()
            account.save()
            return redirect('blog:index')
        else:
            form = AccountForm(request.POST)
            return render(request, 'blog/forms/accountform.html', {'form': form, 'account': account})
    else:
        form = AccountForm(
            initial={'first_name': user.first_name, 'last_name': user.last_name, 'gender': account.gender,
                     'address': account.address, 'birth': account.birth})
    return render(request, 'blog/forms/accountform.html', {'form': form, 'account': account})


def contactus(request):
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            name = cd['name']
            email = cd['email']
            subject = cd['subject']
            message = cd['message']
            phone = cd['phone']
            msg = 'نام: {0}\nموضوع: {2}\nشماره تماس: {3}\nایمیل: {1}\nپیام: {4}'.format(name, email, subject, phone,
                                                                                        message)
            send_mail(subject, msg, 'yasin.danesh@outlook.com', ['yasin.danesh@outlook.com'], fail_silently=False)
            return redirect('blog:post_list')
    else:
        form = ContactUsForm()
    return render(request, 'blog/forms/Contact-Us.html', {'form': form})


def search(request, tag_slug=None):
    query_name = request.POST.get('search_input') if request.method == "POST" else None
    posts = Post.objects.filter(status='published')
    tag = None

    if query_name:
        search_vector = SearchVector('caption', weight='B') + SearchVector('title', weight='A')
        search_query = SearchQuery(query_name)
        posts = posts.annotate(
            rank=SearchRank(search_vector, search_query),
            similarity=TrigramSimilarity('caption', query_name) + TrigramSimilarity('title', query_name)
        ).filter(similarity__gte=0.3).order_by('-similarity', '-rank')

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[tag])

    paginator = Paginator(posts, 2)  # Show 2 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts,
        'page': page,
        'tag': tag
    }

    return render(request, 'blog/post/list.html', context)