select t.main_column, s.identification_name, u.email
from tasks t
inner join sheets s on t.sheet_id = s.sheet_id
inner join users_tasks ut on t.task_id = ut.task_id 
inner join users u on ut.user_id = u.user_id 
where t.task_status = true;

insert into users (email, name, user_type)
values ('ana@email.com', 'ana', 'admin');

insert into users (email, name, user_type)
values ('joao@email.com', 'joao', 'admin');

insert into sheets (identification_name)
values ('plan1');

insert into sheets (identification_name)
values ('plan2');

insert into users (task_status, sheet_id, task_type, main_column)
values (True, 697, 'integer', 'column1');

insert into users_tasks (user_id, task_id)
values (675, 1710);

insert into users_tasks (user_id, task_id)
values (676, 1710)

insert into tasksweekdays (sunday, monday, tuesday, wednesday, thursday, friday, saturday, task_id)
values (True, True, True, True, True, True, True, 1710);

insert into tasksweekdays (sunday, monday, tuesday, wednesday, thursday, friday, saturday, task_id)
values (False, False, False, False, False, False, False, 1710);

insert into tasks_runtime (runtime, task_id)
values ('10:00:00', 1710)

select t.main_column, s.identification_name, u.email, t.auxiliary_column, t.reference_values 
from tasks t
inner join sheets s on t.sheet_id = s.sheet_id
inner join users_tasks ut on t.task_id = ut.task_id 
inner join users u on ut.user_id = u.user_id 
inner join tasksweekdays t2 on t.task_id = t2.task_id 
where t.task_status = true and t2.sunday = true;