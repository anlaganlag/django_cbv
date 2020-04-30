from django.views.generic import ListView
from bookstore.models import Publisher

class PublisherList(ListView):
    model = Publisher