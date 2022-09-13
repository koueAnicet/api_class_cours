# 7192416_APIs_DRF
Un endpoint:
    est une URL sur laquelle on réalise différents appels. Selon la méthode HTTP utilisée 
    (GET, POST, PATCH, DELETE), une partie de code va être exécutée et retourner un résultat.

Ce résultat est constitué :
    D’un status code (200, 201, 400, etc.) qui indique le succès ou non de l’appel ;
    D’un contenu qui est en JSON dans la majorité des cas (peut également être du XML dans certains cas),
    et qui va contenir des informations soit de succès soit d’erreur.

En avant, mettons en place ce premier endpoint en permettant à nos visiteurs d’accéder à la liste des catégories de nos produits.

    La toute première chose à faire lors de la réalisation d’un endpoint est de se demander quelles sont les informations importantes que nous souhaitons en tirer.

Rendez les Views plus génériques avec un ModelViewset
    Notons également qu’il n’est plus nécessaire d'appeler  .as_view(), le router le fait pour nous lorsqu’il génère les URL.

    Le paramètre basename  permet de retrouver l’URL complète avec la fonction redirect, comme le propose Django. Cela sera utile lors de l’écriture des tests que nous aborderons ensuite.

    Un ModelViewset  est comparable à une super vue Django qui regroupe à la fois CreateView, UpdateView, DeleteView, ListView  et DetailView.

Filtrez les résultats d’un endpoint
    Appliquez un filtre sur les données retournées
    Utilisez un filtre transmis dans l’URL
        http://127.0.0.1:8000/api/product/?category_id=1


Une nouvelle classe de test 'APITestCase'  est fournie par DRF. Elle est faite pour fonctionner de la   même façon que la classe 'TestCase'. Sa principale différence étant d’utiliser un client qui permet une utilisation plus simple des appels. Il est donc recommandé de l’utiliser pour ne pas avoir à définir plusieurs paramètres pour réaliser nos appels lors des tests.


La pagination indique les informations suivantes :

    count  : le nombre total d’éléments ;
    next  : l’URL de l’endpoint pour obtenir la page suivante ;
    previous  : l’URL de l’endpoint pour obtenir la page précédente ;
    results  : les données réelles utilisables.

#----Minimisez les appels de votre API grâce aux serializers---#

    En résumé
Imbriquer des serializers permet d’obtenir plus d’informations en un seul appel.
Il est possible d’appliquer des filtres sur un attribut du serializer en utilisant un SerializerMethodField.
Toute modification d’un endpoint entraîne l’adaptation d’un test.
Il est bien de rapidement mettre en place une pagination sur une API.