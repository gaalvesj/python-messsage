import time

from selenium import webdriver;
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
print("Acessando o site...")
time.sleep(10)
print("Site acessado com sucesso!")
#login
username = driver.find_element(By.NAME, 'username')
username.send_keys('gaalvesj')
print("colocando o login!!")

time.sleep(10)

password = driver.find_element(By.NAME, 'password')
password.send_keys('20635342')
print("colocando senha");

time.sleep(5)

login = driver.find_element(By.CSS_SELECTOR, '._acan._acap._acas._aj1-')
login.click()
print("login feito");

time.sleep(10)


searchBox = driver.find_element(By.CLASS_NAME, 'x9f619 x3nfvp2 xr9ek0c xjpr12u xo237n4 x6pnmvc x7nr27j x12dmmrz xz9dl7a xn6708d xsag5q8 x1ye3gou x80pfx3 x159b3zp x1dn74xm xif99yt x172qv1o x10djquj x1lhsz42 xzauu7c xdoji71 x1dejxi8 x9k3k5o xs3sg5q x11hdxyr x12ldp4w x1wj20lx x1lq5wgf xgqcy7u x30kzoy x9jhf4c')
searchBox.click();

inputSearch = driver.find_element(By.CLASS_NAME, 'x1lugfcp x19g9edo x6umtig x1b1mbwd xaqea5y xav7gou x1lq5wgf xgqcy7u x30kzoy x9jhf4c x9f619 x5n08af xl565be x5yr21d x1a2a7pz xyqdw3p x1pi30zi xg8j3zb x1swvt13 x1yc453h xh8yej3 xhtitgo xs3hnx8 x1dbmdqj xoy4bel x7xwk5j')
inputSearch.send_keys("mantovaniluaa_")
time.sleep(5)
