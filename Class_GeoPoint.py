from math import sin, cos, atan2, radians, sqrt


class GeoPoint:
    # Constructor __init__ to initialize  __lat, __lon, and __description variables
    def __init__(self, lat=0, lon=0, description='TBD'):
        self.__lat = lat
        self.__lon = lon
        self.__description = description

    # Accessors/Mutators
    def SetPoint(self, coords):
        self.__lat = coords[0]
        self.__lon = coords[1]

    def GetPoint(self):
        return self.__lat, self.__lon

    def SetDescription(self, description):
        self.__description = description

    def GetDescription(self):
        return self.__description

    """ Distance(self,toPoint) method calculates distance
    between the objects' points  and the user's point
    """
    def Distance(self, toPoint):
        # approximate radius of earth in km
        # R = 6373.0
        # approximate radius of earth in miles
        R = 3958.8
        lat1, lon1 = radians(self.__lat), radians(self.__lon)
        lat2, lon2 = radians(toPoint[0]), radians(toPoint[1])
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        d = R * c
        return d

    Point = property(GetPoint, SetPoint)

    Description = property(GetDescription, SetDescription)
