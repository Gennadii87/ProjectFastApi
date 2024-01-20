Перед запуском проекта необходимо установить базу данных PostgresSQL (В проекте использована 14 версия)
Создаем вертуальное окружение в IDE (например PyCharm)
Клонируем репозиторий командой: git clone https://github.com/Gennadii87/ProjectFastApi.git
Перед установкой пакетов обновите менеджер пакетов: python.exe -m pip install --upgrade pip  (при необходимости)
Установите все зависимости из файла requirements.txt  командой: pip install -r requirements.txt

НЕ ЗАБУДТЕ СОЗДАТЬ ПОЛЬЗОВАТЕЛЯ В БАЗЕ ДАННЫХ PostgresSQL и задать пароль
Далее в файле database.py установите свои параметры подключения к вашей БД (DATABASE_URL = "postgresql://postgres:superuser@localhost:5432/my_database" по умолчанию имя пользователя в PostgresSQL -  postgres, а superuser это ваш пароль когда вы устанвливали базу данных, рекомендуется для удобства использовать pgAdmin)

ЗАПУСТИТЕ ПРОЕКТ КОМАНДОЙ: uvicorn main:app --reload 
При первом запуске автоматически создатся база данных (если правильно уазали параметры DATABASE_URL = "postgresql://postgres:superuser@localhost:5432/my_database" )

EN

"Before launching the project, it is necessary to install the PostgresSQL database (version 14 is used in the project). Create a virtual environment in your IDE (for example, PyCharm). Clone the repository using the command: git clone https://github.com/Gennadii87/ProjectFastApi.git. Before installing the packages, update the package manager: python.exe -m pip install --upgrade pip (if necessary). Install all dependencies from the requirements.txt file using the command: pip install -r requirements.txt.

DON'T FORGET TO CREATE A USER IN THE PostgresSQL DATABASE AND SET A PASSWORD. Then, in the database.py file, set your connection parameters to your database (DATABASE_URL = "postgresql://postgres:superuser@localhost:5432/my_database" - by default, the PostgresSQL username is postgres, and superuser is your password when you installed the database; it is recommended to use pgAdmin for convenience).

RUN THE PROJECT WITH THE COMMAND: uvicorn main:app --reload. During the first launch, the database will be automatically created (if you correctly specified the parameters DATABASE_URL = "postgresql://postgres:superuser@localhost:5432/my_database")."