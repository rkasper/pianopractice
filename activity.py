class Activity:
    group : str
    exercise : str

    def __init__(self, group, exercise):
        self.group = group
        self.exercise = exercise

    def __repr__(self):
        return self.group + ': ' + self.exercise