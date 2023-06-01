# coding: utf-8
from home.models import Contact
Contact.objects.all
Contact.objects.all()
Contact.objects.all()
Contact.objects.all()[0].name
Contact.objects.all()[0].phone
Contact.objects.filter(name="Abhinav gupta")
Contact.objects.filter(name="Abhinav")
Contact.objects.filter(name="abhinav gupta")
ins=Contact.objects.filter(name="Abhinav gupta")
ins.desc="i know very much about django fundamentals"
ins.save()
ins.save()
Contact.objects.filter(name="Abhinav gupta")
Contact.objects.all()[0].desc
ins.save()
help
help()
Contact.objects.all()[0].desc
ins.save()
