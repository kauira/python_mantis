class Project:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return "%s %s" % (self.name, self.description)

    def __eq__(self, other):
        if not isinstance(other, Project):
            return NotImplemented
        return self.name == other.name and self.description == other.description

    def __gt__(self, other):
        if not isinstance(other, Project):
            return NotImplemented
        if self.name != other.name:
            return self.name > other.name
        return self.description > other.description