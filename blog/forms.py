from django import forms
from django.contrib.auth.models import User

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

    def clean(self):
        cleaned_data = super().clean()
        old_password = cleaned_data.get('old_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if not self.user.check_password(old_password):
            self.add_error('old_password', 'رمز قدیمی اشتباه است')
        if new_password1 != new_password2:
            self.add_error('new_password2', 'رمز های وارد شده یکسان نیستند')

        if len(new_password1) < 8:
            self.add_error('new_password1', 'رمز عبور باید حداقل 8 کاراکتر باشد')

        if not any(char.isdigit() for char in new_password1):
            self.add_error('new_password1', 'رمز عبور باید حداقل یک عدد داشته باشد')

        if not any(char.isupper() for char in new_password1):
            self.add_error('new_password1', 'رمز عبور باید حداقل یک حرف بزرگ داشته باشد')

        if not any(char.islower() for char in new_password1):
            self.add_error('new_password1', 'رمز عبور باید حداقل یک حرف کوچک داشته باشد')

        return cleaned_data


class RegisterForm(forms.Form):
    username = forms.CharField(label='نام کاربری')
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        password2 = cleaned_data.get('password2')
        if password != password2:
            self.add_error('password2', 'رمز های وارد شده یکسان نیستند')
        if password and len(password) < 8:
            self.add_error('password', 'رمز عبور باید حداقل 8 کاراکتر باشد')
        if password and not any(char.isdigit() for char in password):
            self.add_error('password', 'رمز عبور باید حداقل یک عدد داشته باشد')
        if password and not any(char.isupper() for char in password):
            self.add_error('password', 'رمز عبور باید حداقل یک حرف بزرگ داشته باشد')
        if password and not any(char.islower() for char in password):
            self.add_error('password', 'رمز عبور باید حداقل یک حرف کوچک داشته باشد')
        if User.objects.filter(username=username).exists():
            self.add_error('username', 'نام کاربری تکراری است')
        return cleaned_data

    # def clean_username(self):
    #     username = self.cleaned_data.get('username')
    #     if User.objects.filter(username=username).exists():
    #         self.add_error('username', 'نام کاربری تکراری است')
    #     return username

    def save(self, commit=True):
        user = User.objects.create_user(
            username=self.cleaned_data['username'],
            password=self.cleaned_data['password']
        )
        return user
