import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(
        '/Users/felbushe/Desktop/Важное/Тестировщик QA Engiener/Школа Седого тестировщика/ДЗ/Репозитории/Pytest/Module_25/chromedriver')

    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends.skillfactory.ru/login')

    yield

    pytest.driver.quit()

@pytest.fixture()
### открывается авторизованная страница с питомцами
def show_my_pets():
    # Вводим email и пароль
    pytest.driver.find_element(By.ID, 'email').send_keys("testingfelapi@gmail.com")
    pytest.driver.find_element(By.ID, 'pass').send_keys("123")

    # Развертывание страницы во весь экран
    pytest.driver.maximize_window()

    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

    # Нажимаем на пункт меню "Мои питомцы"
    pytest.driver.find_element(By.XPATH, '//*[@href=\"/my_pets\"]').click()