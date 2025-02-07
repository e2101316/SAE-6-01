"""
📝 **Instructions** :
- Installez toutes les bibliothèques nécessaires en fonction des imports présents dans le code, utilisez la commande suivante :conda create -n projet python pandas numpy ..........
- Complétez les sections en écrivant votre code où c’est indiqué.
- Ajoutez des commentaires clairs pour expliquer vos choix.
- Utilisez des emoji avec windows + ;
- Interprétez les résultats de vos visualisations (quelques phrases).
"""

### 1. Importation des librairies et chargement des données
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import plotly.express as px

# Chargement des données
data = pd.read_csv('ds_salaries.csv', sep=',')


### 2. Exploration visuelle des données
#votre code 
st.title("📊 Visualisation des Salaires en Data Science")
st.markdown("Explorez les tendances des salaires à travers différentes visualisations interactives.")


if st.checkbox("Afficher un aperçu des données"):
    st.write(data.head(10))


#Statistique générales avec describe pandas 
#votre code 
st.subheader("📌 Statistiques générales")
st.write(data.describe())

### 3. Distribution des salaires en France par rôle et niveau d'expérience, uilisant px.box et st.plotly_chart
#votre code 

data_fr = data[data.company_location == 'FR']
data_selec = data_fr[['company_location', 'job_title', 'salary_in_usd','experience_level']]
st.subheader("📈 Distribution des salaires en France")

fig = px.box(data_selec, x='experience_level', y='salary_in_usd', color='experience_level')
st.plotly_chart(fig)

### 4. Analyse des tendances de salaires :
#### Salaire moyen par catégorie : en choisisant une des : ['experience_level', 'employment_type', 'job_title', 'company_location'], utilisant px.bar et st.selectbox 
select = st.selectbox('Choix de catégorie', ['Poste', "Niveau d'expérience", "Type d'emplois", 'Locatisation (entreprise)'])

   
if select == 'Poste':
    selec = data[['job_title','salary_in_usd']]
    moyenne = selec.groupby('job_title').mean('salary_in_usd')
    moyenne["job_title"] = moyenne.index
    fig2 = px.bar(moyenne, x = 'job_title', y = 'salary_in_usd', color = 'job_title')
    st.plotly_chart(fig2)
    
if select == "Niveau d'expérience":
    selec = data[['experience_level','salary_in_usd']]
    moyenne = selec.groupby('experience_level').mean('salary_in_usd')
    moyenne["experience_level"] = moyenne.index
    fig2 = px.bar(moyenne, x = 'experience_level', y = 'salary_in_usd', color = 'experience_level')
    st.plotly_chart(fig2)
    
if select == "Type d'emplois":
    selec = data[['employment_type','salary_in_usd']]
    moyenne = selec.groupby('employment_type').mean('salary_in_usd')
    moyenne["employment_type"] = moyenne.index
    fig2 = px.bar(moyenne, x = 'employment_type', y = 'salary_in_usd', color = 'employment_type')
    st.plotly_chart(fig2)
    
if select == 'Locatisation (entreprise)':
    selec = data[['company_location','salary_in_usd']]
    moyenne = selec.groupby('company_location').mean('salary_in_usd')
    moyenne["company_location"] = moyenne.index
    fig2 = px.bar(moyenne, x = 'company_location', y = 'salary_in_usd', color = 'company_location')
    st.plotly_chart(fig2)

### 5. Corrélation entre variables
# Sélectionner uniquement les colonnes numériques pour la corrélation
#votre code 
data_num = data.select_dtypes(include=[np.number])


# Calcul de la matrice de corrélation
#votre code
correlation_matrix = data_num.corr()
st.write(correlation_matrix)



# Affichage du heatmap avec sns.heatmap
#votre code 
st.subheader("🔗 Corrélations entre variables numériques")

fig3 = sns.heatmap(correlation_matrix)
st.pyplot(fig3.get_figure())


### 6. Analyse interactive des variations de salaire
# Une évolution des salaires pour les 10 postes les plus courants
# count of job titles pour selectionner les postes
# calcule du salaire moyen par an
#utilisez px.line
#votre code 





### 7. Salaire médian par expérience et taille d'entreprise
# utilisez median(), px.bar
#votre code 




### 8. Ajout de filtres dynamiques
#Filtrer les données par salaire utilisant st.slider pour selectionner les plages 
#votre code 




### 9.  Impact du télétravail sur le salaire selon le pays




### 10. Filtrage avancé des données avec deux st.multiselect, un qui indique "Sélectionnez le niveau d'expérience" et l'autre "Sélectionnez la taille d'entreprise"
#votre code 

