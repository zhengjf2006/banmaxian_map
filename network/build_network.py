# -*- coding: utf-8 -*-
import json
import xml.dom.minidom
# import matplotlib
# import matplotlib.pyplot as plt
from public_class import map_class
from public_calculation import cal_position
import copy
# from mpl_toolkits.basemap import Basemap
# from lxml import etree
# import xmltodict

# def iter_element(file_parsed, file_length, file_write):
#     current_line = 0
#     try:
#         for event, element in file_parsed:
#             current_line += 1
#             print current_line/float(file_length)
#             elem_data = etree.tostring(element)
#             elem_dict = xmltodict.parse(elem_data, attr_prefix="", cdata_key="")
#             if (element.tag == "node"):
#                 elem_jsonStr = json.dumps(elem_dict["node"])
#                 file_write.write(elem_jsonStr + "\n")
#             element.clear()
#             while element.getprevious() is not None:
#                 del element.getparent()[0]
#     except:
#         pass

# def get_movement_info_json(self):
#     movement_info_json = {}
#     for node_id in self.nodes.keys():
#         node = self.nodes[node_id]
#         for movement_id in node.movements.keys():
#             movement = node.movements[movement_id]
#             phase_id = movement.phase_id

#             land_marks = movement.get_landmarks(self)
#             if not (node_id in movement_info_json):
#                 movement_info_json[node_id] = {}
#             movement_info_json[node_id]["Phase" + str(phase_id)] = land_marks
#     json_string = json.dumps(movement_info_json)
#     return json_string

# def add_node(self, node_id, latitude, longitude):
#     if self.nodes is None:
#         self.nodes = {}

#     node = Node(node_id, latitude, longitude)
#     self.nodes[node_id] = node

# def add_link(self, link_id, latitude_list, longitude_list):
#     if self.links is None:
#         self.links = {}

#     link = Link(link_id, latitude_list, longitude_list)
#     self.links[link_id] = link

# def get_json_nodes_location_info(self):
#     nodes_loc_dict = {}
#     for node_id in self.nodes:
#         latitude = self.nodes[node_id].latitude
#         longitude = self.nodes[node_id].longitude

#         nodes_loc_dict[node_id] = [[latitude, longitude], self.nodes[node_id].name_string]
#     nodes_loc_json = json.dumps(nodes_loc_dict)
#     return nodes_loc_json

# def get_ts_diagram_json(self, return_type="str"):
#     ts_diagram_dict = {}
#     for node_id in self.nodes.keys():
#         node = self.nodes[node_id]
#         movements = node.movements
#         if movements is None:
#             continue

#         for movement_id in movements.keys():
#             movement = movements[movement_id]
#             phase_id = str(movement.phase_id)

#             ts_trajectory = movement.ts_trajectory
#             if ts_trajectory is None:
#                 continue
#             if not ("time_in_cycle" in ts_trajectory.keys()):
#                 continue

#             local_trajs_dict = {"time": ts_trajectory["time_in_cycle"],
#                                 "distance": ts_trajectory["distance"],
#                                 "time_stamp": ts_trajectory["time_stamp"]}

#             if not (node_id in ts_diagram_dict):
#                 ts_diagram_dict[node_id] = {}

#             ts_diagram_dict[node_id][phase_id] = local_trajs_dict

#         if not (node_id in ts_diagram_dict.keys()):
#             ts_diagram_dict[node_id] = {}

#         phases_list = ["1", "2", "3", "4", "5", "6", "7", "8"]
#         for phase_id in phases_list:
#             if not (phase_id in ts_diagram_dict[node_id].keys()):
#                 ts_diagram_dict[node_id][phase_id] = {"time": [], "distance": []}
#     if return_type == "str":
#         ts_diagram_json = json.dumps(ts_diagram_dict, default=str)
#         return ts_diagram_json
#     else:
#         return ts_diagram_dict

# def get_delay_diagram_json(self, return_type="str"):
#     delay_diagram_dict = {}
#     max_tod = 0
#     max_delay = 0
#     for node_id in self.nodes:
#         node = self.nodes[node_id]
#         movements = node.movements
#         if movements is None:
#             continue

#         for movement_id in movements:
#             movement = movements[movement_id]
#             phase_id = str(movement.phase_id)
#             delay_information = movement.delay_dict
#             if delay_information is None:
#                 continue

#             stop_delay_list = delay_information["stop_delay"]
#             date_time_list = delay_information["date_time"]
#             stop_pos_list = delay_information["stop_pos"]

#             if len(stop_delay_list) > 0:
#                 max_tod = np.max([max_tod, np.max(date_time_list)])
#                 max_delay = np.max([max_delay, np.max(stop_delay_list)])

#             if not (node_id in delay_diagram_dict.keys()):
#                 delay_diagram_dict[node_id] = {}

#             delay_diagram_dict[node_id][phase_id] =\
#                 [stop_delay_list, date_time_list, stop_pos_list]

#         if not (node_id in delay_diagram_dict.keys()):
#             delay_diagram_dict[node_id] = {}

#         phases_list = ["1", "2", "3", "4", "5", "6", "7", "8"]
#         for phase_id in phases_list:
#             if not (phase_id in delay_diagram_dict[node_id].keys()):
#                 delay_diagram_dict[node_id][phase_id] = [[], [], []]

#     if max_delay == 0:
#         max_delay = 100

#     if max_delay > 200:
#         max_delay = 200
#     visualization_dict = {"details": delay_diagram_dict, "max_delay": max_delay, "max_tod": max_tod}

#     if return_type == "str":
#         delay_diagram_json = json.dumps(visualization_dict, default=str)
#         return delay_diagram_json
#     return visualization_dict

# def get_signal_status_json(self):
#     signal_status_dict = {}

#     # iteration for node
#     for node_id in self.nodes.keys():
#         node = self.nodes[node_id]

#         signal_plan = node.signal_plan

#         if signal_plan is None:
#             continue
#         signal_plan_dict = signal_plan.signal_plan_dict

#         if not (node_id in signal_status_dict.keys()):
#             signal_status_dict[node_id] = {}

#         for reference_time in signal_plan_dict.keys():
#             local_signal = signal_plan_dict[reference_time]

#             cycle_length = int(local_signal.cycle_length)
#             phases = local_signal.phases

#             for plus_sec in range(cycle_length + 1):
#                 current_time = reference_time + plus_sec
#                 date_time = cvt_time.timestamp2datetime(current_time)
#                 date_time_string = cvt_time.get_date_time_string(date_time)

#                 if not (date_time_string in signal_status_dict[node_id].keys()):
#                     signal_status_dict[node_id][date_time_string] = {}

#                 for phase_id in phases.keys():
#                     str_name = "signal-status-" + str(phase_id)
#                     signal_status_dict[node_id][date_time_string][str_name] = 0

#             for phase_id in phases.keys():
#                 green_start = phases[phase_id].green_start
#                 green_duration = int(phases[phase_id].green_start)

#                 for plus_sec in range(green_duration):
#                     current_time = reference_time + green_start + plus_sec
#                     date_time = cvt_time.timestamp2datetime(current_time)
#                     date_time_string = cvt_time.get_date_time_string(date_time)

#                     str_name = "signal-status-" + str(phase_id)
#                     if not (date_time_string in signal_status_dict[node_id].keys()):
#                         continue
#                     signal_status_dict[node_id][date_time_string][str_name] = 1

#     signal_status_json = json.dumps(signal_status_dict)
#     return signal_status_json

# def clear_node_signal_plan(self):
#     for node_id in self.nodes.keys():
#         self.nodes[node_id].signal_plan = None

# def output_matched_trajectories(self, output_folder, additional_file_name="_"):
#     output_path = output_folder

#     # output the raw trajectories data
#     raw_trajs_file_name = os.path.join(output_path, additional_file_name + "-raw_trajs.json")
#     with open(raw_trajs_file_name, "w") as raw_trajs_file:
#         raw_trajs_file.write(json.dumps(self.raw_trajectories, default=json_dump_default))

#     # output the matched trajectory data
#     matched_trajs = {}
#     for node_id in self.nodes.keys():
#         node = self.nodes[node_id]
#         movements = node.movements
#         if movements is None:
#             continue

#         for movement_id in movements:
#             movement = movements[movement_id]

#             ts_trajectories = movement.matched_trajectory
#             if ts_trajectories is None:
#                 continue

#             if not (node_id in matched_trajs):
#                 matched_trajs[node_id] = {}

#             matched_trajs[node_id][movement_id] = ts_trajectories

#     matched_trajs_file_name = os.path.join(output_path,
#                                            additional_file_name + "-matched_trajs.json")

#     with open(matched_trajs_file_name, "w") as matched_trajs_file:
#         matched_trajs_file.write(json.dumps(matched_trajs))

# def clear_raw_and_movement_trajs(self):
#     self.raw_trajectories = {}
#     self.delete_movement_trajs()

# def delete_movement_trajs(self):
#     for node_id in self.nodes.keys():
#         node = self.nodes[node_id]
#         movements = node.movements
#         if movements is None:
#             continue
#         for movement_id in movements:
#             self.nodes[node_id].movements[movement_id].ts_trajectory = None
#             self.nodes[node_id].movements[movement_id].raw_trajectory = None
#             self.nodes[node_id].movements[movement_id].matched_trajectory = None

# def delete_node_trajs(self):
#     for node_id in self.nodes.keys():
#         self.nodes[node_id].raw_trajectories = {"time_stamp": [], "latitudes": [],
#                                                 "longitudes": [], "trip_id": []}

# def get_node_range(self, node_id, buffer=0):
#     radius = 6371000
#     node = self.nodes[node_id]

#     movements = node.movements

#     all_latitudes = []
#     all_longitudes = []

#     for movement_id in movements.keys():
#         movement = movements[movement_id]
#         in_link_id = movement.in_link_id
#         out_link_id = movement.out_link_id

#         in_link_latitudes = self.links[in_link_id].latitude_list
#         in_link_longitudes = self.links[in_link_id].longitude_list

#         out_link_latitudes = self.links[out_link_id].latitude_list
#         out_link_longitudes = self.links[out_link_id].longitude_list

#         all_latitudes += in_link_latitudes
#         all_latitudes += out_link_latitudes

#         all_longitudes += in_link_longitudes
#         all_longitudes += out_link_longitudes

#     lat_min = np.min(all_latitudes)
#     lat_max = np.max(all_latitudes)

#     lon_min = np.min(all_longitudes)
#     lon_max = np.max(all_longitudes)

#     lat_max += buffer / radius * 180 / pi
#     lat_min -= buffer / radius * 180 / pi

#     lon_min -= buffer / radius * 2 * 180 / pi
#     lon_max += buffer / radius * 2 * 180 / pi

#     return [lat_min, lat_max, lon_min, lon_max]

def express_osm_file(file_name):
    # osmfile = "test_map.osm"0
    osmfile = file_name
    dom = xml.dom.minidom.parse(osmfile)
    root = dom.documentElement
    nodes = root.getElementsByTagName("node")
    ways = root.getElementsByTagName("way")
    node_dict = {}
    way_dict = {}
    junction_dict = {}
    max_lon = -180.0
    min_lon = 0.0
    max_lat = 0.0
    min_lat = 90.0

    # fig = plt.figure()
    # print(len(nodes))
    for node in nodes:
        node_id = node.getAttribute("id")
        node_lat = float(node.getAttribute("lat"))
        node_lon = float(node.getAttribute("lon"))
        if float(node_lon) > max_lon:
            max_lon = float(node_lon)
        if float(node_lon) < min_lon:
            min_lon = float(node_lon)
        if float(node_lat) > max_lat:
            max_lat = float(node_lat)
        if float(node_lon) < min_lat:
            min_lat = float(node_lat)
        node_dict[node_id] = {}
        node_dict[node_id]["node_id"] = node_id
        node_dict[node_id]["lon"] = float(node_lon)
        node_dict[node_id]["lat"] = float(node_lat)
        node_dict[node_id]["degree"] = 0
        
        tags = node.getElementsByTagName("tag")
        tag_dict = {}
        for tag in tags:
            key = tag.getAttribute("k")
            value = tag.getAttribute("v")
            tag_dict[key] = value

        node_dict[node_id]["tag"] = tag_dict
        # print node_dict[node_id]

        # if len(tag) > 0:
        #     print "54354353", tag, len(tag)
        #     plt.scatter(node_lon, node_lat)
        # else:
        #     continue
        # for i in xrange(0, len(tag)):
           #  key = tag[0].getAttribute("k")
           #  value = tag[0].getAttribute("v")
           #  print key,value

        # node_dict[node_id] = (node_lat, node_lon)
        # print node, len(node.childNodes), node_lat
        # for i in xrange(0, len(node.childNodes)):
        #     print node.childNodes[i].nodeName, node.childNodes[i].nodeValue
        # exit(1)

    k = 0
    colors = ["blue", "red", "green", "yellow", "cyan", "magenta", "black", "brown", "darkgray", "darkblue", "ivory", "mediumpurple", "teal",
     "sandybrown", "royalblue", "pink", "seashell", "skyblue", "wheat", "lightblue", "lightgoldenrodyellow", "lightsalmon", "lightseagreen",
     "lightskyblue", "lavender", "lavenderblush", "gold", "firebrick", "darkslategray", "darkorchid"]

    for way in ways:
        way_id = way.getAttribute("id")
        way_nodes = way.getElementsByTagName("nd")
        tmp_way_nodes = []
        for node in way_nodes:
            node_id = node.getAttribute("ref")
            tmp_way_nodes.append(node_id)

        tags = way.getElementsByTagName("tag")
        tag_dict = {}
        for tag in tags:
            key = tag.getAttribute("k")
            value = tag.getAttribute("v")
            tag_dict[key] = value

        
        # if tag_dict.get("highway") is not None and tag_dict["highway"] == "cycleway":
        # if tag_dict.get("highway") is not None and tag_dict["highway"] != "service" and tag_dict["highway"] != "footway" and tag_dict["highway"] != "cycleway" and tag_dict["highway"] != "residential" and tag_dict["highway"] != "path" and tag_dict["highway"] != "living_street" and tag_dict["highway"] != "unclassified" and tag_dict["highway"] != "steps" and tag_dict.get("lanes") is not None :
        if tag_dict.get("highway") is not None and tag_dict.get("lanes") is not None and tag_dict["highway"] != "footway" and tag_dict["highway"] != "cycleway":
            # for i in xrange(0, len(tmp_way_nodes) - 1):
            #     cur_node_id = tmp_way_nodes[i]
            #     next_node_id = tmp_way_nodes[i + 1]
            #     plt.plot([node_dict[cur_node_id]["lon"], node_dict[next_node_id]["lon"]], [node_dict[cur_node_id]["lat"], node_dict[next_node_id]["lat"]], c = colors[k])
            
            node_dict[tmp_way_nodes[0]]["degree"] += 1
            node_dict[tmp_way_nodes[-1]]["degree"] += 1

            way_dict[way_id] = {}
            way_dict[way_id]["way_id"] = way_id
            way_dict[way_id]["way_nodes"] = tmp_way_nodes
            way_dict[way_id]["tag"] = tag_dict
    
        #     k += 1
            # print way_dict[way_id]
    # print k

        
    for node_id, node in node_dict.items():
        # if node["degree"] > 2 or node["degree"] == 1:
        if node["degree"] > 0:
            junction_dict[node_id] = node
            # print node
            # plt.scatter(node_dict[node_id]["lon"], node_dict[node_id]["lat"], s = 30)

    # plt.show()



    # junction_file_path = "junction.json"
    # with open(junction_file_path, "wb") as junction_file:
    #     json.dump(junction_dict, junction_file)

    # for way_id, way in way_dict.items():
    #     sub_segment_dict[way_id] = way
    #     print way
    # sub_segment_file_path = "sub_segment.json"
    # with open(sub_segment_file_path, "wb") as sub_segment_file:
    #     json.dump(sub_segment_dict, sub_segment_file)
    
    # k = 0
    # colors = ["blue", "red", "green", "yellow"]
    # for way in ways:
    # 	way_id = way.getAttribute("id")
    # 	nodes = way.getElementsByTagName("nd")
    # 	tags = way.getElementsByTagName("tag")
    # 	print_flag = 0
    # 	print len(tags)

    # 	for tag in tags:
    # 		key = tag.getAttribute("k")
    # 		value = tag.getAttribute("v")
    # 		if key == "highway":
    # 			print_flag = 1
    # 		print key, value
    # 	if print_flag == 1:
    # 		for node in nodes:
    # 			node_id = node.getAttribute("ref")
    # 			if node_id in node_dict:
    # 				plt.scatter(node_dict[node_id][0], node_dict[node_id][1], c=colors[k % len(colors)])
    # 		k += 1
    # print k, len(ways) 
    # plt.show()

    # print(','.join([max_lon, min_lon, max_lat, min_lat]))

    return junction_dict, way_dict, node_dict



def get_degree_name(degree):
    if 0 <= degree < 45 or 315 <= degree < 360:
        return "N"
    if 45 <= degree < 135:
        return "E"
    if 135 <= degree < 225:
        return "S"
    if 225 <= degree < 315:
        return "W"

def build_network_topology(osmfile):
    tmp_junctions, tmp_segments, tmp_nodes = express_osm_file(osmfile)
    print(tmp_junctions)
    # print(','.join([len(tmp_junctions), len(tmp_segments)]))
    nodes = {}
    junctions = {}
    segments = {}
    movements = {}

    for node_id, node in tmp_nodes.items():
        lon = node["lon"]
        lat = node["lat"]
        nodes[node_id] = map_class.Node(node_id, lon, lat)

    # print tmp_junctions

    for junction_id, junction in tmp_junctions.items():
        traffic_signal_flag = 0
        if junction["tag"].get("highway") and junction["tag"]["highway"] == "traffic_signals":
            traffic_signal_flag = 1
        lon = junction["lon"]
        lat = junction["lat"]
        junction_name = ""
        degree = junction["degree"]
        city_id = "0"
        sub_junction_ids = None
        pedestrian = None
        roundabout = None
        ramp_type = None
        pedestrian_island = None
        city_boundary = None
        geometric_shape = None
        in_segment_dict = {}
        out_segment_dict = {}
        movement_dict = {}

        junctions[junction_id] = map_class.Junction(junction_id, junction_name, lon, lat, city_id, sub_junction_ids, 
        traffic_signal_flag, pedestrian, roundabout, ramp_type, pedestrian_island, 
        city_boundary, degree, geometric_shape, in_segment_dict, out_segment_dict, movement_dict)

    # for segment_id, segment in tmp_segments.items():
    #     segment["tag"]
    # print tmp_segments

    for segment_id, segment in tmp_segments.items():
        lanes = None
        node_list = segment["way_nodes"]
        upstream_junction_id = node_list[0]
        downstream_junction_id = node_list[-1]
        # print upstream_junction_id, downstream_junction_id
        pair_segment_id = segment_id + "1"
        segment_type = None
        city_id = "0"
        main_segment_id = segment_id + "0"
        side_segment_ids = None
        sub_segment_ids = None
        direction = None
        angle = None
        length = 0
        speed_limit = None
        segment_name = None
        length_list = [0]
        if segment["tag"].get("lanes") is not None:
            lanes = segment["tag"]["lanes"]

        if segment["tag"].get("maxspeed") is not None:
            speed_limit = segment["tag"]["maxspeed"]

        for i in range(0, len(node_list) - 1):
            length += cal_position.cal_two_points_distance(nodes[node_list[i]].lon, nodes[node_list[i]].lat, nodes[node_list[i + 1]].lon, nodes[node_list[i + 1]].lat)
            length_list.append(length)
        # print len(node_list), len(node_list)

        segments[main_segment_id] = map_class.Segment(main_segment_id, upstream_junction_id, downstream_junction_id, 
        pair_segment_id, length, segment_type, segment_name, city_id, main_segment_id, 
        side_segment_ids, sub_segment_ids, direction, angle, lanes, speed_limit, node_list, length_list)

        junctions[upstream_junction_id].out_segments[main_segment_id] = segments[main_segment_id]
        junctions[downstream_junction_id].in_segments[main_segment_id] = segments[main_segment_id]

        tmp_upstream_junction_id = downstream_junction_id
        tmp_downstream_junction_id = upstream_junction_id
        tmp_pair_segment_id = segment_id + "0"
        tmp_main_segment_id = segment_id + "1"

        node_list_reverse = copy.deepcopy(node_list)
        node_list_reverse.reverse()
        # print len(length_list), len(node_list_reverse)


        reverse_length_list = [0]
        reverese_length = 0
        for i in range(0, len(node_list_reverse) - 1):
            reverese_length += cal_position.cal_two_points_distance(nodes[node_list_reverse[i]].lon, nodes[node_list_reverse[i]].lat, nodes[node_list_reverse[i + 1]].lon, nodes[node_list_reverse[i + 1]].lat)
            reverse_length_list.append(reverese_length)


        segments[tmp_main_segment_id] = map_class.Segment(tmp_main_segment_id, tmp_upstream_junction_id, tmp_downstream_junction_id, 
        pair_segment_id, reverese_length, segment_type, segment_name, city_id, main_segment_id, 
        side_segment_ids, sub_segment_ids, direction, angle, lanes, speed_limit, node_list_reverse, reverse_length_list)

        junctions[tmp_upstream_junction_id].out_segments[tmp_main_segment_id] = segments[tmp_main_segment_id]
        junctions[tmp_downstream_junction_id].in_segments[tmp_main_segment_id] = segments[tmp_main_segment_id]

        

    for junction_id ,junction in junctions.items():
        for in_segment_id, in_segment in junction.in_segments.items():
            for out_segment_id, out_segment in junction.out_segments.items():
                movement_id = in_segment_id + out_segment_id
                upstream_segment_id = in_segment_id
                downstream_segment_id = out_segment_id
                related_movement_id = None
                sub_junction_id = None
                junction_link_length = 0
                in_segement_length = in_segment.length
                out_segment_length = out_segment.length
                entrance_exit_lane_ids_pair = None
                # movement_name = None
                min_green = None
                waiting_area = None
                movement_type = None
                city_id = "0"
                trajectories = []
                in_tmp_node_id1 = in_segment.node_list[0]
                in_tmp_node_id2 = in_segment.node_list[1]
                in_degree = cal_position.getDegree(nodes[in_tmp_node_id1].lon, nodes[in_tmp_node_id1].lat, nodes[in_tmp_node_id2].lon, nodes[in_tmp_node_id2].lat)

                out_tmp_node_id1 = out_segment.node_list[0]
                out_tmp_node_id2 = out_segment.node_list[1]
                out_degree = cal_position.getDegree(nodes[out_tmp_node_id1].lon, nodes[out_tmp_node_id1].lat, nodes[out_tmp_node_id2].lon, nodes[out_tmp_node_id2].lat)

                in_degree_string = get_degree_name(in_degree)
                out_degree_string = get_degree_name(out_degree)
                turn_degree = (out_degree - in_degree + 360) % 360
                degree_reverse = {"E":"W", "W":"E", "N":"S", "S":"N"}
                movement_name = degree_reverse[in_degree_string] + " to " + out_degree_string
                # print movement_name, in_degree, out_degree


                movements[movement_id] = map_class.Movement(movement_id, upstream_segment_id, downstream_segment_id, 
                    related_movement_id, junction_id, sub_junction_id, junction_link_length, in_segement_length, out_segment_length, 
                    entrance_exit_lane_ids_pair, movement_name, min_green, waiting_area, movement_type, city_id, turn_degree, trajectories)

                junction.movements[movement_id] = movements[movement_id]

    network_name = "Ann Arbor"
    sub_segments = None
    # print(','.join([len(junctions), len(segments), len(movements)]))

    network = map_class.Network(network_name, junctions, segments, sub_segments, movements, nodes)

    return(network)


# if __name__ == "__main__":
#     osmfile = "big_map.osm"
#     build_network_topology(osmfile)
