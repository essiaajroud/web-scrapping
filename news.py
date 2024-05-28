from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Fonction pour extraire les titres et les paragraphes de la page Web
def extract_text(url):
    # Faire la requête GET pour obtenir le contenu de la page
    response = requests.get(url)
    # Vérifier si la requête a réussi
    if response.status_code == 200:
        # Utiliser BeautifulSoup pour analyser le contenu HTML de la page
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Exclure les éléments indésirables en utilisant des sélecteurs CSS ou des classes spécifiques
        unwanted_classes = ['header', 'footer', 'navbar', 'sidebar', 'right-side', 'left-side']
        for unwanted_class in unwanted_classes:
            for tag in soup.find_all(class_=unwanted_class):
                tag.decompose()  # Supprimer l'élément du DOM
        
        # Extraire les titres et les paragraphes du contenu principal
        main_content = soup.find('main')  # Adapté selon la structure HTML de votre site
        if main_content:
            titles = [title.get_text() for title in main_content.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])]
            paragraphs = [p.get_text() for p in main_content.find_all('p')]
            
            # Extraire les liens des images
            image_links = [img['src'] for img in main_content.find_all('img') if 'src' in img.attrs]
            
            return {'titles': titles, 'paragraphs': paragraphs, 'images': image_links}
        else:
            return {'error': 'Main content not found.'}
    else:
        # Retourner None si la requête a échoué
        return {'error': 'Failed to fetch URL.', 'status_code': response.status_code}


# Route pour extraire les titres et les paragraphes à partir d'une URL donnée
@app.route('/extract-text/<path:url>', methods=['GET'])
def extract_text_from_url(url):
    data = extract_text(url)
    if data:
        return jsonify(data), 200
    else:
        return jsonify({'error': 'Failed to extract text from URL.'}), 500

if __name__ == '__main__':
    app.run(debug=True)