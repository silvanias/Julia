from selenium import webdriver
from PIL import Image
from io import BytesIO
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.headless = True
fox = webdriver.Firefox(options=options)
fox.get('http://127.0.0.1:8000/login')
email = fox.find_element(By.ID, "email")
password = fox.find_element(By.ID, "password")

email.send_keys("silas@gmail.com")
password.send_keys("password")

fox.find_element(By.XPATH, '/html/body/form/button').click()
fox.get('http://127.0.0.1:8000/gen')


# now that we have the preliminary stuff out of the way time to get that image :D
element = fox.find_element(By.XPATH, '/html/body/section/div/div[3]/img') # find part of the page you want image of
fox.execute_script("arguments[0].scrollIntoView(true);", element)

location = element.location
size = element.size
png = fox.get_screenshot_as_png() # saves screenshot of entire page
fox.quit()

im = Image.open(BytesIO(png)) # uses PIL library to open image in memory


left = location['x']
top = location['y'] - size['height'] * 0.4
right = location['x'] +  size['width'] * 1 
bottom = location['y'] +  size['height'] * 0.5 


im = im.crop((left, top, right, bottom)) # defines crop points
im.save('reference.png') # saves new cropped image
