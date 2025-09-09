# Sports API Parser 

Automated Python tool that fetches sports leagues from TheSportsDB API, stores them in SQLite, and exports daily-updated CSVs for analysis or apps.

---

## Table of Contents
1. [Overview](#overview)  
2. [Features](#features)  
3. [Tech Stack](#tech-stack)  
4. [Installation](#installation)  
5. [Usage](#usage)  
6. [Sample Output](#sample-output)  
7. [Next Steps / Expansion](#next-steps--expansion)  
8. [License](#license)

---

## Overview
Sports API Parser is a backend-focused project that automates the process of collecting sports leagues data.  
- Fetches all leagues from [TheSportsDB API](https://www.thesportsdb.com/api.php)  
- Handles API errors and retries automatically  
- Stores leagues in an SQLite database for persistent storage  
- Saves daily-updated CSV files for analytics or integration with other apps  
- Provides a CLI interface for easy operation  

This is perfect for sports enthusiasts, developers, or analysts who want a ready-to-use dataset without manually scraping or updating data.

---

## Features
- ✅ **Automated data fetching** – pulls all leagues from the API  
- ✅ **Database storage** – SQLite keeps your leagues persistent  
- ✅ **CSV export** – daily-updated CSV file  
- ✅ **Error handling & retries** – ensures data consistency  
- ✅ **Command-line interface (CLI)** – run `python parse_leagues.py --out leagues_min.csv`  
- ✅ **Extendable** – can add dashboards, alerts, or ML predictions  

---

## Tech Stack
- **Python 3.11+**  
- **Requests** – API fetching  
- **SQLite3** – lightweight database  
- **CSV module** – export data  
- **Argparse** – CLI  
- **Time module** – automated daily updates  

---


## Project Structure

```
sports_api_project/
├── api_client.py        # API requests and error handling
├── db_client.py         # SQLite database operations
├── parse_leagues.py     # Main fetch/save/update logic
├── requirements.txt     # Python dependencies
├── sports.db            # SQLite database file
├── leagues_daily.csv    # Output CSV file
```

---


## Installation

**Clone repo:**
```sh
git clone https://github.com/yourusername/sportspulse.git
cd sportspulse
```

**Create virtual environment:**
```sh
python -m venv venv
source venv/bin/activate    # Linux/Mac
venv\Scripts\activate      # Windows
```

**Install dependencies:**
```sh
pip install -r requirements.txt
```

## Usage

Run the script to fetch leagues and save CSV:
```sh
python parse_leagues.py --out leagues_daily.csv
```

- CSV file will be generated in the project folder
- Data will also be inserted into SQLite database `sports.db`
- Infinite loop updates daily automatically; for testing, adjust `time.sleep()`

## Sample Output

```
OK: fetched 100 leagues | First: English Premier League
🎉 Done: leagues saved to DB.
First 5 leagues: [...]
Soccer leagues: [...]
Total leagues in DB: 100
Saved 100 leagues to leagues_daily.csv
```

## Next Steps / Expansion

- Add a dashboard with Flask/Django
- Track upcoming matches and send alerts via email or Telegram
- Include player/team stats for ranking and comparison
- Feed data into analytics or machine learning predictions


## License

MIT License – feel free to use and expand for learning and projects