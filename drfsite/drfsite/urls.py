from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from women.views import *

# from rest_framework import routers


# class MyCustomRouter(routers.SimpleRouter):
# class MyCustomRouter(SimpleRouter):
#     routes = [
#         Route(
#             url=r'^{prefix}$',
#             mapping={'get': 'list'},
#             name='{basename}-list',
#             detail=False,
#             initkwargs={'suffix': 'List'}
#         ),
#         Route(
#             url=r'^{prefix}/{lookup}$',
#             mapping={'get': 'retrieve'},
#             name='{basename}-detail',
#             detail=True,
#             initkwargs={'suffix': 'Detail'}
#         ), ]


# router = MyCustomRouter()
# router = routers.SimpleRouter()
# router = routers.DefaultRouter()

# router.register(r'women', WomenViewSet, basename='women')
# print(router.urls)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/drf-auth/', include('rest_framework.urls')),
    path('api/v1/women/', WomenAPIList.as_view()),
    path('api/v1/women/<int:pk>/', WomenAPIUpdate.as_view()),
    path('api/v1/women-delete/<int:pk>', WomenAPIDestroy.as_view()),

    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

# path('api/v1/', include(router.urls))

# path('api/v1/women_list/', WomenAPIList.as_view()),
# path('api/v1/women_list/<int:pk>/', WomenAPIUpdate.as_view()),
# path('api/v1/women_detail/<int:pk>/', WomenAPIDetailView.as_view()),

# path('api/v1/women_list/', WomenViewSet.as_view({'get': 'list'})),
# path('api/v1/women_list/<int:pk>/', WomenViewSet.as_view({'put': 'update'})) ,

