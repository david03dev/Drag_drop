from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


class DragAndDropDemo:

    def __init__(self, web_url):
        self.url = web_url
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start(self):
        # Maximize the browser window and load the page
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(2)  # Let the page load

    def perform_drag_and_drop(self):
        try:
            # Switch to the iframe that contains the drag-and-drop functionality
            iframe = self.driver.find_element(by=By.XPATH, value="//iframe[@class='demo-frame']")
            self.driver.switch_to.frame(iframe)

            # Locate the draggable (white rectangular box) and droppable (yellow rectangular box) elements
            draggable = self.driver.find_element(by=By.ID, value="draggable")
            droppable = self.driver.find_element(by=By.ID, value="droppable")

            # Perform drag and drop operation using ActionChains
            action = ActionChains(self.driver)
            action.drag_and_drop(draggable, droppable).perform()

            print("Drag and Drop operation completed successfully!")
        except Exception as e:
            print("An error occurred:", str(e))

    def shutdown(self):
        # Close the browser window
        self.driver.quit()


if __name__ == "__main__":
    url = "https://jqueryui.com/droppable/"
    drag_and_drop_demo = DragAndDropDemo(url)
    
    # Start the browser and perform drag and drop
    drag_and_drop_demo.start()
    drag_and_drop_demo.perform_drag_and_drop()
    
    # Close the browser
    sleep(3)
    drag_and_drop_demo.shutdown()
