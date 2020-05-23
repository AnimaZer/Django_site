from django.contrib import admin
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new

# from .views import HomePageView, LoadDataView # new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('face_finder.urls')), # new
    # path('progress/', LoadDataView.as_view(), name='progress') # new
]

if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)