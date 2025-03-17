# This code snippet automates the process of sending connection requests on LinkedIn.
# It uses the Selenium library to interact with the LinkedIn website, locate the connect buttons, and click on them to send connection requests.
# You can customize the script by replacing the placeholders with your email, password, and search query.
#try it in your unofficial LinkedIn account to avoid any problems with your account.
# This code snippet is for educational purposes only and should be used responsibly.
# You can also add additional error handling and logging to make the script more robust.
# If you have any questions or need further assistance, feel free to ask.
# Hope this helps!





from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-usb")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--disable-software-rasterizer")  # Further GPU fix
chrome_options.add_argument("--headless")  # (Optional) Run Chrome in headless mode




driver = webdriver.Chrome()



try:
    driver.get("https://www.linkedin.com/login")
    EMAIL = "s_boudiaf@estin.dz"
    PASSWORD = "Mehdi@BDF2005"
    driver.find_element(By.ID, "username").send_keys(EMAIL)
    driver.find_element(By.ID, "password").send_keys(PASSWORD)
    driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
    time.sleep(5)

    driver.get("https://www.linkedin.com/mynetwork/grow/?skipRedirect=true")
    time.sleep(8)


    show = driver.find_element(By.XPATH, "//button[@data-view-name='cohort-section-see-all']").click()
    time.sleep(10)

    connect_buttons = driver.find_elements(By.XPATH, "//button[@class='yyosfl1 h8e4ml0 _1xoe5hd0 _139m7k1gx _1s9oaxg7 _1s9oaxgi yyosfl4 yyosfl3 cnuthtc0 cnutht0 cnutht1i0 _1k2lxmew _1ptbkx61go']")
    
    for button in connect_buttons:
            try:
                button.click()
                print("Connection request sent")
                time.sleep(1)
            except Exception as e:
                print(f"An error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit()
