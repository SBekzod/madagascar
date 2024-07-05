from django.contrib import admin
from django.urls import path, include

from goal.views import (home_view)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', home_view),
    path('', include('goal.urls'))
]
