#! /usr/bin/python3

from gedcom.element.individual import IndividualElement
from gedcom.parser import Parser
import datetime
import smtplib

# https://github.com/nickreynke/python-gedcom
# https://www.w3schools.com/python/python_datetime.asp
# http://naelshiab.com/tutorial-send-email-python/
# https://realpython.com/python-send-email/

emailfile = '/home/user/anniv/email_list.txt'
file_path = '/home/user/anniv/tonfichier.ged' # Path to your `.ged` file

today = datetime.datetime.today().strftime('%d %b %Y')
print ("Aujourd'hui : "+today)

#dt = datetime.datetime.today().strftime('%d %b').upper() 
year = int(datetime.datetime.today().strftime('%Y'))
month = datetime.datetime.today().strftime('%b').upper() 
day = int(datetime.datetime.today().strftime('%d'))

#month ='JAN' #debug
#day =10   #debug

gedcom = Parser()
gedcom.parse_file(file_path)
liste=""
liste_du_mois=""
found=0
all_records = gedcom.get_root_child_elements()
for record in all_records:
    if isinstance(record, IndividualElement):
      (birth_date, birth_place, birth_src) = record.get_birth_data()
      death_year = record.get_death_year()
      birth_date_split = birth_date.split(' ', 2)
      #print (birth_date_split)
      if len(birth_date_split)>=2:
        try:  
          birth_day = int(birth_date_split[0])
        except:
          birth_day = 0
          
        birth_th_mounth_ = birth_date_split
        birth_mounth = birth_date_split[1]
        if (birth_mounth == month):
          (first, last) = record.get_name()
          foundmois=0
          if death_year!=-1:
            #print ("===>"+ str(int(year)-death_year))
            if (year-death_year)<101:    #il y a moins de 100 ans on affiche
              liste_du_mois = liste_du_mois + "<b>"+first+"</b> " + last+ " : "\
              +  birth_date+ ', <font color="#0000ff">décédé(e)</font> en '+ str(death_year) +"<br>\n";
              foundmois=1
          else:
            foundmois=1
            liste_du_mois = liste_du_mois + "<b>"+first+"</b> "+ last+ " : "+  birth_date + "<br>\n";
          #parents:
          if foundmois:
            parents = gedcom.get_parents(record) #record.get_parent_element()
            liste_du_mois = liste_du_mois + "&nbsp;&nbsp;&nbsp;&nbsp;parents : "
            for p in parents:
              (pfirst, plast) = p.get_name()
              (pbirth_date, pbirth_place, pbirth_src) = p.get_birth_data()
              liste_du_mois = liste_du_mois + pfirst + " " + plast+'('+pbirth_date+')&nbsp;&nbsp;'
            liste_du_mois = liste_du_mois +  "<br>\n";

          
        if (birth_day == day and birth_mounth == month):
          (first, last) = record.get_name()
          if death_year!=-1:
            if (year-death_year)<101:    #il y a moins de 20 ans on affiche
              liste = liste + "<b>"+first+"</b> "+ last+ " : "\
               +  birth_date+ ', <font color="#0000ff">décédé(e)</font> en '+ str(death_year) +"<br>\n";
              found=1
          else:
            liste = liste + "<b>"+first+"</b> "+ last+ " : "+  birth_date+"<br>\n";
  #debug
            print ("individu :"+ first + " " + last)
            found=1
          #parents:
          if found:
            parents = gedcom.get_parents(record) #record.get_parent_element()
            liste = liste + "&nbsp;&nbsp;&nbsp;&nbsp;parents : "
            for p in parents:
              (pfirst, plast) = p.get_name()
              (pbirth_date, pbirth_place, pbirth_src) = p.get_birth_data()
              liste = liste + pfirst + " " + plast+'('+pbirth_date+')&nbsp; '
            liste = liste +  "<br>\n";
          
##print ("____Anniversaire du mois____")
##print(liste_du_mois)
##print ("____Anniversaire du jour____")
##print(liste)
        
print ("____emails____")
liste_emails = []
try:  
  fp = open(emailfile)
  for cnt, line in enumerate(fp):
    #print("Line {}: {}".format(cnt, line.strip()))
    liste_emails.append(line.strip())
finally:  
  fp.close()
print (liste_emails)
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("tongmail@gmail.com", "tonpassword")

if day==1:
  msg ="""\
Subject: Anniversaires du mois
Content-Type: text/html; charset=utf-8
Content-Disposition: inline
Content-Transfer-Encoding: 8bit

<font color='#ff0000'><u>La liste des anniversaires de ce mois est :</u></font><br>
"""
  msg=msg+liste_du_mois+"<br><br>\n\n"  #.encode('utf-8')
  
else:
  msg ="""\
Subject: Anniversaire du jour
Content-Type: text/html; charset=utf-8
Content-Disposition: inline
Content-Transfer-Encoding: 8bit

"""
msg1 =""" 
<font color='#ff0000'><u>La liste des anniversaires d'aujourd'hui est :</u></font><br>
"""
msg=msg+msg1+liste
if found==1:
  server.sendmail("tongmail@gmail.com", liste_emails, msg.encode('utf-8'))
server.quit()

print(msg)
