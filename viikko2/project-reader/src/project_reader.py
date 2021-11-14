from urllib import request
from project import Project
import tomli

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        # print(content)

        with open("pyproject.toml", encoding="utf-8") as f:
            toml_dict = tomli.load(f)

        print(toml_dict['tool']['poetry'])


     

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(toml_dict['tool']['poetry']['name'], toml_dict['tool']['poetry']['description'], toml_dict['tool']['poetry']['dependencies'], toml_dict['tool']['poetry']['dev-dependencies'])