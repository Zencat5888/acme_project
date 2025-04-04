from django.contrib import admin

# Из модуля models импортируем модель Category...
from .models import Tag
from .models import Birthday

# ...и регистрируем её в админке:
admin.site.register(Tag)
admin.site.register(Birthday)
