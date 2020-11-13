from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time,conf


print("Starting")
gmailId=conf.EMAIL
passWord=conf.PASS
target=conf.target
captions=''
start_time=time.time()
elapsed_time=0
flag=0


opt = Options()
opt.add_argument("start-maximized")
opt.add_argument("--disable-infobars")
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })

#Logging in to Google account using geeks for geeks google sign-in as google doesn't allow direct sign-in through automated browsers
try:
	driver = webdriver.Chrome(options=opt) 
	driver.get('https://accounts.google.com/o/oauth2/auth/identifier?redirect_'+
		'uri=storagerelay%3A%2F%2Fhttps%2Fauth.geeksforgeeks.org%3Fid%3Dauth601'+
		'908&response_type=permission%20id_token&scope=email%20profile%20openid'+
		'&openid.realm&client_id=388036620207-3uolk1hv6ta7p3r9l6s3bobifh086qe1.'+
		'apps.googleusercontent.com&ss_domain=https%3A%2F%2Fauth.geeksforgeeks.'+
		'org&fetch_basic_profile=true&gsiwebsdk=2&flowName=GeneralOAuthFlow') 
	driver.implicitly_wait(5)

	loginBox=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="identifierId"]')))
	loginBox.send_keys(gmailId)


	nextButton=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id="identifierNext"]/div/button')))
	nextButton.click()


	passWordBox=WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH,'//*[@id ="password"]/div[1]/div / div[1]/input')))
	passWordBox.send_keys(passWord)


	nextButton=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH,'//*[@id ="passwordNext"]')))
	nextButton.click()
	print('Login Successfull')
except Exception as e:
	print("Login Failed",e)
	exit()



time.sleep(3)

#Joining Google Meet
driver.get(conf.meet)
dismiss=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.CLASS_NAME,'CwaK9' )))
driver.execute_script("arguments[0].click();", dismiss)

joinNow="//span[@class='NPEfkd RveJvd snByac' and contains(text(),'Join now')]"
askToJoin="//span[@class='NPEfkd RveJvd snByac' and contains(text(),'Ask to join')]"
time.sleep(5)
try:
	element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,askToJoin)))
	element.click()
except:
	element = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.XPATH,joinNow)))
	element.click()

time.sleep(1)
time_now=time.time()
while(elapsed_time<30 and flag!=1):
	elapsed_time=time.time()-time_now
	try:
		driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[7]/div[3]/div[9]/div[3]/div[2]/div/span/span/div/div[2]').click()
		flag=1
	except:
		time.sleep(5)

if flag==1:
	print("Joined the meeting")
else:
	print("Failed to join the meeting")
	driver.close()
	exit()




#Observing the Google meet conditions for a fall in number of participants or for name being called and then exiting if done so
while True:
	elapsed_time=time.time()-start_time
	element=WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='wnPUne N0PJ8e']")))
	number_of_participants=int(element.text)
	if(number_of_participants>conf.min_participants and elapsed_time>conf.min_time): ###Change kar dena
		print("Meeting over, exiting")
		endButton=driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[7]/div[3]/div[9]/div[2]/div[2]/div')
		driver.execute_script("arguments[0].click();", endButton)
		time.sleep(3)
		driver.close()
		exit()


	try:
		words=driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[7]/div[3]/div[5]/div/div[2]')
		captions+=(words.text).lower()
	except:
		pass
	if len(captions.split())>15:
		captions=captions.split(' ',len(captions.split())-15)[-1]
	for i in range(len(target)):
		if (target[i] in captions):
				print("Name called, exiting")
				endButton=driver.find_element_by_xpath('//*[@id="ow3"]/div[1]/div/div[7]/div[3]/div[9]/div[2]/div[2]/div')
				driver.execute_script("arguments[0].click();", endButton)
				time.sleep(3)
				driver.close()
				exit()

	time.sleep(3)



