from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from traceback import print_stack
import time



class SeleniumDriver():

    def __init__(self,driver):
        self.driver = driver


    def getByType(self, loctorType):
            loctorType = loctorType.lower()
            if(loctorType == "id"):
                 return By.ID
            elif(loctorType == "xpath"):
                 return By.XPATH
            elif (loctorType == "name"):
                 return By.NAME
            elif(loctorType == "class"):
                 return By.CLASS_NAME
            elif(loctorType == "css"):
                 return By.CSS_SELECTOR
            elif(loctorType == "link"):
                 return By.LINK_TEXT
            elif(loctorType == "plink"):
                 return By.PARTIAL_LINK_TEXT
            else:
                print("Locator Type " + loctorType + "not correct / supported!")
            return False


    def getElement(self,locator,locatorType="id"):
        element = None

        try:
            locatorType = locatorType.lower()
            byType = self.getByType(locatorType)
            element = self.driver.find_element(byType,locator)
            print("Element found")
        except:
            print("Element not found")
        return element




    def elementClick(self,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            element.click()
            print(" Clicked  on element " + locator + "locator type: "+locatorType)
        except:
            print(" Cannot click  on element " + locator + "locator type: " + locatorType)
            print_stack()



    def sendKeys(self,data ,locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            print(" Send data  on element " + locator + "locator type: " + locatorType)
        except:
            print(" Cannot send data  on element " + locator + "locator type: " + locatorType)
            print_stack()



    def elementPresentCheck(self,locator,byType):

        try:
            elementlist = self.driver.find_elements(byType,locator)
            if(len(elementlist)>0):
                print("Element found")
                return True
            else:
                print("Element not found")
                return False
        except:
            print("Element not found")
            return False




    def waitForElement(self,locator,locatorType="id",timeout=10,pollFreq=0.5):
        element = None

        try:

            byType = self.getByType(locatorType)
            print("waiting for maximum :: "+ str(timeout)+ ":: seconds for element to be clickable")

            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFreq,
                                 ignored_exceptions=[NoSuchElementException, ElementNotVisibleException,
                                                     ElementNotSelectableException])

            element = wait.until(EC.element_to_be_clickable((byType, locator)))

            print("Element appered on the web page ")
        except:
            print("Element not appeared on the web page")
            print_stack()
        return element

    def take_Screenshot(self, driver):
        # fileName = str(round(time.time() * 1000)) + ".png"
        fileName = "snapShot.png"
        dir = "../screenshots/"
        driver.save_screenshot(dir + fileName)



