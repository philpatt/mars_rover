class MarsLandingArea(object):
    # This class creates the landing area plateau for the rover

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.taken = []