from django import forms
from .models import Demand_survey, Career, Contact


Resident = (
    ('SLUM', 'slum'),
    ('UNAUTHORISED COLONY', 'Unauthorised Colony'),
    ('OTHER', 'other'),
)


OR = (
    ('OWNED', 'owned'),
    ('RENTED', 'rented'),
)


Dwelling = (
    ('EWS', 'ews'),
    ('LIG', 'lig'),
    ('MIG', 'mig'),
    ('HIG', 'hig'),
)


class DemandSurveyForm(forms.ModelForm):
    dob = forms.DateField(help_text='Required. Format: YYYY-MM-DD', widget=forms.TextInput(attrs={'placeholder':'DOB', 'class':'form-control', 'style':'width:200px'}))
    address = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Address', 'class':'form-control', 'style':'width:200px'}))
    fullname = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Fullname', 'class':'form-control', 'style':'width:200px'}))
    father_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Father/Husband Name', 'class':'form-control', 'style':'width:200px'}))
    occupation = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder':'Occupation', 'class':'form-control', 'style':'width:200px'}))
    choice_city = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter 4 most prefered cities of your choice in Desending order', 'class':'form-control', 'style':'width:200px;resize:none'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder':'E-Mail', 'class':'form-control', 'style':'width:200px'}))
    phone = forms.IntegerField(required=True, max_value=9999999999, widget=forms.NumberInput(attrs={'placeholder':'Mobile Number', 'class':'form-control', 'style':'width:200px'}))
    aadhar_no = forms.IntegerField(required=True, max_value=9999999999, widget=forms.NumberInput(attrs={'placeholder':'Mobile Number', 'class':'form-control', 'style':'width:200px'}))
    resident = forms.ChoiceField(choices=Resident, required=True, widget=forms.Select(attrs={'class':'dropdown-item', 'style':'width:200px'}))
    owned_rent = forms.ChoiceField(choices=OR, required=True, widget=forms.Select(attrs={'class':'dropdown-item', 'style':'width:200px'}))
    dwelling = forms.ChoiceField(choices=Dwelling, required=True, widget=forms.Select(attrs={'class':'dropdown-item', 'style':'width:200px'}))


    def clean_email(self):
        mail = self.cleaned_data['email']
        try:
            match = Demand_survey.objects.get(email__iexact=mail)
        except:
            return mail
        raise forms.ValidationError("Email already exists.")

    def clean_phone(self):
        m_num = self.cleaned_data['phone']
        try:
            match = Demand_survey.objects.get(phone__iexact = m_num)
        except:
            return m_num
        raise forms.ValidationError('Mobile Number already exist...Try Again!')

    class Meta:
        model = Demand_survey
        fields = (
                  'aadhar_no',
                  'fullname',
                  'father_name',
                  'dob',
                  'occupation',
                  'email',
                  'phone',
                  'resident',
                  'owned_rent',
                  'address',
                  'dwelling',
                  'choice_city',
                  )


class CareerForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Fullname', 'class': 'form-control', 'style': 'width:200px'}))
    phone = forms.IntegerField(required=True, max_value=9999999999, widget=forms.NumberInput(attrs={'placeholder': 'Mobile Number', 'class': 'form-control', 'style': 'width:200px'}))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'E-Mail', 'class': 'form-control', 'style': 'width:200px'}))
    question = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter your query here...', 'class':'form-control', 'style':'width:200px;resize:none'}))
    cv = forms.FileField(required=True)

    class Meta:
        model = Career
        fields = (
                  'name',
                  'email',
                  'phone',
                  'question',
                  'cv',
                 )


class ContactForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control', 'style': 'width:200px'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Message', 'class': 'form-control', 'style': 'width:200px'}))
    message = forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Enter your query here...', 'class':'form-control', 'style':'width:200px;resize:none'}))
    phone = forms.IntegerField(required=True, max_value=9999999999, widget=forms.NumberInput(attrs={'placeholder': 'Mobile Number', 'class': 'form-control', 'style': 'width:200px'}))

    class Meta:
        model = Contact
        fields = (
                  'name',
                  'phone',
                  'subject',
                  'message',
                 )
