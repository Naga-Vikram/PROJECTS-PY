import requests
from datetime import datetime
#api=pub_8758248bac1a7b2f97b5dd257c7bc54a37646
def fetch_news(api_key, query="climate"):
    """
    Fetches news articles from the Newsdata.io API using requests.

    Args:
        api_key: Your Newsdata.io API key.
        query: The search query (e.g., "climate", "technology").

    Returns:
        A dictionary containing the API response, or None on error.
    """
    url = f"https://newsdata.io/api/1/news?apikey={api_key}&q={query}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses
        data = response.json()
        return data
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching news: {e}")
        print(f"HTTP Status Code: {e.response.status_code}")
        print(f"Error Message: {e.response.text}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Error fetching news: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

def format_date(date_string):
    """Formats a date string from Newsdata.io into a user-friendly format."""
    if not date_string:
        return "date not found"
    try:
        dt = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
        return dt.strftime("%Y-%m-%d %H:%M")
    except ValueError:
        return "date not found"

def prepare_news_for_display(api_response):
    """
    Prepares news articles from the API response for display.

    Args:
        api_response: The dictionary returned by the Newsdata.io API.

    Returns:
        A list of dictionaries, where each dict is a formatted article, or an empty list.
    """
    formatted_articles = []
    if api_response and api_response.get('status') == 'success':
        articles = api_response.get('results', [])
        for article in articles:
            formatted_article = {
                "title": article.get('title', 'No Title'),
                "description": article.get('description', 'No Description'),
                "formatted_date": format_date(article.get('pubDate')),
                "url": article.get('link', '#'),
            }
            formatted_articles.append(formatted_article)
    else:
        print("Error: Invalid API response")
        return []
    return formatted_articles

def display_news_cli(formatted_articles):
    """
    Displays the formatted news articles in a simple command-line format.
    """
    if not formatted_articles:
        print("no news to display")
        return

    for article in formatted_articles:
        print("-" * 80)
        print(f"Title: {article['title']}")
        print(f"Date: {article['formatted_date']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("-" * 80)

def main():
    """
    Main function to run the news app.
    """
    api_key ="pub_8758248bac1a7b2f97b5dd257c7bc54a37646"
    if not api_key:
        print("Error: API key is required.")
        return

    query = input("Enter your search query (e.g., climate, technology): ").strip()
    if not query:
        query = "general"

    news_response = fetch_news(api_key, query)
    if news_response:
        formatted_articles = prepare_news_for_display(news_response)
        display_news_cli(formatted_articles)
    else:
        print("Failed to retrieve news.")

if __name__ == "__main__":
    main()