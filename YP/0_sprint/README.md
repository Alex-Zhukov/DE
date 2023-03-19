В данном спринте используется релиционная БД

```commandline
docker run -d --rm -p 3000:3000 -p 15432:5432 --name=de-sprint-0-server-local sindb/sprint-0-freetrack:latest
```
- Модель данных - структура таблиц со связями.
- Сущность - таблица в БД.
- 