
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Ardas_Interior_App.urls'))
]
