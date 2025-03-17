# IMDb Top Movie Scraper

## Overview
This Python script scrapes IMDb's Top 250 movies and extracts details such as rank, title, year of release, rating, and star cast. The data is then saved as a CSV file for further analysis.

## Features
- Scrapes IMDb Top 250 movies
- Extracts movie rank, title, year, rating, and star cast
- Saves data in `imdb_top_250_movies.csv`

## Requirements
Ensure you have Python installed along with the following dependencies:

```sh
pip install beautifulsoup4 requests pandas
```

## Usage
Run the script using the command:

```sh
python main.py
```

## Output
The script generates a CSV file named `imdb_top_250_movies.csv` with the following structure:

| Rank | Movie Title | Year | Rating | Star Cast |
|------|------------|------|--------|-----------|
| 1    | The Shawshank Redemption | 1994 | 9.2 | Tim Robbins, Morgan Freeman |
| 2    | The Godfather | 1972 | 9.1 | Marlon Brando, Al Pacino |

## Notes
- IMDb updates its website structure periodically. If the script stops working, inspect the IMDb page source and update the CSS selectors accordingly.
- Use a VPN if you encounter access issues due to regional restrictions.

