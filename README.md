# Проект автотестов на [hh.ru](https://hh.ru/)

<img align="center" src="https://github.com/ioomoon/QA-guru-graduation/blob/master/img/hh.jpg?raw=true" width="300">

---

## <img src="https://github.com/ioomoon/QA-guru-graduation/blob/master/img/icon5.png?raw=true" width="20"> Реализованы проверки:
Ui:
- Проверка наличия корректного промо-текста на главной странице
- Проверка наличия результатов поиска по названию вакансии с параметрами
- Проверка результата поиска по некорректному названию вакансии с параметрами
- Проверка результата расширенного поиска по наличию ключевых слов в названии компании
- Проверка перехода на страницу для работодателей при нажатии кнопки в панели навигации
- Проверка перехода на страницу для соискателей при нажатии кнопки в панели навигации

## <img src="https://github.com/ioomoon/QA-guru-graduation/blob/master/img/icon4.png?raw=true" width="20"> Запуск проекта:
- Для запуска проектов локально:
```bash
pytest -s -v tests --alluredir=[path_to_report_dir]
```
- Для генерации Allure-репорта:
```bash
allure serve [path_to_report_dir]
```

## <img src="https://github.com/ioomoon/QA-guru-graduation/blob/master/img/icon6.png?raw=true" width="20"> Отчеты в Allure Report
- Графики
![](img/allureres1.png "status and severity")
- Тестовые наборы
![](img/allureres2.png "suites")
- Шаги воспроизведения
![](img/allureres3.png "suites")
- История запуска теста
![](img/allureres4.png "history")