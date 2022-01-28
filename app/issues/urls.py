from django.urls import path
from issues import views as issue_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/issues/index/', issue_views.index),
    # path('', issue_views.index.as_view(), name='issues'),
    path('api/issues/', issue_views.issue_list),
    path('api/issues/<int:pk>/', issue_views.issue_detail),
    path('api/issues/open/', issue_views.issue_list_open)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
