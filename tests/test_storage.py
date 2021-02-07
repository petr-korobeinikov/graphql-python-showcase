from app.storage import project_by_slug, tasks_by_project_id


def test_project_by_slug():
    assert 'Project 1' == project_by_slug('proj1').first().name


def test_tasks_by_project_id():
    assert all(1 == t.project_id for t in tasks_by_project_id(1))
