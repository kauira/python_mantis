from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def add_project(self, project):
        wd = self.app.wd
        self.open_manage_proj_create_page()
        self.fill_project_form(project)
        self.submit_add()

    def submit_add(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Add Project']").click()

    def open_manage_proj_create_page(self):
        wd = self.app.wd
        base_url = self.app.base_url
        text = wd.find_element_by_css_selector("td.form-title").text
        if not(wd.current_url.endswith("/manage_proj_create_page.php") and text == 'Add Project'):
            wd.get(f"{base_url}manage_proj_create_page.php")

    def fill_project_form(self, project):
        wd = self.app.wd
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(project.name)
        wd.find_element_by_name("description").click()
        wd.find_element_by_name("description").clear()
        wd.find_element_by_name("description").send_keys(project.description)

    def get_projects(self):
        wd = self.app.wd
        self.open_manage_project_page()
        list = []
        for element in wd.find_elements_by_css_selector("table.width100[cellspacing='1'] tbody tr.row-1"):
            cells = element.find_elements_by_tag_name("td")
            name = cells[0].text
            description = cells[4].text
            list.append(Project(name=name, description=description))
        for element in wd.find_elements_by_css_selector("table.width100[cellspacing='1'] tbody tr.row-2"):
            cells = element.find_elements_by_tag_name("td")
            name = cells[0].text
            description = cells[4].text
            list.append(Project(name=name, description=description))
        return list

    def open_manage_project_page(self):
        wd = self.app.wd
        base_url = self.app.base_url
        if not(wd.current_url.endswith("/manage_proj_page.php") and
               len(wd.find_elements_by_css_selector("input[type='submit'][value='Create New Project']")) > 0):
            wd.get(f"{base_url}manage_proj_page.php")

    def delete_project(self, project):
        wd = self.app.wd
        self.open_manage_project_page()
        wd.find_element_by_link_text(project.name).click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        wd.find_element_by_css_selector("input[value='Delete Project']").click()

    def count(self):
        wd = self.app.wd
        self.open_manage_project_page()
        print(len(wd.find_elements_by_css_selector("tr.row-1")))
        return len(wd.find_elements_by_css_selector("tr.row-1"))


