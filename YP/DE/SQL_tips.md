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