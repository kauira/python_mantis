import string
import random
from model.project import Project

def random_srting(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_project(app):
    old_list = app.project.get_projects()
    project = Project(name = random_srting("name", 10), description=random_srting("description", 20))
    app.project.add_project(project)
    new_list = app.project.get_projects()
    old_list.append(project)
    assert sorted(old_list) == sorted(new_list)