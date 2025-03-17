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



driver = webdriver.Chrome()



try:
    driver.get("https://www.linkedin.com/login") # Open LinkedIn login page
    EMAIL = "YOUR EMAIL"
    PASSWORD = "YOUR PASSWORD"
    driver.find_element(By.ID, "username").send_keys(EMAIL) 
    driver.find_element(By.ID, "password").send_keys(PASSWORD) 
    driver.find_element(By.ID, "password").send_keys(Keys.RETURN)
    time.sleep(5) # Wait for the page to load

    search_query = "YOUR SEARCH QUERY" 
    driver.get(f"https://www.linkedin.com/search/results/people/?keywords={search_query}") #open search query
    time.sleep(5)

    connect_buttons = driver.find_elements(By.XPATH, "//button[@class='artdeco-button artdeco-button--2 artdeco-button--secondary ember-view']") # Find all connect buttons

    for button in connect_buttons:
        try:
            button.click() # Click the connect button
            print("Connection request sent") # Print a message to check 
            time.sleep(1) #to avoid spamming
        except Exception as e:
            print(f"An error occurred: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    driver.quit() #close the browser




