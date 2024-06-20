from django import forms
# from .models import Account


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

#
# # from django import forms
# # from .models import Account
#
# class AccountForm(forms.ModelForm):
#     class Meta:
#         model = Account
#         fields = ('first_name', 'last_name', 'gender', 'address', 'birth')

# class ContactUsForm(forms.Form):
#     message= forms.CharField(widget=forms.Textarea, required=)