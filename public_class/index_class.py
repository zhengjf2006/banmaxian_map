class MovementIndex:
    def __init__(self, movement_id, junction_id, city_id, date, hour, traj_num, stop_delay, stop_num, stop_rate, queue_length):
        self.movement_id = movement_id
        self.junction_id = junction_id
        self.city_id = city_id
        self.date = date
        self.hour = hour
        self.traj_num = traj_num
        self.stop_delay = stop_delay
        self.stop_num = stop_num
        self.stop_rate = stop_rate
        self.queue_length = queue_length

    def __repr__(self):
        L = ['%s=%r' % (key, value) for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))

class StopIndex:
    def __init__(self, stop_delay, stop_start_time, stop_queue):
        self.stop_delay = stop_delay
        self.stop_start_time = stop_start_time
        self.stop_queue = stop_queue

    def __repr__(self):
        L = ['%s=%r' % (key, value) for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))


class TrajectoryIndex:
    def __init__(self, timestamp_pass_stopbar, stop_index_before, stop_index_after):
        self.timestamp_pass_stopbar = timestamp_pass_stopbar
        self.stop_index_before = stop_index_before
        self.stop_index_after = stop_index_after

    def __repr__(self):
        L = ['%s=%r' % (key, value) for key, value in self.__dict__.items()]
        return '%s(%s)' % (self.__class__.__name__, ', '.join(L))
