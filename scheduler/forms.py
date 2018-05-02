from django import forms
from .models import OrderModel
class TestForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=100)
    age = forms.IntegerField(label="Your Age")
    about_me = forms.CharField(label="About Me", max_length=300)

class RequestForm(forms.Form):
    firstName = forms.CharField(label='First Name', max_length=100)
    lastName = forms.CharField(label='Last Name', max_length=100)
    dateSubmitted = forms.DateField(label='Date Submitted (dd/mm/xxxx)')
    datePartsNeeded =  forms.DateField(label='Date Parts Needed (dd/mm/xxxx)')
    facultyAdvisor = forms.CharField(label='Professor or ASU Acct Rep that will be approving the purchase')
    paymentAccountNo = forms.IntegerField(label='ASU Acct number to be used for payment')
    className = forms.CharField(label='Class Name')
    machineRequested = forms.CharField(label='Machine Requested')
    listParts = forms.CharField(label='List of Part Names and Quantities')
    maxHeight=forms.FloatField(label='Max Height')
    minHeight=forms.FloatField(label='Min Height')
    maxLength=forms.FloatField(label='Max Length')
    minLength=forms.FloatField(label='Min Length')
    maxWidth=forms.FloatField(label='Max Width')
    minWidth=forms.FloatField(label='Min Width')

class RequestOrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = ['firstName', 'lastName', 'dateSubmitted', 'datePartsNeeded', 'facultyAdvisor', 'paymentAccountNo',
                  'className', 'machineRequested', 'listParts' ,'maxHeight','minHeight','maxLength','minLength',
                  'maxWidth','minWidth'
                  ]
        # labels = ['First Name', 'Last Name', 'Data Submitted (mm/dd/yyyy)', 'Data Parts Needed (mm/dd/yyyy)'
        #           'Professor or ASU Acct Rep that will be approving the purchase',
        #           'ASU Acct number to be used for payment'
        #           'Class Name'
        #           'Machine Requested'
        #           'List of Part Names and Quantities'
        #           ]
