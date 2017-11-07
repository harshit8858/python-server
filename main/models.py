from django.db import models


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


class Demand_survey(models.Model):
    aadhar_no = models.IntegerField()
    fullname = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30)
    dob = models.DateField()
    occupation = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    resident = models.CharField(default='slum', max_length=10, choices=Resident)
    owned_rent = models.CharField(max_length=10, choices=OR)
    address = models.CharField(max_length=100)
    dwelling = models.CharField(max_length=10, choices=Dwelling)
    choice_city = models.TextField(max_length=50)

    def __str__(self):
        return self.fullname


class Career(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.IntegerField()
    question = models.TextField(max_length=200)
    cv = models.FileField(upload_to='media')

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=30)
    phone = models.IntegerField()
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=200)

    def __str__(self):
        return self.subject


# from django.contrib.gis.db import models
# from django.contrib.gis.geos import Point
# from location_field.models.spatial import LocationField
#
# class Place(models.Model):
#     city = models.CharField(max_length=255)
#     location = LocationField(based_fields=['city'], zoom=7, default=Point(1.0, 1.0))
#     objects = models.GeoManager()

class Tender(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=40)
    dept = models.CharField(max_length=40)
    last_date = models.DateField(blank=True, null=True)
    doc = models.FileField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name


class Tender_Archieved(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=40)
    dept = models.CharField(max_length=40)
    last_date = models.DateField(blank=True, null=True)
    doc = models.FileField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name


class Apply_Now(models.Model):
    file = models.FileField(upload_to='media', blank=True, null=True)


class Opportunity_Management(models.Model):
    file = models.FileField(upload_to='media', blank=True, null=True)


class Event(models.Model):
    name = models.CharField(max_length=100)
    event = models.FileField(upload_to='media', null=True, blank=True)

    def __str__(self):
        return self.name


class Blacklisted(models.Model):
    list = models.FileField(upload_to='media', null=True, blank=True)