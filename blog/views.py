from django.views.generic import ListView
from .models import Post, Account
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import AccountForm, ContactUsForm
from django.core.mail import send_mail


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
            form = AccountForm(request.POST)
            return render(request, 'blog/forms/accountform.html', {'form': form, 'account': account})
    else:
        form = AccountForm(initial={'first_name': user.first_name, 'last_name': user.last_name, 'gender': account.gender, 'address': account.address, 'birth': account.birth})
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
            msg = 'نام: {0}\nموضوع: {2}\nشماره تماس: {3}\nایمیل: {1}\nپیام: {4}'.format(name, email, subject, phone, message)
            send_mail(subject, msg, 'yasin.danesh@outlook.com', ['yasin.danesh@outlook.com'], fail_silently=False)
            return redirect('blog:post_list')
    else:
        form = ContactUsForm()
    return render(request, 'blog/forms/Contact-Us.html', {'form': form})
