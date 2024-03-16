# Book Scraper

Ce projet Python extrait des données de livres (titre, prix, évaluation) depuis le site [books.toscrape.com](https://books.toscrape.com/). Les données sont ensuite stockées dans un fichier CSV.

## Dépendances

* Python 3+
* Beautiful Soup 4 
* requests
* pandas

## Installation

1. Cloner le répertoire: `git clone https://github.com/votre-nom-utilisateur/book-scraper.git`
2. Installer les paquets requis: `pip install -r requirements.txt` (créez un fichier requirements.txt listant les dépendances)

## Utilisation

1.  Exécuter le script principal: `python scraper.py`
2. Les données extraites seront sauvegardées dans le fichier 'books.csv'.

## Améliorations potentielles

* Gérer les caractères spéciaux ou non compatibles dans les titres de livre.
* Extraire des informations supplémentaires (ISBN, description, catégorie, etc.).
* Implémenter une gestion d'erreurs plus robuste (connexions, parsing).

## Contribuer

Toutes les contributions sont les bienvenues! Ouvrez une Issue ou soumettez un Pull Request pour suggérer des améliorations.

## License

Ce projet est sous licence MIT. Pour plus d'informations, consultez le fichier LICENSE.
