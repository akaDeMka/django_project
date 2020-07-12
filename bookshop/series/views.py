from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy

from .forms import CreateSeriesForm
from .models import Series
class CreateSeries(CreateView):
    template_name = 'series_edit.html'
    model = Series
    form_class = CreateSeriesForm
    success_url = reverse_lazy("series:list")
class ViewSeries(ListView):
    template_name = 'series_list.html'
    model = Series
    paginate_by = 100
class EditSeries(UpdateView):
    template_name = 'series_edit.html'
    model = Series
    success_url = reverse_lazy("series:list")
    form_class = CreateSeriesForm
class DeleteSeries(DeleteView):
    success_url = reverse_lazy("series:list")
    model = Series
    template_name = 'series_delete.html'
class DetailSeries(DetailView):
    template_name = 'series_detail.html'
    model = Series
    success_url = reverse_lazy("series:list")
    form_class = CreateSeriesForm
    

# Create your views here.
