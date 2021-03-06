from django.urls import include, path
from rest_framework import routers, urlpatterns
from . import views

router = routers.DefaultRouter()
router.register(r'projects', views.ProjectViewSet)

# Wire up our API using automatic URL Routing 
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',
    namespace='rest_framework'))
]

