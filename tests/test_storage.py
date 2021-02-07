from app.storage import person_by_id, project_by_slug, task_by_id, tasks_by_project_id


def test_project_by_slug():
    assert 'Project 1' == project_by_slug('proj1').first().name


def test_tasks_by_project_id():
    assert all(1 == t.project_id for t in tasks_by_project_id(1))


def test_task_by_id():
    assert 1 == task_by_id(1).first().id


def test_person_by_id():
    assert 'Person 1' == person_by_id(1).first().name
