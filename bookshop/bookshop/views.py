from django.views.generic import TemplateView
from .settings import BASE_DIR

#from .urls import urlpatterns
class ViewSite(TemplateView):
    template_name = 'bookshop_main.html'  
    print (BASE_DIR)
