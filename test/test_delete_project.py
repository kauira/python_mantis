import random

from model.project import Project


def test_delete_project(app):
    projects = app.project.get_projects()
    if len(projects) == 0:
        app.project.add_project(Project(name="test", description="test"))
    old_projects = app.project.get_projects()
    project = random.choice(old_projects)
    app.project.delete_project(project)
    new_projects = app.project.get_projects()
    old_projects.remove(project)
    assert sorted(old_projects) == sorted(new_projects)