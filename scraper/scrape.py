import requests
import pandas as pd
from bs4 import BeautifulSoup
import time

phone_urls = [
    "https://www.gsmarena.com/samsung_galaxy_s24_ultra-12771.php",
    "https://www.gsmarena.com/samsung_galaxy_s24-12773.php",
    "https://www.gsmarena.com/samsung_galaxy_s24+-12772.php",
    "https://www.gsmarena.com/samsung_galaxy_s23_ultra-12024.php",
    "https://www.gsmarena.com/samsung_galaxy_s23-12082.php",
    "https://www.gsmarena.com/samsung_galaxy_s23+-12083.php",
    "https://www.gsmarena.com/samsung_galaxy_s22_ultra_5g-11251.php",
    "https://www.gsmarena.com/samsung_galaxy_s22_5g-11253.php",
    "https://www.gsmarena.com/samsung_galaxy_s21_ultra_5g-10596.php",
    "https://www.gsmarena.com/samsung_galaxy_a55-12824.php"
]

headers = {
    "User-Agent": "Mozilla/5.0"
}

phones = []

for url in phone_urls:
    try:
        print(f"Scraping: {url}")

        response = requests.get(
            url,
            headers=headers,
            timeout=20
        )

        response.raise_for_status()

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        phone_name = soup.find(
            "h1",
            class_="specs-phone-name-title"
        ).text.strip()

        specs = {}

        for row in soup.find_all("tr"):
            cells = row.find_all("td")

            if len(cells) >= 2:
                key = cells[0].get_text(
                    strip=True
                )

                value = cells[1].get_text(
                    " ",
                    strip=True
                )

                specs[key] = value

        phone_data = {
            "name": phone_name,
            "display_size": specs.get("Size", ""),
            "chipset": specs.get("Chipset", ""),
            "storage": specs.get("Internal", ""),
            "battery": specs.get("Type", ""),
            "charging": specs.get("Charging", "")
        }

        phones.append(phone_data)

        print(
            f"Collected: {phone_name}"
        )

        time.sleep(2)

    except Exception as e:
        print(
            f"Error scraping {url}"
        )
        print(e)

df = pd.DataFrame(phones)

df.to_csv(
    "data/samsung_phones.csv",
    index=False
)

print("\nCSV Saved Successfully")
print(df.head())