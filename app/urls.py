from django.urls import path
from .views import home_view, blog_view, about_view, contact_view, blog_single_view

urlpatterns = [
    path('', home_view),
    path('blog/', blog_view),
    path('blog/<int:pk>/', blog_single_view),
    path('about/', about_view),
    path('contact/', contact_view),
]
