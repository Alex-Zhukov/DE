INSERT INTO public.d_vendors (id, attribute_one, attribute_two, attribute_three)
SELECT attribute_seven[1],
       attribute_one,
       attribute_seven[2],
       attribute_three
FROM
  (SELECT attribute_one,
          regexp_split_to_array(attribute_seven, ':+') AS attribute_seven,
          attribute_three
   FROM attributes_table_old) AS d_main_attributes_information;
   
  
-- последовательности
  
CREATE SEQUENCE d_first_properties_sequence
START 1;

SELECT nextval('d_first_properties_sequence');

-- result
-- Name   |Value|
-- -------+-----+
-- nextval|1    |
 -- или

SELECT nextval('d_first_properties_sequence')::bigint AS id,
       attributes_five,
       attributes_three::TIMESTAMP
FROM
  (SELECT DISTINCT attribute_five,
                   attribute_three
   FROM attributes_table_old) AS d_first_properties_information;

DROP SEQUENCE d_first_properties_sequence;