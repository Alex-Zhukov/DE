drop table if exists stage.customer_research;
drop table if exists stage.user_order_log;
drop table if exists stage.user_activity_log;

create table stage.customer_research (
    id serial primary key,
	date_id timestamp,
	category_id int,
	geo_id int,
	sales_qty int,
	sales_amt numeric(14,2)
);

create table stage.user_order_log (
	id int,
	date_time timestamp,
	city_id int,
	city_name varchar(100),
	customer_id bigint,
	first_name varchar(100),
	last_name varchar(100),
	item_id int,
	item_name varchar(100),
	quantity bigint,
	payment_amount numeric(14,2)
);

create table stage.user_activity_log (
	id serial primary key,
	date_time timestamp,
	action_id bigint,
	customer_id bigint,
	quantity bigint
);


drop table if exists prod.customer_research;
drop table if exists prod.user_order_log;
drop table if exists prod.user_activity_log;

create table prod.customer_research
as 
select scr.date_id, scr.geo_id, scr.sales_qty, scr.sales_amt
from stage.customer_research scr; 

create table prod.user_order_log
as 
select scr.date_time, scr.customer_id, scr.quantity, scr.payment_amount
from stage.user_order_log scr; 

create table prod.user_activity_log
as 
select scr.date_time, scr.customer_id
from stage.user_activity_log scr; 


