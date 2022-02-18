import requests
import json
import sys

def main():

    url = f'https://api.github.com/users/{sys.argv[1]}/repos'

    if requests.get(url).status_code != 200:
        print(f'Request failed with status code {requests.get(url).status_code}')
        if requests.get(url).status_code == 404:
            print("404 Error: type a correct user or user does not exist")
        elif requests.get(url).status_code == 403:
            print('Cannot make another request. Achieved rate limit.')
        sys.exit(f'Usage: {sys.argv[0]}')

    response = requests.get(url)

    data = json.loads(response.content)

    for repos in data:
        print(repos['name'])


if __name__ == '__main__':
    main()
