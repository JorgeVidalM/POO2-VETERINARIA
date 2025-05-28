from django.contrib import admin
from .models import Mascota
from .models import Dueno
from.models import Especie



admin.site.register(Mascota)
admin.site.register(Dueno)
admin.site.register(Especie)