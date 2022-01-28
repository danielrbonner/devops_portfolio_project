from django.urls import path
from tasks import views as task_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('api/tasks/index/', task_views.index),
    # path('', task_views.index.as_view(), name='tasks'),
    path('api/tasks/', task_views.task_list),
    path('api/tasks/<int:pk>/', task_views.task_detail),
    path('api/tasks/open/', task_views.task_list_open)
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
