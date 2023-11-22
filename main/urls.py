from django.urls import path

from main.views import applications, application_delete, application_create

app_name = 'products'

urlpatterns = [
    path('', applications, name='index'),
    path('<int:category_id>/', applications, name='category'),
    path('page/<int:page>/', applications, name='page'),
    path('application_delete/<int:id>/', application_delete, name='application_delete'),
    path('application_create/', application_create, name='application_create'),
]