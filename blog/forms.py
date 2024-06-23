from django import forms
from .models import Account, Comment


# class AccountForm(forms.ModelForm):
#     class Meta:
#         model = Account
#         fields = ('phone', )


class AccountForm(forms.Form):
    GENDER_CHOICES = (
        ('آقا', "آقا"),
        ('خانم', 'خانم'),
    )
    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect, label='جنسیت')
    address = forms.CharField(max_length=200, widget=forms.Textarea, label='آدرس', required=True)
    first_name = forms.CharField(max_length=15, label='نام', required=True)
    last_name = forms.CharField(max_length=15, label='نام خانوادگی', required=True)
    birth = forms.CharField(max_length=10, label='تاریخ تولد', required=True)

    # def clean(self):
    #


# from django import forms
# from .models import Account


# class AccountForm(forms.ModelForm):
#     first_name = forms.CharField(max_length=30)  # Adding User's first_name
#     last_name = forms.CharField(max_length=30)  # Adding User's last_name
#
#     class Meta:
#         model = Account
#         fields = ('first_name', 'last_name', 'gender', 'address', 'birth')
#
#     def save(self, commit=True):
#         account = super(AccountForm, self).save(commit=False)
#         account.user.first_name = self.cleaned_data['first_name']
#         account.user.last_name = self.cleaned_data['last_name']
#         if commit:
#             account.save()
#             account.user.save()
#         return account


class ContactUsForm(forms.Form):
    name = forms.CharField(label='نام و نام خانوادگی', max_length=100)
    email = forms.EmailField(label='ایمیل')
    phone = forms.CharField(label='شماره تماس', max_length=15)
    message = forms.CharField(label='پیام', widget=forms.Textarea)
    SUBJECT_CHOICES = [
        ('انتقاد و پیشنهاد', 'انتقاد و پیشنهاد'),
        ('شکایت', 'شکایت'),
    ]
    subject = forms.ChoiceField(label='موضوع', choices=SUBJECT_CHOICES)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('Comment', 'name',)


class LoginForm(forms.Form):
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)


class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='رمز قدیمی', widget=forms.PasswordInput)
    new_password1 = forms.CharField(label='رمز جدید', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='تکرار رمز جدید', widget=forms.PasswordInput)