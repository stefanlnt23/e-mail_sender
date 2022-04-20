
from ast import Break
import json
import random
from tqdm import tqdm
import smtplib
import random
import progressbar
import time
EMAIL_ADDRESS = '>YOUR_EMAIL_ADDRESS<'
EMAIL_PASSWORD = '>YOUR_EMAIL_PASSWORD<'

k = 0
try:

    o = int(input('NR E-MAILS: '))
    file = open('my_dictionary.json')
    data = json.load(file)
    send_to = input('DESTINATARY: ')
    while k<o:
        k +=1
        remains = o-k
        for i in data['receipe']:
            x = receipe, ingredients = random.choice(list(i.items())) 
            random_subject = x[0]
            random_body = x[1]
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:

                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login (EMAIL_ADDRESS, EMAIL_PASSWORD)
                g = 'RE: '+ str(k) +'     '+str(x[0])
                msg = f'Subject: {g} \n\n{random_body}'
                smtp.sendmail(EMAIL_ADDRESS,send_to,msg)
            with progressbar.ProgressBar(max_value=10) as bar:
                for i in range(10):
                    time.sleep(0.5)
                    bar.update(i)

            print ('Email number: ',k,'has been sent ',remains,'emails left')
        except smtplib.SMTPRecipientsRefused:
            print ('ERROR DESTINATARY E-MAIL NOT FOUND!')
            break
except ValueError:
    print('ERROR ONLY NUMBERS ALLOWED!')
except smtplib.SMTPAuthenticationError:
    print('ERROR E-MAIL OR PASSWORD IS INCORRECT!')
