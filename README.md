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