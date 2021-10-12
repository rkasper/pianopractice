class Activity:
    group : str
    exercise : str
    url : str

    def __init__(self, group, exercise, url):
        self.group = group
        self.exercise = exercise
        self.url = url

    def __repr__(self):
        return self.group + ': ' + self.exercise