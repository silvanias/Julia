from selenium import webdriver
from PIL import Image
from io import BytesIO
import cv2
from selenium.webdriver.common.by import By
import numpy as np
from selenium.webdriver.firefox.options import Options


def test_selenium_screenshot():
    # Set up selenium driver
    options = Options()
    options.headless = True
    fox = webdriver.Firefox(options=options)
    fox.get('http://127.0.0.1:8000/login')
    
    # Login to test account
    email = fox.find_element(By.ID, "email")
    password = fox.find_element(By.ID, "password")
    email.send_keys("silas@gmail.com")
    password.send_keys("password")
    fox.find_element(By.XPATH, '/html/body/form/button').click()

    fox.get('http://127.0.0.1:8000/gen')

    # Locate mandelbrot to screenshot
    element = fox.find_element(By.XPATH, '/html/body/section/div/div[3]/img')
    fox.execute_script("arguments[0].scrollIntoView(true);", element)
    location = element.location
    size = element.size

    # Saves screenshot of entire page
    png = fox.get_screenshot_as_png() 
    fox.quit()

    # uses PIL library to open image in memory
    im = Image.open(BytesIO(png)) 

    # define crop points
    left = location['x']
    top = location['y'] - size['height'] * 0.4
    right = location['x'] +  size['width'] * 1 
    bottom = location['y'] +  size['height'] * 0.5 

    im = im.crop((left, top, right, bottom))
    im.save('screenshot.png')

    # Load images
    image = cv2.imread('screenshot.png')    
    reference = cv2.imread('reference.png')

    # Compute MSE between images
    mse = np.sum((image.astype("float") - reference.astype("float")) ** 2)
    mse /= float(image.shape[0] * image.shape[1])

    # MSE == 0 means images are identical
    assert mse == 0
