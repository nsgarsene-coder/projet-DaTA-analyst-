 README — Analyse des Animés (EDA, Clustering, Classification)
 Description du projet
Ce projet analyse un dataset d’animés à partir de plusieurs indicateurs de qualité :
- Note globale
- Note du meilleur épisode
- Note du pire épisode
- Nombre d’épisodes
- Studio
- Genres
- Score final et score qualité
- Régularité
L’objectif est de :
- Réaliser une analyse exploratoire des données (EDA)
- Détecter les anomalies (Isolation Forest)
- Segmenter les animés en clusters (K-Means)
- Construire un modèle de classification pour prédire le segment d’un animé
- Générer des visualisations et des insights pour comprendre les tendances du dataset

Structure du projet
projet-anime/
│
├── data/
│   └── anime.csv
│
├── figures/
│   ├── boxplot_note_globale.pdf
│   ├── histogramme_note_pire_ep.pdf
│   ├── clusters_kmeans.pdf
│   └── ...
│
├── notebooks/
│   └── analyse_anime.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── clustering.py
│   ├── classification.py
│   └── visualization.py
│
└── README.md



 Installation
1. Cloner le projet
git clone https://github.com/ton-projet-anime.git



2. Créer un environnement virtuel 
python -m venv venv
venv\Scripts\activate      # Windows


3. Installer les dépendances
pip install -r requirements.txt


4. Lancer Jupyter Notebook
jupyter notebook



 Dépendances principales
Voici les librairies utilisées dans le projet :
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- scipy
- jupyter
Tu peux les installer avec :
-pip install pandas numpy matplotlib seaborn scikit-learn scipy jupyter



 Fonctionnalités du projet
 1. Analyse exploratoire (EDA)
- Statistiques descriptives
- Visualisation des distributions
- Boxplots par studio
- Corrélations entre les notes
- Analyse de la régularité
 2. Détection d’anomalies
- Isolation Forest
- Visualisation des anomalies
- Interprétation des séries atypiques
 3. Clustering (K-Means)
- Normalisation des données
- Détermination du nombre optimal de clusters
- Visualisation des clusters
- Interprétation des segments
 4. Classification
- Modèles testés :
- Logistic Regression
- KNN
- Random Forest
- SVM
- Évaluation :
- Accuracy
- Precision
- Recall
- F1-score
- Matrice de confusion
- Importance des variables
 5. Export des graphiques
Tous les graphiques sont enregistrés automatiquement dans le dossier figures/.
- Ouvrir le notebook :
jupyter notebook notebooks/analyse_anime.ipynb


- Exécute les cellules dans l’ordre :
- Chargement des données
- Nettoyage
- EDA
- Normalisation
- Clustering
- Classification
- Export des graphiques
- Les résultats apparaîtront dans le notebook et dans le dossier figures/.

 Résultats principaux
- Les animés sont globalement bien notés (moyenne ≈ 8.2–8.7)
- Le pire épisode est l’indicateur le plus important
- Les studios influencent fortement la régularité
- L’Isolation Forest détecte correctement les séries extrêmes
- Le clustering révèle 3–4 segments cohérents
- Le modèle Random Forest atteint ≈ 85% d’accuracy

 Auteurs
Projet réalisé par N'SOUGAN KOSSIGAN ARSENE, étudiant en France (Val-de-Marne), passionné de data science, d’IA et d’animation japonaise.

Licence
Projet académique — libre d’utilisation dans un cadre éducatif.

