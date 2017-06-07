from math import sqrt

class PointND:
    def __init__(self,*args):
        l = []
        self.n = len(args);
        for num in args:
            if type(num) is not float:
                raise ValueError("Cannot instantiate an object with non-float values.")
            l.append(num)
        self.t = tuple(l)

    def __str__(self):
        result = "("
        for num in self.t:
            result += "{:.2f}, ".format(num)
        result = result[:-2] + ")"
        return result

    def __hash__(self):
        return hash(self.t)

    def distanceFrom(self,other):
        if(self.n != other.n):
            raise ValueError("Cannot calculate distance between points of different cardinality.")
        sq_sum = 0
        for num1,num2 in zip(self.t,other.t):
            sq_sum += (num1-num2)**2
        return sqrt(sq_sum)

    def nearestPoint(self, points):
        if len(points) == 0:
            raise ValueError("Input cannot be empty.")
        min_point = points.pop()
        min_dist = self.distanceFrom(min_point)
        for point in points:
            temp_dist = self.distanceFrom(point)
            if (temp_dist < min_dist):
                min_dist = temp_dist
                min_point = point
        return min_point

    def clone(self):
        return PointND(*self.t)


    def __add__(self, other):
        if(type(other) is float):
            new_l = [x + other for x in self.t]
            new_pt = PointND(*new_l)
        else:
            if(self.n != other.n):
                raise ValueError("Cannot operate on points with different cardinalities.")
            new_l = []
            for num1,num2 in zip(self.t,other.t):
                new_l.append(num1+num2)
            new_pt = PointND(*new_l)
        return new_pt

    def __radd__(self, other):
        if(type(other) is float):
            new_l = [x + other for x in self.t]
            new_pt = PointND(*new_l)
            return new_pt
        else:
            raise ValueError("Cannot operate non-float values.")

    def __sub__(self, other):
        if(type(other) is float):
            new_l = [x - other for x in self.t]
            new_pt = PointND(*new_l)
        else:
            if(self.n != other.n):
                raise ValueError("Cannot operate on points with different cardinalities.")
            new_l = []
            for num1,num2 in zip(self.t,other.t):
                new_l.append(num1-num2)
            new_pt = PointND(*new_l)
        return new_pt

    def __neg__(self):
        new_l = [-x for x in self.t]
        new_pt = PointND(*new_l)
        return new_pt

    def __mul__(self, other):
        if(type(other) is float):
            new_l = [x * other for x in self.t]
            new_pt = PointND(*new_l)
            return new_pt
        else:
            raise ValueError("Cannot operate non-float values.")

    def __rmul__(self, other):
        if(type(other) is float):
            new_l = [x * other for x in self.t]
            new_pt = PointND(*new_l)
            return new_pt
        else:
            raise ValueError("Cannot operate non-float values.")

    def __truediv__(self, other):
        if(type(other) is float):
            new_l = [x / other for x in self.t]
            new_pt = PointND(*new_l)
            return new_pt
        else:
            raise ValueError("Cannot operate non-float values.")

    def __getitem__(self, item):
        if item >= self.n:
            raise ValueError("Index out of range.")
        return list(self.t)[item]

    def __eq__(self, other):
        if(self.n != other.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        for num1,num2 in zip(self.t,other.t):
            if(num1 != num2):
                return False
        return True

    def __ne__(self, other):
        return not self==other

    def dist_org(self):
        l=[0.0]*self.n
        orig = PointND(*l)
        return self.distanceFrom(orig)


    def __gt__(self, other):
        if(self.n != other.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        return self.dist_org() > other.dist_org()

    def __ge__(self, other):
        if(self.n != other.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        return self.dist_org() >= other.dist_org()

    def __lt__(self, other):
        if(self.n != other.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        return self.dist_org() < other.dist_org()

    def __le__(self, other):
        if(self.n != other.n):
            raise ValueError("Cannot operate on points with different cardinalities.")
        return self.dist_org() <= other.dist_org()

class Point3D(PointND):
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = x
        self.y = y
        self.z = z
        super().__init__(x,y,z)

class PointGroup:
    def __init__(self, **kwargs):
        self._pointMap = {}
        if not kwargs:
            self.n = 0
        elif("pointList" in kwargs):
            points = kwargs["pointList"]
            if not points:
                raise ValueError("'pointList' input parameter cannot be empty.")
            self.n = points[0].n
            for point in points:
                self.addPoint(point)
        else:
            raise KeyError("'pointList' input parameter not found.")


    def addPoint(self, point):
        if (self.n != point.n):
            raise ValueError("Cannot add point {0}. Expecting a point with cardinality {1}.".format(point, self.n))
        else:
            self._pointMap[point.__hash__()] = point

    def count(self):
        return len(self._pointMap)

    def computeBoundingHyperCube(self):
        d_max = []
        d_min = []
        points = list(self._pointMap.values())
        first_p = points.pop()
        for i in range(self.n):
            d_max.append(first_p[i])
            d_min.append(first_p[i])
        for point in points:
            for i in range(self.n):
                d_max[i] = max(point[i],d_max[i])
                d_min[i] = min(point[i],d_min[i])
        min_pt = PointND(*d_min)
        max_pt = PointND(*d_max)
        return (min_pt,max_pt)

    def computeNearestNeighbors(self, otherPointGroup):
        result = []
        mypoints = list(self._pointMap.values())
        mypoints.sort()
        for mypoint in mypoints:
            otherpoints = list(otherPointGroup._pointMap.values())
            min_point = otherpoints.pop()
            min_dist = mypoint.distanceFrom(min_point)
            for otherpoint in otherpoints:
                temp = mypoint.distanceFrom(otherpoint)
                if (min_dist > temp):
                    min_dist = temp
                    min_point = otherpoint
            result.append((mypoint,min_point))
        return result

    def __iter__(self):
        return iter(self._pointMap.values())

    def __add__(self, other):
        self.addPoint(other)
        return self

    def __sub__(self, other):
        for point in self:
            if other == point:
                del self._pointMap[other.__hash__()]
        return self

    def __contains__(self, item):
        for point in self:
            if item == point:
                return True
        return False

