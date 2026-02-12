from task_manager import add_task


def test_add_task():
    # add a task

    task = add_task("Test task")
    assert task["description"] == "Test task"
    assert task["completed"] is False