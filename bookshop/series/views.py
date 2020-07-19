from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .forms import CreateSeriesForm
from .models import Series
class CreateSeries(PermissionRequiredMixin,CreateView):
    permission_required = 'series.add_series'
    template_name = 'series_edit.html'
    model = Series
    form_class = CreateSeriesForm
    success_url = reverse_lazy("series:list")
class ViewSeries(PermissionRequiredMixin,ListView):
    permission_required = 'series.view_series'
    template_name = 'series_list.html'
    model = Series
    paginate_by = 100
class EditSeries(PermissionRequiredMixin,UpdateView):
    permission_required = 'series.change_series'
    template_name = 'series_edit.html'
    model = Series
    success_url = reverse_lazy("series:list")
    form_class = CreateSeriesForm
class DeleteSeries(PermissionRequiredMixin,DeleteView):
    permission_required = 'series.delete_series'
    success_url = reverse_lazy("series:list")
    model = Series
    template_name = 'series_delete.html'
class DetailSeries(PermissionRequiredMixin,DetailView):
    permission_required = 'series.view_series'
    template_name = 'series_detail.html'
    model = Series
    success_url = reverse_lazy("series:list")
    form_class = CreateSeriesForm
    

# Create your views here.
