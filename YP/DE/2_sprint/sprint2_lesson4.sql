select 
constraint_schema,
constraint_name,
update_rule,
delete_rule 
from information_schema.referential_constraints;