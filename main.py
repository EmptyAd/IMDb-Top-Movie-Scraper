from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

# IMDb Top 250 URL
url = 'https://www.imdb.com/chart/top/'
headers = {'User-Agent': 'Mozilla/5.0'}  # Avoid blocking
response = requests.get(url, headers=headers)

# Check if request was successful
if response.status_code != 200:
    print("Failed to retrieve data")
    exit()

soup = BeautifulSoup(response.text, "html.parser")

# Debug: Print the structure of the page
#print(soup.prettify())  # Uncomment to inspect the page source

# Find movie containers (Check IMDb page structure)
movies = soup.select('li.ipc-metadata-list-summary-item')  # Updated selector

if not movies:
    print("No movie data found. IMDb might have changed its structure.")
    exit()

# Extract movie details
movie_list = []
for index, movie in enumerate(movies[:250]):  # Get only top 250 movies
    title_tag = movie.select_one('h3')  # Find movie title
    movie_title = title_tag.text.strip() if title_tag else "N/A"

    year_tag = movie.select_one('span.ipc-metadata-list-summary-item__tl')  # Check for year
    year_match = re.search(r'\d{4}', year_tag.text) if year_tag else None
    year = year_match.group(0) if year_match else "N/A"

    rating_tag = movie.select_one('span.ipc-rating-star')  # Find rating
    rating = rating_tag.text.strip() if rating_tag else "N/A"

    stars_tag = movie.select_one('div.ipc-inline-list')  # Find cast
    stars = stars_tag.text.strip() if stars_tag else "N/A"

    data = {
        "place": index + 1,
        "movie_title": movie_title,
        "rating": rating,
        "year": year,
        "star_cast": stars,
    }
    movie_list.append(data)

# Save to CSV
df = pd.DataFrame(movie_list)
df.to_csv('imdb_top_250_movies.csv', index=False)

# Print top 10 movies for verification
for movie in movie_list[:10]:
    print(f"{movie['place']} - {movie['movie_title']} ({movie['year']}) - Starring: {movie['star_cast']} - Rating: {movie['rating']}")
