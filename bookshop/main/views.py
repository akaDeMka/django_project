
from django.views.generic import ListView
from .models import Carousel

class ViewMain(ListView):
    template_name = 'main.html' 
    model=Carousel
    #queryset = Carousel.objects.all()

    #def get_context_data(self, **kwargs):
        #context = super(ViewHome, self).get_context_data(**kwargs)
        #context['carousel_list'] = self.queryset
        #return context
# Create your views here.
