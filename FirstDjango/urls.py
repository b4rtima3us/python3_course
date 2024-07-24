from MainApp import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.render_main, name='main'),
    path('about/', views.render_about, name='about'),
    path('items/', views.render_items, name='items'),
    path('items/<int:item_id>/', views.render_item_by_id, name='item_id'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
