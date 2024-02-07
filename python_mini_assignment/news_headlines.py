import requests
from bs4 import BeautifulSoup


def get_news_headlines():
    """
    This function will get the headlines form the new website
    :return: list of headlines
    """

    url = "https://timesofindia.indiatimes.com/home/headlines"
    response = requests.get(url)

    try:
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            top_news_element = soup.find('div', class_='top-newslist')
            news_list = top_news_element.select("li")

            headlines_list = [headline.get_text() for headline in news_list]
            return headlines_list
        else:
            print(f"Error: Unable to fetch news headlines. Status Code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred file fetching weather data: {e}")


def save_to_file(headlines_list, filename="news_headlines.txt"):
    # write the headlines into the file
    try:
        with open(".\\text_filles\\news_headlines.txt", 'w', encoding='utf-8') as file:
            for headline in headlines_list:
                file.write(f"{headline}\n")
    except Exception as e:
        print(f"error while write to the file {e}")


if __name__ == "__main__":
    headlines = get_news_headlines()
    # displays in console
    for headline in headlines:
        print(headline)
    save_to_file(headlines)

