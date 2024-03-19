import wikipedia

def get_wikipedia_summary(article_title):
    try:
        page = wikipedia.page(article_title)
        return page.summary, page.url
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Multiple articles found for '{article_title}'. Please specify more precisely.", None
    except wikipedia.exceptions.PageError as e:
        return f"No article found for '{article_title}'.", None

if __name__ == "__main__":
    article_title = input("Enter the Wikipedia article title: ")
    summary, url = get_wikipedia_summary(article_title)
    if summary:
        print("Summary:", summary)
        print("URL:", url)
