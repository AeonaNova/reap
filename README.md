Инструмент для скрапинга веб-ресурса https://quotes.toscrape.com/, создан в среде разработки для python PyCharm. 
Были созданы модули, в которых определена логика получения данных с удаленного сервера. 
Добавлено виртуальное окружение для изолирования зависимостей. 
Посредством библиотеки requests направлен GET запрос, в результате получен html-ответ.
Данные в html были обработаны библиотекой BeautifulSoup, которая позволила извлечь искомые параметры. Структура веб-сайта получена с помощью инструментов разработчика в браузере.
Поступившие данные помещаются в dict, который передается модулю saver, сохраняющему информацию в формат json
Выбран requests вместо Selenium, потому что не задействуются дополнительные ресурсы, такие как запуск chrome драйвера. BeautifulSoup группирует найденные элементы, упрощая обход. 
Зависимости инструмента были выведены в requirements.txt c помощью pip freeze > requirements.txt 
Было выбрано функциональное оформление, потому что удобнее взаимодействие между модулями, трекинг параметров и возвращаемых значений, в отличие от написания в глобальной области видимости.