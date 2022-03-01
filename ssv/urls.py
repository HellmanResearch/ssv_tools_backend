
from rest_framework import routers

from . import views as l_views

router = routers.DefaultRouter(trailing_slash=False)


router.register("results", viewset=l_views.Result)

urlpatterns = router.urls
