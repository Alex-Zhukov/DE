select 
constraint_schema,
constraint_name,
update_rule,
delete_rule 
from information_schema.referential_constraints;

drop table if exists d_products;
drop table if exists d_categories;
drop table if exists d_vendors;

create table d_products (
	product_id serial primary key,
	category_id BIGINT,
	vendor_id BIGINT,
	name_product text,
	description text,
	stock bool
);

create table d_categories(
	category_id BIGINT primary key,
	name_category text,
	description text
);

create table d_vendors(
	id SERIAL,
	vendor_id bigint primary key,
	name_vendor text,
	description text
);

alter table d_products 
	add constraint fk_products_vendors foreign key (vendor_id) references d_vendors(vendor_id);

alter table d_products 
	add constraint fk_products_categories foreign key (category_id) references d_categories(category_id);
	