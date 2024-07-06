-- update_goal.sql
UPDATE goal
SET goalContent = '{{ goalContent }}'
WHERE goalId = {{ goalId }};
