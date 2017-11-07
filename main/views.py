from django.shortcuts import render, redirect
from .forms import DemandSurveyForm, CareerForm, ContactForm
from .models import  *
import datetime
from django.utils.timezone import utc

def index(request):
    return render(request, 'main/index.html')


def home(request):
    now = datetime.datetime.now()
    # now = datetime.datetime.now().strftime('%H:%M:%S')
    # career =  Career.objects.all()
    num_visit = request.session.get('num_visit', 1)
    request.session['num_visit'] = num_visit + 1
    return render(request, 'main/home.html', {'num':num_visit, 'now':now})


def demand_survey(request):
    if request.method == 'POST':
        form = DemandSurveyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = DemandSurveyForm()
    return render(request, 'main/demand_survey.html', {'form':form})


def apply_now(request):
    member = Apply_Now.objects.all()
    return render(request, 'main/apply_now.html', {'member':member})


def about(request):
    return render(request, 'main/about.html')


def project(request):
    return render(request, 'main/project.html')


def tender(request):
    ten = Tender.objects.all()
    return render(request, 'main/tender.html', {'ten':ten})


def tender_archieved(request):
    ten_ar = Tender_Archieved.objects.all()
    return render(request, 'main/tender_archieved.html', {'ten_ar':ten_ar})


def blacklisted(request):
    black = Blacklisted.objects.all()
    return render(request, 'main/blacklisted.html', {'black':black})


def career(request):
    oppo = Opportunity_Management.objects.all()
    if request.method == 'POST':
        form = CareerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('career')
    else:
        form = CareerForm()
    return render(request, 'main/career.html', {'form':form, 'oppo':oppo})



def event(request):
    return render(request, 'main/event.html')

def introduction(request):
    return render(request, 'main/about/introduction.html')

def about_org(request):
    return render(request, 'main/about/about_org.html')

def hfa_sym(request):
    return render(request, 'main/hfa_sym.html')

def disclaimer(request):
    return render(request, 'main/footer/disclaimer.html')

def terms(request):
    return render(request, 'main/footer/terms.html')

def rad_2017(request):
    eve = Event.objects.get(name='RAD 2017')
    return render(request, 'main/rad_2017.html', {'eve':eve})

def cmd_msg(request):
    return render(request, 'main/cmd_msg.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'main/contact.html', {'form':form})
