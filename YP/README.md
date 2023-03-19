
Для монтирования docker 
```commandline

Вариант с монтированием папки:
docker run -d -v /home/username/de_lessons:/lessons --rm -p 3000:3000 -p 15432:5432 --name=de-sprint-1-server-local sindb/sprint-1:latest

Вариант с монтированием вольюма (предпочтительный вариант):
docker run -d -v sprint0:/lessons --rm -p 3000:3000 -p 15432:5432 --name=de-sprint-1-server-local sindb/sprint-1:latest
```