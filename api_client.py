import requests
import time

BASEURL = "https://www.thesportsdb.com/api/v1/json/123"

def get_json(url: str, params: dict|None = None, *, retries: int=3, timeout: float = 10.0) -> dict | list :
    try:
        response = requests.get(url=url, params=params, timeout=timeout)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        if retries > 0:
            time.sleep(1)
            return get_json(url, params, retries=retries-1, timeout=timeout)
        print(f'Error fetching {url}: {e}')
        return None



if __name__ == "__main__":
    url = f'{BASEURL}/all_leagues.php'
    data = get_json(url)
    assert data is not None and 'leagues' in data, 'Failed to fetch leagues'
    print('OK: fetched all leagues')

    bad = get_json(f'{BASEURL}/badendpoint.php', retries=2, timeout=3)
    assert bad is None, 'Expected failure on bad endpoint'
    print('OK: handled bad endpoint gracefully')