# DayLia API

Serveur proxy léger pour le projet DayLia (build WebGL).  
Relaie les requêtes du jeu Unity vers l'API OpenAI.

## Déploiement sur Render

1. Créer un **Web Service** sur [render.com](https://render.com)
2. Connecter ce repo
3. **Build Command** : `pip install -r requirements.txt`
4. **Start Command** : `gunicorn app:app`
5. Ajouter la variable d'environnement `OPENAI_API_KEY` avec votre clé
