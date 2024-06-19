from __future__ import unicode_literals
from django.views.generic import ListView
from .models import Post, Account
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AccountForm


def postlist(request):
    posts = Post.objects.filter(status='published')
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'posts': posts, 'page': page})


def index(request):
    return HttpResponse('سلام')


# class PostListView(ListView):
#     model = Post
#     queryset = Post.objects.filter(status='published')
#     context_object_name = "posts"
#     paginate_by = 2
#     template_name = 'blog/post/list.html'


def postdetail(request, post, pk):
    post = get_object_or_404(Post, slug=post, id=pk)
    return render(request, 'blog/post/detail.html', {'post': post})


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
            # Create a new form instance with the invalid data
            form = AccountForm(request.POST)
            # Re-render the form with the invalid data
            return render(request, 'blog/forms/accountform.html', {'form': form, 'account':account})

    else:
        form = AccountForm(initial={'first_name': user.first_name, 'last_name': user.last_name, 'gender': account.gender, 'address': account.address, 'birth': account.birth})
    return render(request, 'blog/forms/accountform.html', {'form': form,'account':account})
