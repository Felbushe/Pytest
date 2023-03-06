# Pytest

## [- Задание 19.2.3](https://github.com/Felbushe/Pytest/tree/master/19.2.3%20Calculator)
Позитивные тесты для каждого метода калькулятора.

## [- Задание 19.7](https://github.com/Felbushe/Pytest/tree/master/19.7.2%20PetFriendsApiTests) 
Тесты для проверки API + чек листы проверок запросов API
1. У нас есть готовая библиотека с реализацией основных методов, но остались ещё два нереализованных метода. Это и будет практическим заданием: посмотреть [документацию](https://petfriends.skillfactory.ru/apidocs/) к имеющимся API-методам. Найти методы, которые ещё не реализованы в библиотеке, и написать их реализацию в файле api.py.  
2. Подумайте над вариантами тест-кейсов и напишите 10 различных тестов для данного REST API-интерфейса.

---

Объект тестирования: *[сайт "PetFriends"](https://petfriends.skillfactory.ru/)*  
API сайта: *[Flasgger](https://petfriends.skillfactory.ru/apidocs/)*  

### [Чек-листы проверок запросов API](https://docs.google.com/spreadsheets/d/1xbI48-S1MN7-jIQTEQgVmu8ELHDk4jb9WtGVYOOpNu0/edit?usp=sharing)

## [- Задание 25.5.1](https://github.com/Felbushe/Pytest/tree/master/Module_25)
**Project URL**: https://petfriends.skillfactory.ru/login

`conftest.py` - файл конфигурации<br>
`valid_email` - "<email при регистрации в API>"<br>
`valid_password` - "<пароль для email>"

`/tests` содержит файл с тест-кейсом, который проверяет, что на странице со списком питомцев пользователя:
1) присутствуют все питомцы
2) хотя бы у половины питомцев есть фото
3) у всех питомцев есть имя, порода, возраст
4) у всех питомцев разные имена
5) в списке нет повторяющихся питомцев

В написанном тесте есть:
- неявные ожидания всех элементов (проверка карточек питомцев)
- явные ожидания элементов страницы (проверка таблицы питомцев)

Selenium
