from selenium import webdriver
import time
import pywhatkit
from firebase import firebase
from datetime import datetime


firebas=firebase.FirebaseApplication("https://linkedin-job-searcher-default-rtdb.firebaseio.com/",None)

#give the path of the chromedriver
browser=webdriver.Chrome(executable_path='C:/Users/Vikram/chromedriver.exe')
browser.get("https://www.linkedin.com")


username=browser.find_element_by_id("session_key")
#give your linkedin username
username.send_keys('your-username')


password=browser.find_element_by_id("session_password")
#give your linkedin password
password.send_keys('your-password')

login_button=browser.find_element_by_class_name("sign-in-form__submit-button")
login_button.click()

c=0
#Scrolling the page 50 times
while(c<50):
    browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
    #You can change the sleep time
    time.sleep(1)
    c+=1
p=0 
s=""   
l=[]


#give your firebase path
resultdata=firebas.get('/linkedin-job-searcher-default-rtdb/dataSample','')

for i in resultdata:
    l.append(resultdata[i]['hello'])
job=browser.find_elements_by_class_name('break-words')


for i in job:
    k=i.get_attribute('innerText').lower()
    #You can add any number of tags
    jobslist=['#hiring','#hiringalerts','#recruitment','#jobsearch','#jobopportunity']


    posttext=k.split()
    p=0


    for z in range(len(posttext)):
        posttext[z]=posttext[z].lower()  


    for word in jobslist:
        if word in posttext:
            p=1


    if(p==1):
        if k not in l:
            data={'hello':k}
            firebas.post('/linkedin-job-searcher-default-rtdb/dataSample',data)       
            s+=k
            s+='\n'
            s+='\n\n\n\n\n'
            s+='------------------------------------------------------\n'


now = datetime.now()
#print(s)

current_time = now.strftime("%H:%M:%S")
tiim=current_time.split(':')
hr=int(tiim[0])
minute=int(tiim[1])  

if(minute==58):
    minute=1
elif(minute==59):
    minute=2 
else:
    minute+=3
    
#Sending message to whatsapp using pywhatkit   
pywhatkit.sendwhatmsg('+91yourmobileNumber',s,hr,minute)
           
        

               
   