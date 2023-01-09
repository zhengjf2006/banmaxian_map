
class Network:
    def __init__(self, network_name, junctions, segments, sub_segments, movements, nodes):
        self.network_name = network_name
        self.junctions = junctions
        self.segments = segments
        self.sub_segments = sub_segments
        self.movements = movements
        self.nodes = nodes

    def __repr__(self):
        L = ['%s=%r' % (key, value) for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))


class Node:
    def __init__(self, node_id, lon, lat):
        self.node_id = node_id
        self.lon = lon
        self.lat = lat

    def __repr__(self):
        L = ['%s=%r' % (key, value) for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

class Junction:
    def __init__(self, junction_id, junction_name, lon, lat, city_id, sub_junction_ids, 
        traffic_light, pedestrian, roundabout, ramp_type, pedestrian_island, 
        city_boundary, degree, geometric_shape, in_segments, out_segments, movements):
        self.junction_id = junction_id
        self.junction_name = junction_name
        self.lon = lon
        self.lat = lat
        self.city_id = city_id
        self.sub_junction_ids = sub_junction_ids
        self.traffic_light = traffic_light
        self.pedestrian = pedestrian
        self.roundabout = roundabout
        self.ramp_type = ramp_type
        self.pedestrian_island = pedestrian_island
        self.city_boundary = city_boundary
        self.degree = degree
        self.geometric_shape = geometric_shape
        self.in_segments = in_segments
        self.out_segments = out_segments
        self.movements = movements

    def __repr__(self):
        L = ['%s=%r' % (key, value) for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))


class SubSegment:
    def __init__(self, sub_segment_id, next_sub_segment_id, start_pos, end_pos, lane_num, lane_info, 
        level, speed_limit, geometric_shape, sub_segment_type, city_id):
        self.sub_segment_id = sub_segment_id
        self.next_sub_segment_id = next_sub_segment_id
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.lane_num = lane_num
        self.lane_info = lane_info
        self.level = level
        self.speed_limit = speed_limit
        self.geometric_shape = geometric_shape
        self.sub_segment_type = sub_segment_type
        self.city_id = city_id

    def __repr__(self):
        L = ['%s=%r' % (key, value) for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

class Segment:
    def __init__(self, segment_id, upstream_junction_id, downstream_junction_id, 
        pair_segment_id, length, segment_type, segment_name, city_id, main_segment_id, 
        side_segment_ids, sub_segment_ids, direction, angle, lanes, speed_limit, node_list, length_list):
        self.segment_id = segment_id
        self.upstream_junction_id = upstream_junction_id
        self.downstream_junction_id = downstream_junction_id
        self.pair_segment_id = pair_segment_id
        self.length = length
        self.segment_type = segment_type
        self.segment_name = segment_name
        self.city_id = city_id
        self.main_segment_id = main_segment_id
        self.side_segment_ids = side_segment_ids
        self.sub_segment_ids = sub_segment_ids
        self.direction = direction
        self.angle = angle
        self.lanes = lanes
        self.speed_limit = speed_limit
        self.node_list = node_list
        self.length_list = length_list

    def __repr__(self):
        L = ['%s=%r' % (key, value) for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))


class Movement:
    def __init__(self, movement_id, upstream_segment_id, downstream_segment_id, 
        related_movement_id, junction_id, sub_junction_id, junction_link_length, in_segement_length, out_segment_length, 
        entrance_exit_lane_ids_pair, movement_name, min_green, waiting_area, movement_type, city_id, turn_degree, trajectories):
        self.movement_id = movement_id
        self.upstream_segment_id = upstream_segment_id
        self.downstream_segment_id = downstream_segment_id
        self.related_movement_id = related_movement_id
        self.junction_id = junction_id
        self.sub_junction_id = sub_junction_id
        self.junction_link_length = junction_link_length
        self.in_segement_length = in_segement_length
        self.out_segment_length = out_segment_length
        self.entrance_exit_lane_ids_pair = entrance_exit_lane_ids_pair
        self.movement_name = movement_name
        self.min_green = min_green
        self.waiting_area = waiting_area
        self.movement_type = movement_type
        self.city_id = city_id
        self.turn_degree = turn_degree
        self.trajectories = trajectories

    def __repr__(self):
        L = ['%s=%r' % (key, value) for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))





