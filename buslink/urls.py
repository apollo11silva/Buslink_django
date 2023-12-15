#C:\Users\gau_m\OneDrive\Documentos\projetos_python\buslink_django\buslink\urls.py
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('principal.urls')),

]
