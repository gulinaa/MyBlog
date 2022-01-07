from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from blog_api import settings
from main.views import CategoryListView, PostsViewSet, PostImageView

router = DefaultRouter()
router.register('posts', PostsViewSet)

"""
create -> posts/POST
list -> posts/GET
retrieve -> posts/id/PUT
partial_update -> posts/id/PATCH
destroy -> posts/id/DELETE
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('v1/api/categories/', CategoryListView.as_view()),
    path('v1/api/add-image/', PostImageView.as_view()),
    path('v1/api/account/', include('account.urls')),
    path('v1/api/', include(router.urls)),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
