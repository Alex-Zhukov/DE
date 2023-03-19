В данном спринте используется релиционная БД

```commandline
docker run -d --rm -p 3000:3000 -p 15432:5432 --name=de-sprint-0-server-local sindb/sprint-0-freetrack:latest
```
- Модель данных - структура таблиц со связями.
- Сущность - таблица в БД.

**Материализованное представление**

Материализованное представление сохраняет результат запроса в отдельную постоянную таблицу и при повторном обращении не выполняет запрос заново, а берёт уже подготовленные данные из этой таблицы. Такое представление можно обновить: запрос выполнится заново, и при следующем обращении вернутся уже обновлённые данные.

```SQL
CREATE MATERIALIZED VIEW

REFRESH MATERIALIZED VIEW my_other_view;

DROP MATERIALIZED VIEW IF EXISTS my_other_view; 

CREATE OR REPLACE VIEW my_view AS ...; 
```



```
Для запуска проверки:
psql postgresql://jovyan:jovyan@localhost:5432/de -f realization.sql

cloudbeaver
http://127.0.0.1:3000/cloudbeaver/#/

```
Для хранения инфо об источниках, лучше создать справочник.
Нейминг - код системы источника + слой данных + название сущности

Например 001_BUFF_Client, 002_DM_Clients 