from wagtail_stock_images.utils import get_search_engine


def test_default_search_engine():
    search_engine = get_search_engine()
    assert search_engine
