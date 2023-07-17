from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()
url = "https://www.instagram.com/"
driver.get(url)

sleep(12)
# Login
user_name = driver.find_elements(By.TAG_NAME, "input")
user_name[0].send_keys("") # Nick
user_name[1].send_keys("") # Password
# Click login button
sleep(3)

login_button = driver.find_elements(By.TAG_NAME, "button")
login_button[-2].click()

sleep(15)
# Pass Save Login Information?
not_now_button = driver.find_element(By.XPATH, "//div[@role='button']").click()

sleep(25)
# Pass Open Notifications
not_now_button2 = driver.find_elements(By.TAG_NAME, "button")
not_now_button2[-1].click()

sleep(10)
# Go to profile
driver.get("https://www.instagram.com/") # Add your nick name

sleep(35)
# Click followers or following

#followers_button = driver.find_element(By.XPATH, "//a[@href='/Your Nick/following/']") #Following
followers_button = driver.find_element(By.XPATH, "//a[@href='/Your Nick/followers/']") #Followers
followers_button.click()

sleep(30)
# Scroll down
jscommand = """
followers = document.querySelector("._aano");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;

"""

lenOfPage = driver.execute_script(jscommand)
match=False

while(match==False):
    lastCount = lenOfPage
    sleep(3)
    lenOfPage = driver.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True

sleep(15)

# Print followers or following
followers = driver.find_elements(By.CSS_SELECTOR,".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.notranslate._a6hd")

for follower in followers:
    print("******************************")
    print(follower.text)

sleep(8)
driver.close()
