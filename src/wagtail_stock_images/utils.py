from django.utils.module_loading import import_string

from wagtail_stock_images.engine import AbstractSearchEngine
from wagtail_stock_images.settings import SEARCH_ENGINE


def get_search_engine() -> AbstractSearchEngine:
    search_engine = import_string(SEARCH_ENGINE)
    return search_engine()
