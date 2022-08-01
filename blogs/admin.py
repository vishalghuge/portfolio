from django.contrib import admin
from .models import *
# Register your models here.

all_models = [Posts, Tags]

admin.site.register(all_models)