from math import sin,radians,cos,asin,sqrt,atan,degrees,atan2

def cal_two_points_distance(lon1, lat1, lon2, lat2):
    r = 6371000
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    d_lon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(d_lon / 2) ** 2
    c = 2 * asin(sqrt(a))
    
    return c * r

def cal_point_to_link_distance(point_lon, polint_lat, link_s_lon, link_s_lat, link_e_lon, link_e_lat):
    a = cal_two_points_distance(link_s_lon, link_s_lat, link_e_lon, link_e_lat)
    b = cal_two_points_distance(point_lon, polint_lat, link_e_lon, link_e_lat)
    c = cal_two_points_distance(point_lon, polint_lat, link_s_lon, link_s_lat)

    if a ** 2 + b ** 2 < c ** 2:
        dis_to_link = b
        pos_in_link = a
    elif a ** 2 + c ** 2 < b ** 2:
        dis_to_link = c
        pos_in_link = 0
    else:
        dis_to_link = sqrt((a + b + c) * (a + b - c) * (a + c - b) * (b + c - a)) / 2 / a
        # if c ** 2 - dis_to_link ** 2 < 0:
        #   print point_lon, polint_lat, link_s_lon, link_s_lat, link_e_lon, link_e_lat
        #   print a, b, c, dis_to_link
        tmp = max(c ** 2 - dis_to_link ** 2, 0)
        pos_in_link = sqrt(tmp)
    return(dis_to_link, pos_in_link)


def getDegree(lon1, lat1, lon2, lat2):

  rad_lat1 = radians(lat1)
  rad_lon1 = radians(lon1)
  rad_lat2 = radians(lat2)
  rad_lon2 = radians(lon2)
  d_lon = rad_lon2 - rad_lon1
  y = sin(d_lon) * cos(rad_lat2)
  x = cos(rad_lat1) * sin(rad_lat2) - sin(rad_lat1) * cos(rad_lat2) * cos(d_lon)
  degree = degrees(atan2(y, x))
  degree = (degree + 360) % 360
  return degree

# print getDegree(0,0,0.4,0.3)
# print cal_two_points_distance(116.355815,39.932347, 116.360621,39.932446)
# print cal_point_to_link_distance(116.433792,39.931344,116.433921,39.928481,116.433749,39.933384)