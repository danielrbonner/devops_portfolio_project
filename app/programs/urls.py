from django.urls import path
from programs import views as programs_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    #path('', programs_views.index, name='home'),
    path('', programs_views.index.as_view(), name='home'),
    path('api/programs/', programs_views.program_list),
    path('api/programs/<int:pk>/', programs_views.program_detail),
    path('api/programs/open/', programs_views.program_list_open)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)