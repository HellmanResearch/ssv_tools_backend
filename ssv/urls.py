
from rest_framework import routers

from devops_django import routers as dd_routers

from . import views as l_views


# router = dd_routers.CacheRouter(trailing_slash=False)
router = routers.DefaultRouter(trailing_slash=False)


# router.register("results", viewset=l_views.Result, cache_seconds=60*10)
router.register("results", viewset=l_views.Result)
router.register("deposit-key", viewset=l_views.Depositkey)

urlpatterns = router.urls
