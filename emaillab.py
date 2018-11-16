#import smtplist
import smtplib
import getpass
myemail="kppathak2000@gmail.com"
recemail="kshitizpathak2000@gmail.com"
password=getpass.getpass()
s=smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login(myemail,password)
message="WHTAT'S GOINNG MAN ALL GOINNG WELL"
s.sendmail("kppathak2000@gmail.com","kshitizpathak2000@gmail.com",message)
s.quit()

