
from django.views.generic import ListView
from .models import Carousel, Marketing, Feature

class ViewMain(ListView):
    template_name = 'main.html' 
    model=Carousel
    #queryset = Carousel.objects.all()

    def get_context_data(self, **kwargs):
        context = super(ViewMain, self).get_context_data(**kwargs)
        context.update({
            'marketing_list': Marketing.objects.all(),
            'features_list': Feature.objects.all(),
        })
        return context
# Create your views here.
