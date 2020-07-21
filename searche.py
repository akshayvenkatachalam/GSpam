from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
import csv

with open('names.csv', newline='', encoding="utf8") as f:
	reader = csv.reader(f)
	names = list(reader)

with open('doms.csv', newline='', encoding="utf8") as f:
	reader = csv.reader(f)
	doms = list(reader)

with open('branches.csv', newline='', encoding="utf8") as f:
	reader = csv.reader(f)
	branches = list(reader)

with open('dictionary.csv', newline='', encoding="utf8") as f:
	reader = csv.reader(f)
	words = list(reader)

def email(name):
	op = ''
	dom = random.choice(doms)
	for char in name:
		if char.isalnum():
			op += char
	return str(str(op) + '@' + str(dom[0]))

def name(): 
	name = random.choice(names)
	return str(name[0])

def dept():
	dept = random.choice(branches)
	return str(dept[0])

def insta(name):
	op = ''
	for char in name:
		if char.isalnum():
			op += char
	insta = str(str(op) + str(random.randint(1,100)))
	return insta

def desc():
	desc = ''
	for i in range(random.randint(5,50)):
		desc = desc + ' ' + (str(random.choice(words)[0]))
	return str(desc).lower()

'''
PROXY = "178.57.89.142:35943"
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,
    "proxyType": "MANUAL",
}
'''

driver = webdriver.Chrome()
while(1):
	driver.get("https://forms.gle/MF2WiCA31xdEcpMz9")
	time.sleep(2)
	name1 = name()
	textboxes = driver.find_elements_by_class_name("quantumWizTextinputPaperinputInput")
	para = driver.find_elements_by_class_name("quantumWizTextinputPapertextareaInput")
	submitbutton = driver.find_elements_by_class_name("appsMaterialWizButtonPaperbuttonContent")
	textboxes[0].send_keys(email(name1))
	textboxes[1].send_keys(name1)
	textboxes[2].send_keys(str(random.randint(19,23)))
	textboxes[3].send_keys(str(random.randint(00000000000,9999999999)))
	textboxes[4].send_keys(dept())
	textboxes[5].send_keys(insta(name1))
	para[0].send_keys(desc())
	time.sleep(5)
	submitbutton[0].click()
	time.sleep(2)
driver.close()