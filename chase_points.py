#short program showing the value of points spent

'''
class PointValue(object):
    def __init__(self):
        self.points = None
        self.travel = 616.25 / 41083
        self.amazon = 339.44 / 42430


    def dollar_val(self, points, ratio):
        self.points = points
        self.ratio = ratio
        value = points * ratio
        self.value = value
        return value

flight_pts = 45092

hotel_pts = 21153

mom_trip = PointValue()

print(mom_trip.dollar_val(flight_pts + hotel_pts, mom_trip.travel))

'''
point_conversion_travel = 616.25 / 41083
point_conversion_amazon = 339.44 / 42430

flight_pts = 45092

hotel_pts = 21153


def dollar_val(x, ratio):
    money = x * ratio
    return money

print("Chase Ultimate Rewards have a value of $%.3f per dollar on travel" % point_conversion_travel)

print("Chase Ultimate Rewards have a value of $%.3f per dollar on Amazon" % point_conversion_amazon)

print("your %d points spent on flights are worth $%.3f" % (flight_pts, dollar_val(flight_pts, point_conversion_travel)))

print("your %d points spent on hotels are worth $%.3f" % (hotel_pts, dollar_val(hotel_pts, point_conversion_travel)))

print("%d points spent on Amazon.com are worth $%.3f" % (flight_pts, dollar_val(flight_pts, point_conversion_amazon)))

print("%d points spent on Amazon.com are worth $%.3f" % (hotel_pts, dollar_val(hotel_pts, point_conversion_amazon)))
