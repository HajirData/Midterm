import re
import requests
from bs4 import BeautifulSoup

def google_search(query):
    url = f"https://www.google.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    search_results = []
    for result in soup.select("div.g"):
        heading = result.select_one("h3")
        if heading:
            title = heading.get_text().strip()
            link = result.select_one("a")["href"]
            description = result.select_one("span.st").get_text()
            search_results.append({"title": title, "link": link, "description": description})
    return search_results

def chatbot():
    print("Hi, I'm a chatbot. What can I help you with today?")
    while True:
        user_input = input("> ")
        if re.search(r"\b(exit|quit)\b", user_input, re.IGNORECASE):
            print("Goodbye!")
            break
        search_results = google_search(user_input)
        if search_results:
            print(f"I found {len(search_results)} results:")
            for result in search_results[:5]:
                print(f"\n{result['title']}")
                print(f"{result['description']}")
                print(f"{result['link']}")
        else:
            print("Sorry, I couldn't find anything related to your query.")

if _name_ == "_main_":
    chatbot()