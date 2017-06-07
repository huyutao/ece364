import point
from prelab08addon import performProcessing


def createPoint(dataString):
    try:
        number = dataString.split(",")
        number = list(map(float,number))
        p = point.PointND(*number)
    except:
        return "Cannot instantiate an object with non-float values."
    return p

def distanceBetween(point1, point2):
    try:
        distance = point1.distanceFrom(point2)
    except:
        return "Some error,Cannot calculate distance between points"
    return distance

def checkVicinity(point, pointList, radius):
    in_rad = 0
    out_rad = 0
    excep = 0
    for p in pointList:
        try:
             distance = point.distanceFrom(p)
             if(distance <= radius):
                 in_rad += 1
             else:
                 out_rad += 1
        except:
            excep += 1
    return (in_rad,out_rad,excep)

def checkOperation(*args):
    try:
        performProcessing(*args)
    except ConnectionRefusedError:
        raise
    except OSError as ose:
        return "The following Error occurred: {}".format(ose.__class__.__name__)
    except:
        return False
    else:
        return True



if __name__ == "__main__":
    print(createPoint("3.14,2.701,19.77"))
    print(createPoint("4.98,3FA2,None"))
    p1=createPoint("1,2,3")
    p2=createPoint("2,3,4")
    p3=createPoint("1,2,3,4")
    print(distanceBetween(p1,p2))
    print(distanceBetween(p1,p3))
    point_list = [point.PointND(1.0,4.0,7.0),point.PointND(6.0,3.0,4.0),point.PointND(9.0,0.0,5.0),createPoint("4.98,3FA2,None")]
    print(checkVicinity(createPoint("2,2,2"), point_list, 6))
    print(checkOperation("a"))



