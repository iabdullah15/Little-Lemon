from . import views
from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()
router.register('tables', views.BookingViewSet)


urlpatterns = [
    path('', views.index, name = 'home'),
    path('items/', views.MenuItemsView.as_view()),
    path('item/<int:pk>/', views.SingleMenuItemView.as_view()),
    path('', include(router.urls)),
]