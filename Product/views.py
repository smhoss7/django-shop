from django.db.models import Sum, Avg
from django.db.models.functions.text import Lower
from django.http import Http404
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView

from Product.models import Product, Category, Brand


# Create your views here.

# def products(request):
#     products = Product.objects.all().order_by(Lower('name'))
#     print('okay')
#     rate=products.aggregate(Avg('rating'))
#     context = {'products': products,
#                'rate':rate}
#     return render(request,'Product/product_list.html',context)

class products(ListView):
    model = Product
    template_name = 'Product/product_list.html'
    paginate_by = 2

    def get_queryset(self):
        queryset = Product.objects.all().filter(is_published=True)
        category_slug = self.kwargs.get('cat', None)
        brand_slug = self.kwargs.get('brand', None)
        if category_slug is not None:
            category_obj = Category.objects.get(slug=category_slug)
            queryset = queryset.filter(category=category_obj)
        if brand_slug is not None:
            brand_obj = Brand.objects.get(slug=brand_slug)
            queryset = queryset.filter(brand=brand_obj)
        return queryset


class product_details(DetailView):
    model = Product
    template_name = 'Product/product_detail.html'


class AddToBuy(View):
    def post(self, request):
        product_id = int(request.POST['product_id'])
        product = Product.objects.get(pk=product_id)


# def product_details(request, slug):
#     try:
#         product = Product.objects.get(slug=slug)
#     except:
#         raise Http404()
#     context = {'product': product}
#     return render(request,'Product/product_detail.html',context)


def product_category(request):
    category_list = Category.objects.all()
    return render(request, 'Product/category.html', {'category_list': category_list})

def product_brands(request):
    brand_list = Brand.objects.all()
    return render(request, 'Product/brand.html', {'brand_list': brand_list})
