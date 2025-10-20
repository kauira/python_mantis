import random

from model.project import Project


def test_delete_project(app):
    projects = app.project.get_projects()
    if len(projects) == 0:
        app.project.add_project(Project(name="test", description="test"))
    projects = app.project.get_projects()
    project = random.choice(projects)
    app.project.delete_project(project)
    projects = app.project.get_projects()
    soap = app.soap.get_projects()
    assert sorted(soap) == sorted(projects)