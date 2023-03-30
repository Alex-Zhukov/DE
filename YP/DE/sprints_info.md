```commandline
docker run --rm -d -v sprint1:/lessons -p 7010:8000 --name de-sprint-1-server-local cr.yandex/crp1r8pht0n0gl25aug1/de-sprint-1-v2:latest


```

Копирование файла:
```bash
docker ps 

# команда копирования файла с локального компьютера в контейнер в нужную папку
docker cp /path/to/our_file/titanic_dag.py [CONTAINER ID]:/lessons/dags/titanic_dag.py


```