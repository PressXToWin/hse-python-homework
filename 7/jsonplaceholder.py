from http.client import HTTPException

import requests

url = "https://jsonplaceholder.typicode.com/posts"
POST_COUNT = 5

def main():
    response = requests.get(url)

    if response.status_code != 200:
        raise HTTPException(response.status_code)

    posts = response.json()

    if not isinstance(posts, list):
        raise TypeError("Posts must be a list")

    if len(posts) == 0:
        raise ValueError("No posts found")

    count_posts = min(POST_COUNT, len(posts))
    posts_to_show = posts[:count_posts]

    for post in posts_to_show:
        title = post.get("title")
        body = post.get("body")

        print(f"Заголовок: {title}")
        print(f"Тело: {body}")
        print("\n")

if __name__ == "__main__":
    main()