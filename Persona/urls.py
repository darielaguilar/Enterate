from django.urls import path, include
from rest_framework.routers import DefaultRouter
from Persona import views

router = DefaultRouter()
router.register('Persona-viewset', views.PersonaViewSet, basename='Persona-viewset')
router.register('model-viewset',views.PersonaModelViewSet)
urlpatterns = [
    path('rest-view',views.PersonaAPIView.as_view()),
    path('', include(router.urls))
]

