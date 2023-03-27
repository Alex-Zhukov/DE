Обновление из другой таблицы
```SQL
UPDATE название таблицы
SET поле = значение
FROM  название таблицы, из которой нужно взять значение
WHERE условие объединения таблиц
```
Загрузка из csv
```SQL
COPY "002_BUFF_client"(client_id, client_firstname, client_lastname, client_email, client_phone, client_city)
FROM './clients.csv'
DELIMITER ','
CSV HEADER;
```

```SQL
Проверка таблицы
SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname = 'public'
    AND tablename = 'your_table_name';
    
```

Нейминг таблиц:

Для хранения инфо об источниках, лучше создать справочник. Нейминг - код системы источника + слой данных + название сущности

Например 001_BUFF_Client, 002_DM_Clients

Нейминг ограничений:

{tablename}_{columnname(s)}_{suffix}

- tablename — название таблицы,
- columnname(s) — одна или несколько колонок в ограничении,
- suffix — тип ограничения:
    - pkey для первичного ключа,
    - fkey для внешнего ключа,
    - check для ограничения-проверки,
    - idx для любого другого типа индекса.

Информацию по индексам в таблице метаданных pg_indexes в схеме pg_catalog

Backup pg_dump

```sql
pg_dump -U имя_пользователя название_базы_данных
pg_dump --username имя_пользователя --host 192.168.0.1 --dbname название_базы_данных
pg_dump --username имя_пользователя --host 127.0.0.1 --dbname название_базы_данных --file example_dump.sql
```
-table сохранит только дамп отдельной таблицы
—schema-only только модель
--data-only только данные

Для дампа табличных пространств/ролей пользователей и тд использовать pg_dumpall

Пример названия бэкапа:
- pg_prod_clients_2222_01_01_task_777_backup.sql
- pg — название СУБД PostgreSQL;
- prod — название продуктивной среды;
- clients — название БД;
- 2222_01_01 — дата создания бэкапа;
- task_777 — шифр задачи.

**psql** 
подключение:
```sql
psql --username имя_пользователя --dbname название_базы_данных --file example_dump.sql

pg_restore --dbname название_базы_данных --file example_dump.sql
pg_restore --table название_таблицы --file example_dump.sql
pg_restore --data-only --file example_dump.sql
pg_restore --schema-only --file example_dump.sql
```























