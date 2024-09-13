from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from booking import views

urlpatterns = [
    path('', views.add_booking, name='add_booking')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


