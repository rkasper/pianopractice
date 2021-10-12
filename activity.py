class Activity:
    group : str
    name : str
    url : str

    def __init__(self, group, exercise, url):
        self.group = group
        self.name = exercise
        self.url = url

    def __repr__(self):
        return self.group + ': ' + self.name