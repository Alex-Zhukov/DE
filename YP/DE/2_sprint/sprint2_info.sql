SELECT * FROM user_activity_log ual  LIMIT 0;

-- Какие базы есть в таблице
SELECT table_schema, table_name FROM information_schema.tables;

-- Свойства нескольких таблиц
select table_name, column_name, data_type, character_maximum_length, column_default, is_nullable  
 from information_schema.columns  
  where table_schema = 'public' and  
   table_name in ('my_table', 'second_table', 'third_table', 'other_table') 
    order by table_name;
    
-- Создание индекса
CREATE INDEX second_id_index ON f_main_table (second_id);

-- Изменение типа колонки
ALTER TABLE public.d_products ALTER COLUMN price TYPE numeric(14,2);

