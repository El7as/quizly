from django.contrib import admin

from .models import Question, Quiz, Option
# Register your models here.


admin.site.register(Question)
admin.site.register(Quiz)
admin.site.register(Option)