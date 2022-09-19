from rest_framework import routers
from .views import PersonaViewsets

router = routers.DefaultRouter()
router.register('persona', PersonaViewsets)

from django.urls import path, include

urlpatterns = [
    path('api/', include(router.urls)),
]