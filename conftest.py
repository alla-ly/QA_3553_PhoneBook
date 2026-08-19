import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    #driver.implicitly_wait(5) #неявное ожидание
    driver.maximize_window() #открыв. на весь размер экрана

    driver.get("https://telranedu.web.app/home")

    yield driver

    driver.quit()

