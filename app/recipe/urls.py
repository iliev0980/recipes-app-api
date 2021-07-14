from django.urls import path, include
from rest_framework.routers import DefaultRouter
# from ..recipe import views
from app.recipe.views import TagViewSet

router = DefaultRouter()
router.register('tags', TagViewSet)

app_name = 'recipe'

urlpatterns = [
    path('', include(router.urls))
]