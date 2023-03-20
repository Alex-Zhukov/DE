**Таблица pg_stat_activity**

- pid Идентификатор серверного процесса
- state Состояние (active-выполнение, idle-ожидание команды от клиента, idle in transaction-внутри транзакции, но не выполняет запрос)
- query_stat время начала выполнения активного/последнего запроса
- query Текст запроса
- waiting Флаг блокировки

```SQL
SELECT 
  now() - query_start AS duration,
  pid,
  username,
  state,
  query
FROM pg_stat_activity
WHERE state !='idle' ORDER BY 1 DESC;
```

Для OLTP - длительные операции 3-5 минут
Для OLAP - несколько часов


**План запроса**
Удобный инструмент для визуализации и анализа плана запроса <a>explain-tesor.ru</a> / <a>planchecker.arenadata.io</a>
EXPLAIN(не выполняется) / EXPLAIN ANALIZE(выполняется)

В случае Explain analize есть риск изменения данных (если есть Update/insert/delete). В такое случае лучше использовать ROLLBACK

