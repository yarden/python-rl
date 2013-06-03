import numpy

class TrivialBasis(object):
    """Uses the features themselves as a basis. However, does a little bit of basic manipulation
    to make things more reasonable. Specifically, this allows (defaults to) rescaling to be in the
    range [-1, +1].
    """

    def __init__(self, nvars, ranges):
        self.numTerms = nvars
        self.ranges = numpy.array(ranges)

    def scale(self, value, pos):
        if self.ranges[pos,0] == self.ranges[pos,1]:
            return 0.0
        else:
            return (value - self.ranges[pos,0]) / (self.ranges[pos,1] - self.ranges[pos,0])

    def computeFeatures(self, features):
        return (numpy.array([self.scale(features[i],i) for i in range(len(features))]) - 0.5)*2.


