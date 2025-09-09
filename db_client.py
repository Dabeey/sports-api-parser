import sqlite3

DB_NAME = 'sports.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute('''
    CREATE TABLE IF NOT EXISTS leagues(
        idLeague TEXT PRIMARY KEY,
        strLeague TEXT,
        strSport TEXT,
        strLeagueAlternate TEXT)''')

    conn.commit()
    conn.close()
    print('\nDatabase initialized with leagues table.')


def insert_leagues(leagues: list[dict]) -> None:
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    for league in leagues:
        cur.execute('''
        INSERT OR REPLACE INTO leagues (idLeague, strLeague, strSport, strLeagueAlternate)
        VALUES (?, ?, ?, ?)
        ''',(
            league.get('idLeague'),
            league.get('strLeague'),
            league.get('strSport'),
            league.get('strLeagueAlternate')
        ))

    conn.commit()
    conn.close()
    print(f'\nInserted/Updated {len(leagues)} league into the database.')


def get_all_leagues(limit: int=10):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute('SELECT idLeague, strLeague, strSport, strLeagueAlternate FROM leagues LIMIT ?', (limit,))
    rows = cur.fetchall()    
    conn.close()
    return rows

def get_leagues_by_sport(sport: str):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()

    cur.execute('SELECT idLeague, strLeague FROM leagues WHERE strSport = ?', (sport,))
    rows = cur.fetchall()
    conn.close()
    return rows 
