
from django.conf.urls import url
from django.views.decorators.cache import cache_page

from rest_framework.routers import SimpleRouter


class CacheRouter(SimpleRouter):
    # def register(self, prefix, viewset, base_name=None, cache_seconds=0):
    #     if base_name is None:
    #         base_name = self.get_default_base_name(viewset)
    #         basename = self.get_default_basename(viewset)
    #     self.registry.append((prefix, viewset, base_name, cache_seconds))

    def register(self, prefix, viewset, basename=None, cache_seconds=0):
        if basename is None:
            basename = self.get_default_basename(viewset)
        self.registry.append((prefix, viewset, basename, cache_seconds))

        # invalidate the urls cache
        if hasattr(self, '_urls'):
            del self._urls

    def get_urls(self):
        """
        Use the registered viewsets to generate a list of URL patterns.
        """
        ret = []

        for prefix, viewset, basename, cache_seconds in self.registry:
            lookup = self.get_lookup_regex(viewset)
            routes = self.get_routes(viewset)

            for route in routes:

                # Only actions which actually exist on the viewset will be bound
                mapping = self.get_method_map(viewset, route.mapping)
                if not mapping:
                    continue

                # Build the url pattern
                regex = route.url.format(
                    prefix=prefix,
                    lookup=lookup,
                    trailing_slash=self.trailing_slash
                )

                # If there is no prefix, the first part of the url is probably
                #   controlled by project's urls.py and the router is in an app,
                #   so a slash in the beginning will (A) cause Django to give
                #   warnings and (B) generate URLS that will require using '//'.
                if not prefix and regex[:2] == '^/':
                    regex = '^' + regex[2:]

                initkwargs = route.initkwargs.copy()
                initkwargs.update({
                    'basename': basename,
                })
                if(cache_seconds):
                    view = cache_page(cache_seconds)(viewset.as_view(mapping, **initkwargs))
                else:
                    view = viewset.as_view(mapping, **initkwargs)
                name = route.name.format(basename=basename)
                ret.append(url(regex, view, name=name))

        return ret
