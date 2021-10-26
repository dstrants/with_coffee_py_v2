from typing import Union

import requests
from core.models.hackernews import Article


class HackerNews:
    """
    HACKER NEWS CLIENT

    Consumes the hackernews firebase api to fetch articles.

    params:
    limit: int -> Number of articles to be fetched from hackernews. Defaults to 5.
    """
    def __init__(self, limit: int = 5) -> None:
        self.base_url = "https://hacker-news.firebaseio.com/v0"
        self.articles = self.get_articles(limit=limit)
    

    def get_articles(self, limit: int = 5) -> list[Article]:
        """
        GET ARTICLES LIST
        
        Returns a list of articles included in the topstories list.
        It automatically parses the articles in pydantic classes.
        """
        ids = self.top_stories()[:limit]
        articles = [Article(**self.article(a_id)) for a_id in ids]
        return articles
    
    def call(self, endpoint: str) -> Union[dict, list, int]:
        """Abstract method to communicate with the hackernes API."""
        response = requests.get(f"{self.base_url}/{endpoint}.json")
        response.raise_for_status()
        return response.json()
    
    def max_id(self) -> int:
        """Returns the maximum available article id in hackernews."""
        return self.call("maxitem")
    
    def new_stories(self) -> list:
        """Returns the list of article ids of the newester stories available in hackernews."""
        return self.call("newstories")

    def top_stories(self) -> list:
        return self.call("topstories")
    
    def article(self, id: int) -> dict:
        return self.call(f"item/{id}")