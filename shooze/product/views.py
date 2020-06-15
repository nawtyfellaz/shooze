from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.utils import timezone
from django.views import View
from django.views.generic import DetailView, ListView
from django.views.generic.edit import (
    CreateView,
    DeleteView,
    FormMixin,
    UpdateView
)
from datetime import datetime

from shooze.product.models import Product, Brand, Seller
from shooze.contents.models import Category, Review

# Create your views here.
class ProductList(ListView):
    model = Product
    template_name = 'product/list.html'
    ordering = '-created, title'
    quesryset = Product.objects.all_instock()
    context_object_name = 'instance'
    allow_empty = True
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        request = self.request
        context['today']   = timezone.now().date()
        context['categories'] = Category.objects.a