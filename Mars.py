class MarsLandingArea(object):
    # This class creates the landing area plateau for the rover
    # Any Landing Area's dimemsion will be determined by (self.x, self.y)
    # The landing Area will also have a list called ~self.taken~ that keeps track of all successful landed rovers.
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.taken = []