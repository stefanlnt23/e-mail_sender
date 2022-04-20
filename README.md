# Recipe sender

### Send E-mails with food recipes to your friends you can edit the "my_dictionary.json" file with what recipes you want
![alt text](https://github.com/stefanlnt23/e-mail_sender/blob/main/img/x3.png "Text2")

## Modules required:

```python
pip install ast 
pip install json
pip install random
pip install tqdm 
pip install smtplib
pip install random
pip install progressbar
pip install time
```

## Explication:
### Step 1
#### Import modules 
```python

from ast import Break
import json
import random
from tqdm import tqdm
import smtplib
import random
import progressbar
import time
```
### Step 2
#### Create variables with your e-mail credentials
```python
EMAIL_ADDRESS = 'YOUR_EMAIL_ADDRESS'
EMAIL_PASSWORD = 'YOUR_EMAIL_PASSWORD'
```
### Step 3
### Variables for while loop
```python
k = 0
# If user input's wrong ValueType catch the error
try:

    o = int(input('NR E-MAILS: '))
```
### Step 4
### Opening JSON file
```python
    file = open('my_dictionary.json')
```
### Step 5
### Defining dictionary
```python
    data = json.load(file)
 ```
 ### Step 6
### While loop
```python
    send_to = input('DESTINATARY: ')
    while k<o:
        k +=1
        remains = o-k
```
### Step 7
### Iterating through the json
```python
        for i in data['receipe']:
```
```python
# Chosing random string
            x = receipe, ingredients = random.choice(list(i.items())) 
```
### Step 8
### Defining index values
```python
            random_subject = x[0]
            random_body = x[1]
```
### Step 9
### Send email
```python
        try:
            with smtplib.SMTP('smtp.gmail.com', 587) as smtp:

                smtp.ehlo()
                smtp.starttls()
                smtp.ehlo()
                smtp.login (EMAIL_ADDRESS, EMAIL_PASSWORD)
                g = 'RE: '+ str(k) +'     '+str(x[0])
                msg = f'Subject: {g} \n\n{random_body}'
                smtp.sendmail(EMAIL_ADDRESS,send_to,msg)
```
### Step 10
### Progress bar animation
```python
            with progressbar.ProgressBar(max_value=10) as bar:
                for i in range(10):
                    time.sleep(0.5)
                    bar.update(i)
```
### Step 11
### Confirmation
```python
            print ('Email number: ',k,'has been sent ',remains,'emails left')
```
### Step 12
### IF email not found break the loop
```python
        except smtplib.SMTPRecipientsRefused:
            print ('ERROR DESTINATARY E-MAIL NOT FOUND!')
            break
```
### Step 13
### IF nr of emails not int throw error
```python
except ValueError:
    print('ERROR ONLY NUMBERS ALLOWED!')
```
### Step 14
### IF E-mail or Password is incorrect throw error
```python
except smtplib.SMTPAuthenticationError:
    print('ERROR E-MAIL OR PASSWORD IS INCORRECT!')
```
# In order for this script to work you need to insert e-mail credentials
* If your e-mail has 2 factors authentification activated [Click here](https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmyaccount.google.com%2Fapppasswords&osid=1&rart=ANgoxccqxZEcQ-iajblFG-Oigddioy7bHWE2jf7kI1K252-AmIOGCk3cDSrzFfYgYT7Zjgg11sykG_yVEwnWGHKT9TxMUYjQBQ&service=accountsettings&flowName=GlifWebSignIn&flowEntry=ServiceLogin) , and follow these steps:

![alt text](https://github.com/stefanlnt23/e-mail_sender/blob/main/img/x1.png "img x1")


![alt text](https://github.com/stefanlnt23/e-mail_sender/blob/main/img/x2.png "img x2")

 create an "app" password wich python will use to log in and send e-mails


* If your e-mail does'nt have 2 factors authentification activated [Click here](https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4Pplz1tcmHd2l4oMIT-uxobFlFefVkQBF27koccYycwlRpFB7_bvrCgE9_rChUKte5pf6JyrCU4y56cDLOwVBBqnuZVag) and swich "Less secure apps acces" to allow  ![alt text](https://github.com/stefanlnt23/e-mail_sender/blob/main/img/123.png "Text2")



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
