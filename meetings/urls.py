from django.urls import path
from django.views.generic import TemplateView

app_name = 'meetings'

urlpatterns = [
    path('', TemplateView.as_view(template_name='meetings/index.html')),
]
