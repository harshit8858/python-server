from django.conf.urls import url
from .views import *
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^home/', home, name='home'),
    url(r'^demand_survey/', demand_survey, name='demand_survey'),
    url(r'^apply_now/', apply_now, name='apply_now'),
    url(r'^about/', about, name='about'),
    url(r'^project/', project, name='project'),
    url(r'^tender/', tender, name='tender'),
    url(r'^tender_archieved/', tender_archieved, name='tender_archieved'),
    url(r'^blacklisted/', blacklisted, name='blacklisted'),
    url(r'^career/', career, name='career'),
    url(r'^event/', event, name='event'),
    url(r'^rad_2017/', rad_2017, name='rad_2017'),
    url(r'^contact/', contact, name='contact'),
    url(r'^introduction/', introduction, name='introduction'),
    url(r'^about_org/', about_org, name='about_org'),
    url(r'^hfa_sym/', hfa_sym, name='hfa_sym'),
    url(r'^cmd_msg/', cmd_msg, name='cmd_msg'),
    url(r'^disclaimer/', disclaimer, name='disclaimer'),
    url(r'terms/', terms, name='terms')

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

