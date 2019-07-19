
from model.todoitem import TodoItem
from schema import DEFAULT_DB_PATH


def seed(dbpath):
    TodoItem.dbpath = dbpath
    go_to_class = TodoItem(title="Go to class",
                           description="Gotta get it done...",
                           status=1)
    do_homework = TodoItem(title="Do Homework",
                           description="There's so much!",
                           status=0)
    fix_dinner = TodoItem(title="Fix Dinner",
                          description="Don't eat take out again, come on",
                          status=0)
    go_to_class.save()
    do_homework.save()
    fix_dinner.save()


if __name__ == "__main__":
    seed(DEFAULT_DB_PATH)
