from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from .api import views


router = routers.DefaultRouter()


router.register(r'posts', views.PostView, 'post')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]

print(urlpatterns)
