create schema if not exists stage;

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