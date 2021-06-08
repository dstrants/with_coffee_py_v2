import requests


class HackerNews:
    def __init__(self) -> None:
        self.base_url = "https://hacker-news.firebaseio.com/v0"

    
    def call(self, endpoint: str) -> dict:
        response = requests.get(f"{self.base_url}/{endpoint}")
        response.raise_for_status()
        return response.json()
    
    def maxid(self) -> dict:
        return self.call("maxitem")
    
    def new_stories(self) -> dict:
        return self.call("newstories")

    def top_stories(self) -> dict:
        return self.call("topstories")
    
    def article(self, id: int) -> dict:
        return self.call(f"item/{id}")