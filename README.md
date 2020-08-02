# gedcom-anniversaire / birthday
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

    python3.6 /home/user/anniv/anniv.py

ou via un cron par exemple à 3h du matin :

    0 3 * * * python3.6 /home/user/anniv/anniv.py

sur un Raspberry PI

    /usr/bin/python3 /home/pi/Documents/py/anniv/anniv.py > /home/pi/Documents/py/anniv/anniv.log

ou via le CRON :

    0 3 * * * /usr/bin/python3 /home/pi/Documents/py/anniv/anniv.py > /tmp/anniv.log 2>&1

___ 
####_English explanations_

Parse the genealogy file of a gedcom .ged format and email the list of birthdays for the day.
Also on the first of the month, it emails the list of all birthdays for that month.

email are sents to all the destinators of a txt list.

In my case, I use [Ancestris] (http://ancestris.org) to manage my family tree. Great free software. The script works on any .ged file that meets the standard.

You must add two files

    email_list.txt
    tonfichier.ged

the ** python-gedcom ** library must be installed on the system

    pip3 install python-gedcom

and run the anniv.py python script
Manual execution:

    python3.6 /home/user/anniv/anniv.py

or via a cron for example at 3 am:

    0 3 * * * python3.6 /home/user/anniv/anniv.py

on a Raspberry PI

    /usr/bin/python3 /home/pi/Documents/py/anniv/anniv.py > /home/pi/Documents/py/anniv/anniv.log

ou via a CRON :

    0 3 * * * /usr/bin/python3 /home/pi/Documents/py/anniv/anniv.py > /tmp/anniv.log 2>&1
