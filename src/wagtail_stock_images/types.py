from dataclasses import dataclass
from turtle import st
from typing import List, Optional


@dataclass
class Image:
    id: str
    url: str
    title: str
    thumbnail: str
    tags: Optional[List[str]] = None
