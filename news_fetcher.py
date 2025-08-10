import os
import requests
from dotenv import load_dotenv

# This line loads the variables from your .env file
load_dotenv()

# This retrieves the API key you just saved
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
NEWS_API_ENDPOINT = "https://newsapi.org/v2/everything"

def get_news(topic: str, max_articles: int = 5) -> list:
    """
    Fetches a list of news articles for a given topic from NewsAPI.
    """
    if not NEWS_API_KEY:
        # This handles the case where the API key is missing
        return ["Error: News API key is not configured in the .env file."]

    # These are the options we send to the API, like a search query
    params = {
        "q": topic,
        "apiKey": NEWS_API_KEY,
        "pageSize": max_articles,
        "sortBy": "publishedAt",
        "language": "en"
    }

    try:
        # This sends the actual request to the NewsAPI server
        response = requests.get(NEWS_API_ENDPOINT, params=params)
        response.raise_for_status()  # This will raise an error if the request failed
        
        data = response.json()
        articles = data.get("articles", [])
        
        if not articles:
             return [f"Sorry, I couldn't find any recent articles about {topic}."]

        # We format the articles into a clean, readable list
        formatted_articles = [f"- {article['title']}: {article['url']}" for article in articles]
        
        return formatted_articles
        
    except requests.exceptions.RequestException as e:
        # This handles network errors
        print(f"Error fetching news: {e}")
        return ["Error: Could not connect to the news service."]

# This special block allows us to test the file directly
if __name__ == "__main__":
    print("Testing the news fetcher...")
    test_topic = "artificial intelligence"
    news_list = get_news(test_topic)
    
    print(f"\nTop news about '{test_topic}':")
    for item in news_list:
        print(item)