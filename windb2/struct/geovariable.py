class GeoVariable(object):
    """Abstract class"""

    """Datatime of the observation time."""
    time = None

    """Height above ground level [m]"""
    height = None

    """Value of variable"""
    val = None

    """Units of speed."""
    units = None

    """Creates a new FlowData object"""

    def __init__(self, name, time, height, val, units="unset"):
        self.name = name
        self.time = time
        try:
            self.height = float(height)
        except ValueError:
            self.height = None
        if val is not None:
            self.val = float(val)
        else:
            self.val = None
        try:
            self.units = units
        except ValueError:
            self.units = 'unset'

    """Returns the value as a float"""

    def getVal(self):
        return self.val

    """Prints the flow data in a pretty fashion."""
    def __str__(self):
        return 'time={} height={} val={} units={}'.format(self.time, self.height, self.val, self.units)
