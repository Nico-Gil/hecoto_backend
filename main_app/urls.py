from django.urls import path

from rest_framework import routers


from main_app.views.views import (
    LaboratoriesViewSet
)

app_name = 'main_app'

router = routers.DefaultRouter()

router.register(r'laboratories', LaboratoriesViewSet, 'laboratories')

urlpatterns = router.urls