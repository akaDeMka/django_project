from django.views.generic import ListView
from carousel.models import Carousel
class ViewHome(ListView):
    template_name = 'home.html' 
    context_object_name = 'name' 
    model=Carousel
    #queryset = Carousel.objects.all()

    #def get_context_data(self, **kwargs):
    #    context = super(ViewHome, self).get_context_data(**kwargs)
    #    context['carousel_list'] = self.queryset
    #    return context
