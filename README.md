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

#------------les action----------#
    Vous devez penser Action chaque fois qu’un besoin fait référence à une entité, mais que le verbe ne correspond pas à un élément du CRUD. Par exemple, dans « Nous souhaitons que nos visiteurs puissent liker des publications », l’entité est la publication et l’action est liker.

    @Ainsi, la réalisation d’un POST sur l'endpointhttp://127.0.0.1:8000/api/category/2/disable/  aura pour effet de :

    Désactiver la catégorie, ce qui ne rendra plus visible la catégorie sur l'endpointhttp://127.0.0.1:8000/api/category/.
    Désactiver les produits de cette catégorie, ce qui ne rendra plus visible ces produits sur l'endpoint http://127.0.0.1:8000/api/product/.

#------------- Resume sur actions --------#
    Il est possible de créer d’autres actions en dehors de celles du CRUD.
DRF met à disposition un décorateur action  qui permet de créer de nouvelles actions.
Les actions peuvent être mises en place sur les URL de liste et de détail d’un endpoint.
Les actions peuvent utiliser n’importe quelle méthode HTTP (GET, POST, PATCH, DELETE…).

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


#-----------Cloisonnez vos tests-------#

il existe un cas compliqué à tester, lorsque nous sommes consommateurs d’une API.

    Lors de l’exécution des tests, nous ne souhaitons pas que les appels soient réalisés. Cela pourrait créer des données incohérentes sur le système cible, ou empêcher simplement certains tests si, par exemple, la création de doublons de noms n’est pas permise (comme nous l’avons mis en place dans la partie précédente !). Et imaginez que l’API tierce soit payante, alors chaque exécution d’un test serait alors facturée.

    Pour pallier cela, il existe ce qu’on appelle des mocks.

    Un mock se base sur le principe du Monkey Patching, c'est-à-dire modifier une section de code pour une durée limitée, sans toucher à sa version originale. Dans le cas d’un mock, cela veut dire que lors de l'exécution du test qui réalise l’appel, nous allons Monkey Patcher l’appel réseau, et simuler une réponse qui correspond à notre cas de test.

    Comme un exemple vaut mille mots, voyons cela tout de suite !

Appelez une API externe

    Donnons aux consommateurs encore plus de détails sur nos produits grâce à Open Food Facts, une base de données sur les produits alimentaires. Nous allons extraire l’écoscore de cet appel et le retourner dans notre endpoint de détail d’un produit.

    Mettons en place un appel à l’API d’Open Food Facts sur un produit spécifique. L’appel sera réalisé sur l’URL

    https://world.openfoodfacts.org/api/v0/product/3229820787015.json

    Réalisons cet appel et retournons les données dans un nouvel attribut nommé ecoscore. Nous verrons ensuite comment résoudre la problématique de l’appel tiers dans nos tests.

    Commençons par ajouter requests  à nos dépendances pour réaliser l’appel.

    Modifions notre serializer de liste de produits pour qu’il retourne l’écoscore.

    Les propriétés de model peuvent être ajoutées directement dans la liste des 
    champs des serializers, ils sont alors considérés comme en lecture seule.

    Mocker les appels API externes est tout aussi important que de tester sa propre API. Cela permet de tester les différents comportements que peuvent avoir les API partenaires. N’hésitez pas à tester des erreurs comme des 500 ou des Timeouts, un problème de réseau ou de SI Partenaire ne doit jamais mettre en péril votre propre SI.
    
En résumé
    Une API peut très bien faire des appels à d’autres API.
    Lors d’un appel à une API externe, il faut prévoir que cette API puisse ne pas répondre, afin d’éviter que notre API ne fonctionne plus.
    Lors d’un appel à une API externe, il faut mettre en place un mock pour pouvoir tester dans tous les cas d’usage, même sans connexion Internet.
    Dans cette partie, nous avons rendu nos endpoints plus performants et avons mis notre API à l’épreuve de tests grâce aux mocks. Avant de sécuriser notre API avec l’authentification, validez vos acquis de cette partie dans le quiz ! Je vous attends dans la partie 3 !

#------------------Ajoutez l’authentification des utilisateurs----------#

Un JWT est constitué de 3 parties séparées par un point. Par exemple ce JWT : 
 eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYyODk0ODE0NSwianRpIjoiODBmZTA4MDkxM2UxNDBjYmEwMDU4YWY4YmM5NjllZjYiLCJ1c2VyX2lkIjoxfQ.l31cs5pTApiR9R9s8pZaeyHIJuTmjcs07fxSqSpj1fQ

Chaque partie est encodée en base64, il est possible d’utiliser jwt.io pour les déchiffrer :

@ Le header, qui est en général constitué de deux attributs, indique le type de token et l'algorithme de chiffrement utilisé.
Une fois décodé :
{
    "typ": "JWT",
    "alg": "HS256"
}
@ Le payload contient les informations utiles que nous souhaitons faire transiter entre le serveur et le client.
Une fois décodé :
 {
    "token_type": "refresh",
    "exp": 1628948145,
    "jti": "80fe080913e140cba0058af8bc969ef6",
    "user_id": 1
}

@ La signature est un élément de sécurité permettant de vérifier que les données n’ont pas été 
modifiées entre les échanges client-serveur. La clé permettant la génération de cette signature 
est stockée sur le serveur qui fournit le JWT (elle est basée sur la SECRET_KEY de Django).

- La librairie Simple JWT va nous permettre d’authentifier nos utilisateurs et de leur fournir une paire de JWT :

    Un access_token  qui va permettre de vérifier l’identité et les droits de l’utilisateur. Sa durée de 
    vie est limitée dans le temps ;
    Un refresh_token  qui va permettre d’obtenir une nouvelle paire de tokens une fois que l’ access_token  sera expiré.

- Deux endpoints vont donc être mis à disposition par djangorestframework-simplejwt  :

    Un endpoint d’authentification ;
    Un endpoint de rafraîchissement de token.

NB: 
    Pour rappel, une classe d’authentification dans Django permet de définir 
    l’utilisateur à l’origine de la requête. 
    C’est elle qui attache le user  à la requête avec l’attribut request.user  
    si l'utilisateur a prouvé son authentification.

En résumé:
    @ Les JWT permettent de transférer des informations du client au serveur en plus des jetons d’authentification.
    @ djangorestframework-simplejwt  est une librairie permettant de gérer l’authentification,  
      mais il en existe d’autres également conseillées par DRF.
    @ Deux nouveaux endpoints d’obtention et de rafraîchissement de tokens fournis par Simple JWT  
      permettent de gérer l’authentification de nos utilisateurs.



#--------------Donnez des accès avec les tokens--------#

- Le token d’accès a une durée de vie limitée dans le temps ; si nous décodons son payload en utilisant par exemple jwt.io :

    {
        "token_type": "access",
        "exp": 1628927720,
        "jti": "63e4e6dab0494aee803fed93f24a80c1",
        "user_id": 1
    }

- nous pouvons voir différentes informations :

    @ token_type :  indique le type de token ;
    @ exp :  est un timestamp indiquant jusqu’à quand ce token peut être utilisé ;
    @ jti :  signifie JWT ID, c’est un identifiant unique créé lors de la génération du token ;
    @ user_id :  est l’identifiant Django de l’utilisateur, il est ajouté par Simple JWT lors de la génération du token.


- la durée de vie des tokens peut être configurée dans les settings de Django.

    SIMPLE_JWT = {
        'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
        'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    }
- Rafraîchissez des tokens
    Lorsque le token d’accès n’est plus valide, il est nécessaire d’en créer un autre. 
    C’est à cela que sert le token de rafraîchissement.

    Il faut pour cela réaliser un appel en POST sur l’endpoint de rafraîchissement de tokens. 
    Le token de rafraîchissement doit être transmis dans le corps de la requête sous l’attribut refresh, 
    et un nouveau token d’accès est alors retourné par le serveur.

En résumé:

    -  Les tokens JWT sont un moyen d’assurer l’authentification des utilisateurs.
    - Les tokens d’accès et de rafraîchissement sont à conserver précieusement par les applications 
      clientes pendant la session des utilisateurs.
    - Deux endpoints différents permettent d’une part l’obtention de tokens, 
      et d’autre part le rafraîchissement du token d’accès.    

#--------Restreignez l'accès à certains endpoints--------#

- Lors de la création d’un endpoint, il est important de penser à son accès, car il retourne 
peut-être des informations confidentielles ou permet des actions qui ne doivent pas être permises à tout le monde.

- Les permissions permettent la mise en place de règles de contrôle strictes. 
Avoir une permission par « acteur » (clients, partenaires, utilisateurs, 
administrateurs, etc.) de notre API est un bon moyen de gérer qui peut accéder à quels endpoints.

En résumé:

-Les permissions permettent de limiter l’accès aux endpoints.
-DRF fournit certaines permissions, mais il est possible de créer les nôtres.
-Disposer une permission par acteur permet de facilement savoir sur quels endpoints les permissions doivent être placées.
-Lors de la mise en place d’un nouvel endpoint, il est important de savoir qui va l’utiliser, 
 pour déterminer s’il doit rester public ou doit posséder certaines permissions.