import string
import random
from model.project import Project

def random_srting(prefix, maxlen):
    symbols = string.ascii_letters + string.digits
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def test_add_project(app, ):
    project = Project(name = random_srting("name", 10), description=random_srting("description", 20))
    app.project.add_project(project)
    projects = app.project.get_projects()
    soap = app.soap.get_projects("administrator","root")
    assert sorted(soap) == sorted(projects)