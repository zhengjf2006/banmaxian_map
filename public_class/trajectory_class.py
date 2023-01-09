class TrajectoryPoint:
    def __init__(self, lon, lat, timestamp, segment_id, position, poi_id):
        self.lon = lon
        self.lat = lat
        self.timestamp = timestamp
        self.segment_id = segment_id
        self.position = position
        self.poi_id = poi_id


    def __repr__(self):
        L = ['%s=%r' % (key, value) for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

class Trajectory:
    def __init__(self, trip_id, driver_id, trajectory_points):
        self.trip_id = trip_id
        self.driver_id = driver_id
        self.trajectory_points = trajectory_points


    def __repr__(self):
        L = ['%s=%r' % (key, value) for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

class MovementTrajectory(Trajectory):
    def __init__(self, trip_id, driver_id, trajectory_points, traj_index):
        self.trip_id = trip_id
        self.driver_id = driver_id
        self.trajectory_points = trajectory_points
        self.traj_index = traj_index


    def __repr__(self):
        L = ['%s=%r' % (key, value) for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))