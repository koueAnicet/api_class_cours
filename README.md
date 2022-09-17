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

#------------Améliorez le rendu du détail d’un endpoint-------#
Lorsqu’une requête entre dans notre API, les viewsets définissent un attribut action  qui correspond à l’action que l’application client est en train de réaliser. Elle peut être :

    list : appel en GET  sur l’URL de liste ;
    retrieve : appel en GET  sur l’URL de détail (qui comporte alors un identifiant) ;
    create : appel en POST  sur l’URL de liste ;
    update : appel en PUT  sur l’URL de détail ;
    partial_update : appel en PATCH  sur l’URL de détail ;
    destroy : appel en DELETE  sur l’URL de détail.

#--------Validez les données----#
 Nous allons très vite en mettre un second en place, qui sera dédié aux administrateurs qui, eux, auront la possibilité de créer, modifier et supprimer des données.

DRF nous permet de réaliser ces deux types de contrôles au travers de la réécriture de méthodes sur le serializer :

    validate_XXX  où XXX est le nom du champ à valider ;
    validate  qui permet un contrôle global sur tous les champs du serializer.
Pour se faire
    -Validez les données d’un champ
    Dans les endpoints d’administration :

        Des serializers différents sont utilisés et les données retournées diffèrent ;
        Certains accès peuvent également être limités à certaines personnes authentifiées. 

        nouvel endpoint en le déclarant auprès de notre routeur.
    Maintenant que nous utilisons un Viewset, la création de catégorie est possible. C’est à la création que sert ce formulaire en nous permettant d'effectuer des actions POST. Les actions de mise à jour et de suppression sont disponibles sur les URL de détail des catégories.

    Validons à présent nos données, sans oublier que la création d’un doublon de catégorie ne doit pas être permis. Il nous faut pour cela modifier notre serializer de liste, car c’est lui qui est utilisé pour l’action create 

    La validation d’un champ unique se fait en écrivant la méthode validate_XXX  où XXX  est le nom du champ. Dans notre cas, validate_name:

    -Mettez en place une validation multiple
    
        Pour notre boutique, nous souhaitons optimiser le référencement et avoir un rappel du nom de la catégorie également présent dans la description. Nous pouvons effectuer automatiquement ce contrôle au travers d’une validation multiple.

        La validation entre champs se fait au travers de la méthode validate. Vérifions que le nom est bien présent dans la description :