from django.urls import include, path
from blogger.views import blogger, member, legendary


# app_name = 'blogger'
urlpatterns = [
    path('', blogger.home, name='home'),

    path('member/', include(([
        path('', member.details, name='member-detail'),
    ], 'blogger'), namespace='member')),

    path('legendary/', include(([
        path('', legendary.dashboard, name='legendary-dashboard'),
        path('post/<int:pk>', legendary.PostDetailView.as_view(), name='detail-post'),
        path('post/new', legendary.PostCreateView.as_view(), name='create-post'),
        path('post/<int:pk>/update/', legendary.PostUpdateView.as_view(), name='update-post'),
    ], 'blogger'), namespace='legendary')),

]
