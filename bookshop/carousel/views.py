from .models import Carousel
# Create your views here.
from django.views.generic import ListView

class ViewSite(ListView):
    model=Carousel
    template_name = 'carousel.html'  