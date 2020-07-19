from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from .forms import CreatePublisherForm
from .models import Publisher
class CreatePublisher(PermissionRequiredMixin,CreateView):
    permission_required = 'publisher.add_publisher'
    template_name = 'publisher_edit.html'
    model = Publisher
    form_class = CreatePublisherForm
    success_url = reverse_lazy("publisher:list")
class ViewPublishers(PermissionRequiredMixin,ListView):
    permission_required = 'publisher.view_publisher'
    template_name = 'publisher_list.html'
    model = Publisher
    paginate_by = 100
class EditPublisher(PermissionRequiredMixin,UpdateView):
    permission_required = 'publisher.change_publisher'
    template_name = 'publisher_edit.html'
    model = Publisher
    success_url = reverse_lazy("publisher:list")
    form_class = CreatePublisherForm
class DeletePublisher(PermissionRequiredMixin,DeleteView):
    permission_required = 'publisher.delete_publisher'
    success_url = reverse_lazy("publisher:list")
    model = Publisher
    template_name = 'publisher_delete.html'
class DetailPublisher(PermissionRequiredMixin,DetailView):
    permission_required = 'publisher.view_publisher'
    template_name = 'publisher_detail.html'
    model = Publisher
    success_url = reverse_lazy("publisher:list")
    form_class = CreatePublisherForm
    
