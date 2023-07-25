from django.urls import path
from django.views.generic import TemplateView
from product.views.product import CreateProductView
from product.views.variant import VariantView, VariantCreateView, VariantEditView

app_name = "product"

urlpatterns = [
    # Variants URLs

    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(template_name='variants/create.html'), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(template_name='products/create.html'), name='create.product'),
    path('list/', TemplateView.as_view(template_name='products/list.html', extra_context={
        'product': True
    }), name='list.product'),

]
