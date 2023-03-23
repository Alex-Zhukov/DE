SELECT *
FROM pg_catalog.pg_tables
WHERE schemaname = 'public'
    AND tablename = 'user_payment_log';
    
select 
column_name ,
data_type
from information_schema.columns
where table_name = 'user_payment_log';

SELECT 
coalesce(payment_amount, 0) AS payment_amount 
FROM user_payment_log; 

select 
client_id,
phone
from (select 
		client_id,
		phone,
		row_number() over (partition by client_id order by updated_at desc) as rnk
	  from user_contacts) t
where rnk = 1
;

select distinct on (client_id)
	client_id,
	phone
from user_contacts;

SELECT /* дополните запрос */ AS phone
FROM user_contacts;

select regexp_replace(phone, '[^0-9]','', 'g') 
from user_contacts uc ;

select regexp_replace(phone, '[^0-9]','', 'g') 
from user_contacts uc ;

SELECT substring(regexp_replace(phone, '[^0-9]','', 'g') from 2 for 3) AS reg_code
FROM user_contacts; 

select
to_timestamp(updated_at, 'HH24:MI:SS DD/MM/YYYY') AS updated_month
FROM user_contacts; 


SELECT updated_at AS updated_month
FROM user_contacts; 

alter table user_contacts 
add constraint user_contacts_client_id_fkey foreign key (client_id) references user_attributes (client_id);