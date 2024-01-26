Перед запуском проекта необходимо установить базу данных PostgresSQL (В проекте использована 14 версия)
**Используя команду:** `createdb -U postgres  my_database` что бы создать базу данных с именем `my_database` (оно указано в настройках по подключению) 

**ВАЖНО!** надо ввести пароль который вы указали при установке PostgresSQL, он так же будет использоваться для подключения к базе.

**Клонируем репозиторий командой:** `git clone https://github.com/Gennadii87/ProjectFastApi.git`
Создаем вертуальное окружение в IDE (например PyCharm) прямо в папке ProjectFastApi

Перед установкой пакетов обновите менеджер пакетов: `python.exe -m pip install --upgrade pip`  (при необходимости)

Установите все зависимости из файла **requirements.txt**  командой: `pip install -r requirements.txt`

**НЕ ЗАБУДТЕ СОЗДАТЬ ПОЛЬЗОВАТЕЛЯ В БАЗЕ ДАННЫХ PostgresSQL и задать пароль.**

Далее в файле `.env` установите свои параметры подключения к вашей БД (`POSTGRES_USER=postgres POSTGRES_PASSWORD=superuser
POSTGRES_DB=my_database` по умолчанию имя пользователя в PostgresSQL -  postgres, а **superuser** это ваш пароль когда вы устанвливали базу данных, рекомендуется для удобства использовать pgAdmin)

*Примечание: в моделях базы используеться поле id с типом uudi*, необходимо выполнить команду в PostgressSQL - `CREATE EXTENSION IF NOT EXISTS "uuid-ossp";`

**ЗАПУСТИТЕ ПРОЕКТ КОМАНДОЙ:** `uvicorn main:app --reload `
При первом запуске автоматически создадутся таблицы (если правильно уазали параметры `DATABASE_URL` )
