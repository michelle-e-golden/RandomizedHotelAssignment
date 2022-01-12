# Object for hotels
class Hotel:
    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.attendees = []

    def get_hotel_name(self):
        return self.name

    def get_hotel_x(self):
        return self.x

    def get_hotel_y(self):
        return self.y

    def set_hotel_name(self, name):
        self.name = name

    def set_hotel_y(self, y):
        self.y = y

    def set_hotel_x(self, x):
        self.x = x

    def add_attendee(self, attend):
        self.attendees.append(attend)
