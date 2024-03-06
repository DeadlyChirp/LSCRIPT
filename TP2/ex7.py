'''


La taille initiale d'une liste vide en Python est de 56 octets.
Lorsque nous commençons à ajouter des éléments dans la liste,
la taille de la liste augmente par paliers, ce qui reflète la stratégie d'allocation
de mémoire dynamique de Python pour les listes.

Voici l'évolution de la taille de la liste après l'ajout de certains nombres d'éléments :

Après l'ajout de 1 élément : 88 octets
Après l'ajout de 10 éléments : 184 octets
Après l'ajout de 20 éléments : 256 octets
Après l'ajout de 30 éléments : 336 octets
Après l'ajout de 40 éléments : 424 octets
Après l'ajout de 50 éléments : 520 octets
Après l'ajout de 60 éléments : 632 octets
Après l'ajout de 70 éléments : toujours 632 octets (la liste avait déjà pré-alloué de l'espace pour de futurs éléments)
Après l'ajout de 80 éléments : 760 octets
Après l'ajout de 90 éléments : 904 octets
Après l'ajout de 100 éléments : toujours 904 octets

La taille finale de la liste après l'ajout de 100 éléments est de 904 octets.
 Cela montre que Python ne réalloue pas de la mémoire pour chaque nouvel élément ajouté ;
  il alloue de l'espace supplémentaire à l'avance pour minimiser le nombre de réallocations nécessaires.
  Cela permet d'assurer que, bien que certaines opérations d'ajout puissent être coûteuses en raison de
  la nécessité de réallouer et de copier des éléments, le coût moyen reste constant,
  ce qui permet aux listes d'opérer efficacement même en ajoutant de nombreux éléments.

'''