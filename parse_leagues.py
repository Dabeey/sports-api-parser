from api_client import get_json, BASEURL
from db_client import init_db, insert_leagues, get_all_leagues, get_leagues_by_sport
import csv
import argparse
import time

def fetch_leagues_min() -> list[dict]:
    url = f'{BASEURL}/all_leagues.php'
    data = get_json(url)
    if not data or 'leagues' not in data:
        print("Failed to fetch leagues.")
        return []
    return data.get('leagues', [])

def save_leagues_to_csv(leagues: list[dict], filename: str) -> None:
    if not leagues:
        print('\nNo leagues to save.')
        return

    fields = ['idLeague', 'strLeague', 'strSport', 'strLeagueAlternate']

    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows({k: league.get(k,'') for k in fields} for league in leagues)
    print(f'\nSaved {len(leagues)} leagues to {filename}')

def daily_update(filename='leagues_daily.csv'):
    leagues = fetch_leagues_min()
    if not leagues:
        print("No leagues fetched. Skipping DB/Csv update.")
        return

    insert_leagues(leagues)
    save_leagues_to_csv(leagues, filename=filename)
    print(f"✅ Update done! Fetched {len(leagues)} leagues | First: {leagues[0].get('strLeague')}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch and save sports leagues to csv')
    parser.add_argument('--out', type=str, default='leagues_daily.csv', help='Output CSV file name')
    parser.add_argument('--interval', type=int, default=24*60*60, help='Time between updates in seconds')
    args = parser.parse_args()

    init_db()

    try:
        while True:
            daily_update(filename=args.out)
            print(f"⏰ Sleeping {args.interval} seconds...")
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\n⏹ Update loop stopped by user.")
