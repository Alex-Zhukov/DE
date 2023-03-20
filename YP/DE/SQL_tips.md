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
