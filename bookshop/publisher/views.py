from django.views.generic import CreateView, UpdateView, ListView, DeleteView, DetailView
from django.urls import reverse_lazy

from .forms import CreatePublisherForm
from .models import Publisher
class CreatePublisher(CreateView):
    template_name = 'publisher_edit.html'
    model = Publisher
    form_class = CreatePublisherForm
    success_url = reverse_lazy("publisher:list")
class ViewPublishers(ListView):
    template_name = 'publisher_list.html'
    model = Publisher
    paginate_by = 100
class EditPublisher(UpdateView):
    template_name = 'publisher_edit.html'
    model = Publisher
    success_url = reverse_lazy("publisher:list")
    form_class = CreatePublisherForm
class DeletePublisher(DeleteView):
    success_url = reverse_lazy("publisher:list")
    model = Publisher
    template_name = 'publisher_delete.html'
class DetailPublisher(DetailView):
    template_name = 'publisher_detail.html'
    model = Publisher
    success_url = reverse_lazy("publisher:list")
    form_class = CreatePublisherForm
    
