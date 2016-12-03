import requests
from urllib.parse import urljoin
from datetime import datetime, timedelta

API_URL = 'https://api.github.com'


def get_trending_repositories(amount_of_reps, days_interval=7, api_url=API_URL):
    days_ago = datetime.today().date() - timedelta(days=days_interval)
    api_method_url = urljoin(api_url, 'search/repositories')
    params = {'q': 'created:>{}'.format(days_ago), "sort": 'stars'}
    repositories_info = requests.get(api_method_url, params=params).json()
    return repositories_info["items"][:amount_of_reps]


def print_trending_repositories(trending_repositories):
    print("{:^72}\n{}|{:^55}|{:^13}".format("GITHUB TRENDING REPOSITORIES",
                                            "STARS", "URL", "OPEN ISSUES"))
    for trending_repository in trending_repositories:
        print("{b[stargazers_count]:^5}|"
              "{b[html_url]:55}|{b[open_issues]:^12}".format(b=trending_repository))


if __name__ == '__main__':
    repositories = get_trending_repositories(20)
    print_trending_repositories(repositories)
