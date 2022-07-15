from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter
router.register('projects', views.ProjectViewSet, basename='projects')

urlpatterns = [
    path('', include(router.urls))
]
