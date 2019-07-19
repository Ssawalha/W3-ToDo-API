
echo 'get_all_items (127.0.0.1:5000/todo/api/tasks)'
curl 127.0.0.1:5000/todo/api/tasks

echo 'get_item (127.0.0.1:5000/todo/api/tasks/1)'
curl 127.0.0.1:5000/todo/api/tasks/1

echo 'create_task (127.0.0.1:5000/todo/api/tasks)'
curl -X POST -H  'content-type: application/json' -d '{"title":"new_todo","description":"does this work?", "status":false}' 127.0.0.1:5000/todo/api/tasks

echo 'update_task (127.0.0.1:5000/todo/api/tasks/2)'
curl -X PUT -H  'content-type: application/json' -d '{"status":true}' 127.0.0.1:5000/todo/api/tasks/2

echo 'delete_task (127.0.0.1:5000/todo/api/tasks/6)'
curl -X DELETE 127.0.0.1:5000/todo/api/tasks/6