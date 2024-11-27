# Script pour convertir en tiddlers les panneaux du site securotheque.wallonie.be
# Note: le script n'est pas parfait et ne gère pour le moment pas les variantes de panneaux ayant le même code

import requests
from bs4 import BeautifulSoup
import logging
import json
import re
from concurrent.futures import ThreadPoolExecutor, as_completed

# Configuration du logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# Activer ou désactiver le mode test
mode_test = False  # Change à False pour désactiver le mode test

# URL de la page principale
BASE_URL = "https://securotheque.wallonie.be"
MAIN_URL = f"{BASE_URL}/equipements/signalisation-c/verticale/signaux"

# Limite de liens en mode test
TEST_LINK_LIMIT = 3

# Liste pour stocker les données formatées pour le JSON
panneaux_data = []

# Timeout de la requête
REQUEST_TIMEOUT = 10

def fetch_page(url):
    """Fetches the content of a webpage, returns the BeautifulSoup object or None on failure."""
    try:
        response = requests.get(url, timeout=REQUEST_TIMEOUT)
        response.raise_for_status()  # Lève une exception pour les erreurs HTTP
        return BeautifulSoup(response.content, 'html.parser')
    except requests.RequestException as e:
        logging.error(f"Erreur lors de la récupération de la page : {url} - {e}")
        return None

def parse_title(title):
    """Parse the title to extract name, category, and optionally a description."""
    parts = title.split(" – ")
    if len(parts) >= 3:
        nom = parts[0].split(":")[-1].replace(" - Sécurothèque", "").strip()
        catégorie = "[[{}]]".format(parts[1].strip())
        description = parts[2].replace(" - Sécurothèque", "").strip()
        return {
            "title": nom,
            "tags": catégorie,
            "description": description
        }
    elif len(parts) == 2:
        nom = parts[0].split(":")[-1].replace(" - Sécurothèque", "").strip()
        catégorie = "[[{}]]".format(parts[1].strip())
        return {
            "title": nom,
            "tags": catégorie,
            "description": "Description non fournie"
        }
    elif len(parts) == 1:
        nom = parts[0].split(":")[-1].replace(" - Sécurothèque", "").strip()
        return {
            "title": nom,
            "tags": "[[Catégorie non fournie]]",
            "description": "Description non fournie"
        }
    logging.error(f"Impossible de parser le titre : '{title}'")
    return None

def extract_panneaux_from_main_page():
    """Extract all panneau images and their associated links from the main page."""
    soup = fetch_page(MAIN_URL)
    if not soup:
        logging.error("Échec de la récupération de la page principale.")
        return []

    panneaux = []
    for link in soup.select("a[href^='/equipements/signalisation-c/verticale/']"):
        href = link.get('href')
        full_url = BASE_URL + href
        img = link.find("img", src=True)
        if img:
            img_src = BASE_URL + img['src']
            panneaux.append((img_src, full_url))

    return panneaux

def extract_and_store_details(img_src, url):
    """Fetches a webpage, extracts title, code articles, and stores the panneau information."""
    soup = fetch_page(url)
    if not soup:
        logging.error(f"Échec de la récupération de la page de détail : {url}")
        return

    # Extraire les informations générales du panneau
    title = soup.title.string.strip() if soup.title else "Titre non trouvé"
    panneau_info = parse_title(title)
    if not panneau_info:
        logging.error(f"Échec du parsing du titre : {title}")
        return

    # Trouver l'article du code de la route dans la section cadreLegal -> tab_0_0
    code_articles = []
    cadre_legal = soup.find("div", class_="cadreLegal")
    if cadre_legal:
        tab = cadre_legal.find("div", id="tab_0_0")
        if tab:
            for element in tab.find_all(['p', 'strong']):
                element_text = element.get_text(strip=True)
                if element_text.startswith("Art"):
                    code_articles.extend(re.findall(r"\d+\.\d+", element_text))

    # Ajouter les informations spécifiques au panneau
    panneau_info.update({
        "code_article": " ".join(sorted(set(code_articles))) if code_articles else "Article non trouvé",
        "source": url,
        "image": img_src
    })

    panneaux_data.append(panneau_info)

def save_data_to_json():
    """Save the panneaux_data list to a JSON file."""
    with open("panneaux_data.json", "w", encoding="utf-8") as json_file:
        json.dump(panneaux_data, json_file, ensure_ascii=False, indent=4)
    logging.error("Données JSON générées dans 'panneaux_data.json'")

def main():
    panneaux = extract_panneaux_from_main_page()
    if mode_test:
        panneaux = panneaux[:TEST_LINK_LIMIT]

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_panneau = {
            executor.submit(extract_and_store_details, img_src, url): (img_src, url)
            for img_src, url in panneaux
        }

        for future in as_completed(future_to_panneau):
            img_src, url = future_to_panneau[future]
            try:
                future.result()
            except Exception as exc:
                logging.error(f"Lien {url} a généré une exception : {exc}")

    save_data_to_json()

if __name__ == "__main__":
    main()
