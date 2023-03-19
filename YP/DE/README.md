
Для монтирования docker 
```commandline

Вариант с монтированием папки:
docker run -d -v /home/username/de_lessons:/lessons --rm -p 3000:3000 -p 15432:5432 --name=de-sprint-1-server-local sindb/sprint-1:latest

Без metabase:
docker run -d -e OFF_MB=1 --rm -p 3000:3000 -p 15432:5432 --name=de-sprint-0-server-local sindb/sprint-0-freetrack:latest

Вариант с монтированием вольюма (предпочтительный вариант):
docker run -d -v sprint0:/lessons --rm -p 3000:3000 -p 15432:5432 --name=de-sprint-1-server-local sindb/sprint-1:latest
```


```BASH
Стоп:
docker stop <container> 

Удаление:
 docker rm <container-name> 
 docker rmi <image-name> (Удаление образа)
 
Перезапуск:
docker start [параметры] <container-name> 

Сброс прогресса:
/flush_lessons.sh
```