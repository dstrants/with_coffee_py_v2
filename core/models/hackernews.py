import pendulum
from pydantic import HttpUrl

from core.models.base import BaseEntry


class Article(BaseEntry):
    by: str
    descendants: int
    id: int
    kids: list[int]
    score: int
    time: int
    title: str
    type: str
    url: HttpUrl

    def human_ts(self) -> str:
        return pendulum.from_timestamp(self.time).to_datetime_string()
