# Sports API Parser – Daily Sports Leagues Tracker

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
SportsPulse is a backend-focused project that automates the process of collecting sports leagues data.  
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

## Installation
1. Clone repo:  
```bash
git clone https://github.com/yourusername/sportspulse.git
cd sportspulse
