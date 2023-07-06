# Francisation des exercices

J'ai fait le choix d'utiliser des gabarits pour effectuer la traduction des exercices.
 Cela me paraît moins nous exposer à des erreurs. En effet dans le cas 
 d'une validation des réponses automatisée, il faut être particulièrement
 attentif à la cohérence des données. 
 
Cela exige en contrepartie la mise au point (c'est fait) et l'utilisation
 d'un système de gabarits et de remplacement de texte.

## Exercices déjà traduits

Les textes des exercices sont sous la forme de fichiers comme `task1.txt` 
 accompagné de son `task1.template` par exemple.
 
 - Le fichier `*.txt` est celui qui sera effectivement utilisé par 
  l'exercicseur.
  
 - Le fichier `*.template` est celui qui va généré le précédent après
 subsitution des expressions finnois par leur éqhuvalente française.
  

Les exercices 1 à 16 sont déjà traduits. Il reste ceux de 17 à 100...

## Pour continuer la traduction

Le cycle de travail est le suivant:

### Mise à jour des fichiers originaux pour traduction

- Ouvrir un fichier `*.template` non encore traité
- Entourer les expressions en _suomi_ par des doubles accolades: `{{ ... }}`.
Les phrases complètes sont à entourer dans leur globalité car 
on ne va pas faire une traduction mot-à-mot. C'est le cas des consignes de chaque énoncé.
- Enregistrer les modifications.

### Mise à jour des entrées du dictionnaire

- Une fois un ou plusieurs fichiers `template` mis à jour par vos soins,
exécutez le script python `motscles.py`

Il passe en revue tous les `*.template` 
 et note les nouvelles entrées encore sans traduction, tout en générant
  les fichiers traduits avec les entrées complètes. 
  
L'avancement du projet de traduction est affiché pour chaque fichier
 en pourcentage.

Un dictionnaire (au sens Python comme au sens propre) est utilisé pour stocker les traductions 
françaises des expressions finnoises,. 

Ce dictionnaire est stocké dans le fichier `suomi-français.json`.
 
### Mise à jour du dictionnaire

Il faut ouvrir le fichier `suomi-français.json` et rempacer les `null`
 par l'expression française correspondant à la clé.
 
 Personnellement, j'utilise google translate et j'adapte.
 
 ## En résumé :
 
  ```mermaid
graph TD
0{Jour de pluie ?} -- oui --> A 
A[modification d'un ou plusieurs template] --> B[`python motscles.py`]
B --> C[complétion des enntrées du dictionnaire]
B --> E[création des exercices traduits]
C --> D[Ajout manuel des traductions dans le dictionnaire]
D --> A
D --> B
```
