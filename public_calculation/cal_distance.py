from math import sin,radians,cos,asin,sqrt,atan

def cal_two_points_distance(lon1, lat1, lon2, lat2):
    r = 6371000
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
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
        pos_in_link = sqrt(c ** 2 - dis_to_link ** 2)
    return(dis_to_link, pos_in_link)



# print cal_two_points_distance(116.355815,39.932347, 116.360621,39.932446)