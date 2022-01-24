from typing import List

from wagtail_stock_images.types import Image


class AbstractSearchEngine:
    def __init__(self, **kwargs):
        pass

    def get_client(self):
        raise NotImplementedError(
            "subclasses of AbstractSearchEngine must provide a get_client() method"
        )

    def get_image(self, id: str) -> Image:
        raise NotImplementedError(
            "subclasses of AbstractSearchEngine must provide a get_image() method"
        )

    def search_images(self, query: str) -> List[Image]:
        raise NotImplementedError(
            "subclasses of AbstractSearchEngine must provide a search_images() method"
        )
