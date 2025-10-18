from zeep import Client
from zeep.exceptions import Fault
from model.project import Project

class SoapHelper:

    def __init__(self, app):
        self.app = app

    def get_projects(self, username, password):
        client = Client("http://localhost/mantisbt-1.2.20/mantisbt-1.2.20/api/soap/mantisconnect.php?wsdl")
        try:
            dict_project = client.service.mc_projects_get_user_accessible(username, password)
            projects = []
            for i in dict_project:
                desired_keys = ["name", "description"]
                filtered_dict = {key: i[key] for key in desired_keys if key in i}
                projects.append(Project(name=filtered_dict["name"], description=filtered_dict["description"]))
            return projects
        except Fault:
            return False
