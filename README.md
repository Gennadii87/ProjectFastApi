Перед запуском проекта необходимо установить базу данных PostgresSQL (В проекте использована 14 версия)
Создаем вертуальное окружение в IDE (напримерв PyCharm)
Клонируем репозиторий командой: git clone https://github.com/Gennadii87/ProjectFastApi.git
Перед установкой пакетов обновите менеджер пакетов: python.exe -m pip install --upgrade pip  (при необходимости)
Установите все зависимости из файла requirements.txt  командой: pip install -r requirements.txt

НЕ ЗАБУДТЕ СОЗДАТЬ ПОЛЬЗОВАТЕЛЯ В БАЗЕ ДАННЫХ PostgresSQL и задать пароль
Далее в файле database.py установите свои параметрв подключения к вашей БД (DATABASE_URL = "postgresql://postgres:superuser@localhost:5432/my_database" по умолчанию имя пользователя в PostgresSQL -  postgres, а superuser это ваш пароль когда вы устанвливали базу данных, рекомендуется для удобства использовать pgAdmin)

ЗАПУСТИТЕ ПРОЕКТ КОМАНДОЙ: uvicorn main:app --reload 
При первом запуске автоматически создатся база данных (если правильно уазали параметры DATABASE_URL = "postgresql://postgres:superuser@localhost:5432/my_database" )
