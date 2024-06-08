import requests


def movie_search(m):

    api_key = 'a7b1b975b1e7a3e1ae4339b129e1548e'

    base_url = 'https://api.themoviedb.org/3/'

    movie_name = m

    endpoint = 'search/movie'

    params = {'api_key': api_key, 'query': movie_name}

    response = requests.get(base_url + endpoint, params=params)

    data = response.json()

    return data





