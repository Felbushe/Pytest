import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_all_my_pets(show_my_pets):
    '''Тест на присутствие всех питомцев пользователя на странице'''

    WebDriverWait(pytest.driver, 5).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr')))

    # Общее кол-во питомцев на странице
    pets = pytest.driver.find_elements (By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr')
    all_pets = len(pets)

    # Число питомцев из информации пользователя
    list_of_pets = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
    num_pets = list_of_pets[0].text.split('\n')
    num_pets = num_pets[1].split(' ')
    num_pets = int(num_pets[1])

    # Сравниваем, кол-во питомцев на странице должно быть равно кол-ву в информации пользователя
    assert all_pets == num_pets


def test_different_name(show_my_pets):
    '''Тест на уникальность имени'''

    # Информация обо всех именах питомцах
    pytest.driver.implicitly_wait(10)
    name = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody > tr > td:nth-child(2)')

    # Проверяем на уникальность имени (отсутствие повторений)
    assert len(set(name)) == len(name)


def test_different_pets(show_my_pets):
    '''Тест на уникальность питомцев'''

    # Получаем информацию обо всех питомцах
    pet_info = pytest.driver.find_elements(By.CSS_SELECTOR, '.table.table-hover tbody tr')

    # Оставляем имя, возраст и породу из pet_info. Остальное меняем на пустые строки и разделяем пробелами.
    list_info = []
    for i in range(len(pet_info)):
        data_pet = pet_info[i].text.replace('\n', '').replace('×', '')
        split_data_pet = data_pet.split(' ')
        list_info.append(split_data_pet)

    # Склеиваем данные из pet_info. Склейки добавляем в строку разделяем пробелами
    line = ''
    for i in list_info:
        line += ''.join(i)
        line += ' '

    # Получаем список из строки line
    list_line = line.split(' ')

    # Превращаем список в множество
    set_list_line = set(list_line)

    # Находим количество элементов списка и множества
    a = len(list_line)
    b = len(set_list_line)

    # Из количества элементов списка вычитаем количество элементов множества
    result = a - b

    # Если количество элементов == 0 значит карточки с одинаковыми данными отсутствуют
    assert result == 0


def test_have_full_info(show_my_pets):
    '''Тест на наличие у всех питомцев возраста, имени, породы'''

    # Получаем информацию обо всех питомцах
    pytest.driver.implicitly_wait(10)
    pets = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody tr')

    # Оставляем имя, возраст и породу из pets. Остальное меняем на пустые строки и разделяем пробелами.
    # Находим количество элементов в получившемся списке и сравниваем их с ожидаемым результатом
    for i in range(len(pets)):
        info_pets = pets[i].text.replace('\n', '').replace('×', '')
        split_info_pets = info_pets.split(' ')
        result = len(split_info_pets)
        assert result == 3


def test_have_photo(show_my_pets):
    '''Тест на наличие фото минимум у половины питомцев'''

    # Общее кол-во питомцев и их фото
    pytest.driver.implicitly_wait(10)
    pets_photo = pytest.driver.find_elements(By.CSS_SELECTOR, '#all_my_pets > table > tbody img')

    # Число питомцев из информации пользователя
    list_of_pets = pytest.driver.find_elements(By.CSS_SELECTOR, ".\\.col-sm-4.left")
    num_pets = list_of_pets[0].text.split('\n')
    num_pets = num_pets[1].split(' ')
    num_pets = int(num_pets[1])

    # Питомцы без фото
    half_pets = num_pets // 2
    count = 0
    for i in range(len(pets_photo)):
        if pets_photo[i].get_attribute('src') != '':
            count += 1

    # Количество питомцев с фотографией больше или равно половине количества питомцев
    assert len(pets_photo) >= half_pets