
from django.views.generic import ListView
from .models import Carousel, Marketing
from book.models import Book
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class ViewMain(ListView):
    template_name = 'main.html' 
    model=Carousel

    def get_context_data(self, **kwargs):
        context = super(ViewMain, self).get_context_data(**kwargs)
        context.update({
            'marketing_list': Marketing.objects.all(),
            'last_books': Book.objects.order_by("-id")[0:3],
        })
        return context


class ViewStaffPage(ListView):
    template_name = 'staff_page.html'
    model=Carousel
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_staff:
            messages.error(
                request,
                'You do not have the permission required to perform the '
                'requested operation.')
            return redirect(settings.LOGIN_URL)
        return super(ViewStaffPage, self).dispatch(request,
            *args, **kwargs)


