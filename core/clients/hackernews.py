import requests
from core.models.hackernews import Article


class HackerNews:
    def __init__(self, limit: int = 5) -> None:
        self.base_url = "https://hacker-news.firebaseio.com/v0"
        self.articles = self.get_articles(limit=limit)
    

    def get_articles(self, limit: int = 5) -> list[Article]:
        ids = self.top_stories()[:limit]
        articles = [Article(**self.article(a_id)) for a_id in ids]
        return articles
    
    def call(self, endpoint: str) -> dict:
        response = requests.get(f"{self.base_url}/{endpoint}.json")
        response.raise_for_status()
        return response.json()
    
    def max_id(self) -> dict:
        return self.call("maxitem")
    
    def new_stories(self) -> dict:
        return self.call("newstories")

    def top_stories(self) -> dict:
        return self.call("topstories")
    
    def article(self, id: int) -> dict:
        return self.call(f"item/{id}")