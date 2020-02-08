from django.urls import path

from adminx.views import index_view

app_name = 'adminx'

urlpatterns = [
    path('', index_view, name='index')
]
