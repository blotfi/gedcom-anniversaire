# gedcom-anniversaire
Parse le fichier de généalogie au format gedcom .ged et envoie par email la liste des anniversaires du jour.
Egalement le premier du mois, envoi par email la liste de tous les anniversaires de ce mois.

L'envoi se fait à tous les emails d'une liste txt.

Dans mon cas, j'utilise [Ancestris](http://ancestris.org) pour gérer mon arbre généalogique. Un excellent logiciel gratuit. Le script fonctionne sur tout fichier .ged qui respecte la norme.

Vous devez rajouter deux fichiers

    email_list.txt
    tonfichier.ged

il faut que la bibliothèque **python-gedcom** soit installée sur le système

    pip3 install python-gedcom

et lancer le script python anniv.py  
Exécution manuelle :

    python3.6 /home/blofib/anniv/anniv.py

ou via un cron par exemple à 3h du matin :

    0 3 * * * python3.6 /home/blofib/anniv/anniv.py

sur un Raspberry PI

    /usr/bin/python3 /home/pi/Documents/py/anniv/anniv.py > /home/pi/Documents/py/anniv/anniv.log

ou via le CRON :

    0 3 * * * /usr/bin/python3 /home/pi/Documents/py/anniv/anniv.py > /tmp/anniv.log 2>&1
