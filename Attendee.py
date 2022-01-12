# Object for Attendees
class Attendee:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_attendee_x (self):
        return self.x

    def get_attendee_y(self):
        return self.y

    def set_attendee_y(self, y):
        self.y = y

    def set_attendee_x(self, x):
        self.x = x
