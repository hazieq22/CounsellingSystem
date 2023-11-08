from django.contrib import admin

# Register your models here.
from .models import Student,Counsellor,Session,Detail

admin.site.register(Counsellor)
admin.site.register(Student)
admin.site.register(Session)
admin.site.register(Detail)