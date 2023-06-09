from datetime import datetime

class Position(object):

    def __init__(self, latitude: float, longitude: float, time: datetime = None, name = "") -> None:
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        if not time:
            self.time = datetime.now()
        else:
            self.time = time


    def euclid(self, position: '__class__') -> float:
        return pow(pow(self.latitude - position.latitude, 2) + pow(self.longitude - position.longitude, 2), 0.5)

    def __str__(self):
        return f"Position is {self.latitude} latitude and {self.longitude} longitude." + \
               f" Created at {self.time}, name of the point is {self.name}" 