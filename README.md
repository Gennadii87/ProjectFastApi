Перед запуском проекта необходимо установить базу данных PostgresSQL (В проекте использована 14 версия)
Используя команду: createdb -U postgres  mydatabase что бы создать базу данных с именем my_database (оно указано в настройках по подключению) 
ВАЖНО! надо ввести пароль который вы указали при установке PostgresSQL, он так же будет использоваться для подключения к базе.
Клонируем репозиторий командой: git clone https://github.com/Gennadii87/ProjectFastApi.git
Создаем вертуальное окружение в IDE (например PyCharm) прямо в папке ProjectFastApi
Перед установкой пакетов обновите менеджер пакетов: python.exe -m pip install --upgrade pip  (при необходимости)
Установите все зависимости из файла requirements.txt  командой: pip install -r requirements.txt

НЕ ЗАБУДТЕ СОЗДАТЬ ПОЛЬЗОВАТЕЛЯ В БАЗЕ ДАННЫХ PostgresSQL и задать пароль
Далее в файле database.py установите свои параметры подключения к вашей БД (DATABASE_URL = "postgresql://postgres:superuser@localhost:5432/my_database" по умолчанию имя пользователя в PostgresSQL -  postgres, а superuser это ваш пароль когда вы устанвливали базу данных, рекомендуется для удобства использовать pgAdmin)
Примечание: в моделях базы используеться поле id с типом uudi, необходимо выполнить команду в PostgressSQL - CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

ЗАПУСТИТЕ ПРОЕКТ КОМАНДОЙ: uvicorn main:app --reload 
При первом запуске автоматически создатся база данных (если правильно уазали параметры DATABASE_URL = "postgresql://postgres:superuser@localhost:5432/my_database" )

EN

Before launching the project, it is necessary to install the PostgresSQL database (Version 14 is used in the project).
Use the command: createdb -U postgres mydatabase to create a database with the name my_database (as specified in the connection settings). IMPORTANT! Enter the password you provided during the installation of PostgresSQL; it will also be used for connecting to the database.
Clone the repository with the command: git clone https://github.com/Gennadii87/ProjectFastApi.git
Create a virtual environment in your IDE (e.g., PyCharm) directly in the ProjectFastApi folder.
Before installing the packages, update the package manager: python.exe -m pip install --upgrade pip (if necessary).
Install all dependencies from the requirements.txt file with the command: pip install -r requirements.txt

DON'T FORGET TO CREATE A USER IN THE PostgresSQL DATABASE AND SET A PASSWORD.
Next, in the database.py file, set your connection parameters to your database (DATABASE_URL = "postgresql://postgres:superuser@localhost:5432/my_database"). By default, the username in PostgresSQL is postgres, and superuser is your password when you installed the database. It is recommended for convenience to use pgAdmin.
Note: The database models use the id field with the UUID type. Execute the following command in PostgresSQL: CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

RUN THE PROJECT WITH THE COMMAND: uvicorn main:app --reload

During the first run, the database will be automatically created (if you correctly specified the parameters DATABASE_URL = "postgresql://postgres:superuser@localhost:5432/my_database").