from email.policy import default

from django.conf import settings
from django.utils.translation import gettext as _


def get_setting(name: str, default=None):
    return getattr(settings, "WAGTAIL_STOCK_IMAGES_%s" % name, default)


MENU_LABEL = get_setting("MENU_LABEL", default=_("Stock images"))
MENU_ORDER = get_setting("MENU_ORDER", default=8000)
PATH_PREFIX = get_setting("PATH_PREFIX", default="stock-images")

SEARCH_ENGINE = get_setting(
    "SEARCH_ENGINE",
    default="wagtail_stock_images.contrib.unsplash.UnsplashSearchEngine",
)

UNSPLASH_CLIENT_ID = get_setting("UNSPLASH_CLIENT_ID", default="")
UNSPLASH_CLIENT_SECRET = get_setting("UNSPLASH_CLIENT_SECRET", default="")
UNSPLASH_REDIRECT_URI = get_setting("UNSPLASH_REDIRECT_URI", default="")
