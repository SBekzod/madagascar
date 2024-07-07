-- update_plan.sql
UPDATE plan
SET content = '{{ content }}'
WHERE id = {{ id }};
