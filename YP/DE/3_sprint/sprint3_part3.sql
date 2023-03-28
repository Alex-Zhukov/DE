select distinct 
city_id,
city_name
from stage.user_order_log;

truncate mart.d_calendar;

select 
*
from mart.d_calendar;

CREATE SEQUENCE city_id_sequence
START 1;


create table stage.d_city as 
select 
nextval('city_id_sequence')::int AS id,
city_id,
city_name FROM
	(select distinct 
	city_id,
	city_name
	from stage.user_order_log) t;

DROP SEQUENCE city_id_sequence;

CREATE SEQUENCE calendar_id_sequence
START 1;

create table stage.d_calendar as 
select 
	   nextval('calendar_id_sequence')::int AS date_id,
	   date::date,
       extract('day' from t) as day_num,
       extract('month' from t) as month_num,
       to_char(t, 'MON')  as month_name,
       date_part('year', t)  as year_num
  from generate_series(date '01-01-2020',
                       date '01-01-2022',
                       interval '1 day')
       as t(date);
      
DROP SEQUENCE calendar_id_sequence;