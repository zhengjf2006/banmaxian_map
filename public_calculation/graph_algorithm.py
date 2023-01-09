

def find_shortest_path_folyed(network):
    shortest_path_table = {}
    i = 0
    for junction_id, junction in network.junctions.items():
        shortest_path_table.setdefault(junction_id, {})
        shortest_path_table[junction_id][junction_id] = [0, []]

    for segment_id, segment in network.segments.items():
        upstream_junction_id = segment.upstream_junction_id
        downstream_junction_id = segment.downstream_junction_id
        path_length = segment.length
        shortest_path_table.setdefault(upstream_junction_id, {})
        shortest_path_table[upstream_junction_id][downstream_junction_id] = [path_length, [segment_id]]


    for mid_junction_id, mid_junction in network.junctions.items():
        # print mid_junction_id, i
        i += 1
        for start_junction_id, start_junction in network.junctions.items():
            for end_junction_id, end_junction in network.junctions.items():
                if shortest_path_table[start_junction_id].get(mid_junction_id) is not None and shortest_path_table[mid_junction_id].get(end_junction_id) is not None:
                    tmp_length = shortest_path_table[start_junction_id][mid_junction_id][0] + shortest_path_table[mid_junction_id][end_junction_id][0]
                    tmp_path = shortest_path_table[start_junction_id][mid_junction_id][1] + shortest_path_table[mid_junction_id][end_junction_id][1]
                    if shortest_path_table[start_junction_id].get(end_junction_id) is  None or tmp_length < shortest_path_table[start_junction_id][end_junction_id][0]:
                        shortest_path_table[start_junction_id][end_junction_id] = [tmp_length, tmp_path]

    return(shortest_path_table)




    # visit_junctions = {}
    # visit_queue = Queue()
    # visit_queue.put(start_junction_id)
    # for node_id, node in network.nodes.items():
    #     visit_junctions[node_id] = False
    # visited[start_junction_id] = True
    # last_queue_len = 0
    # while last_queue_len == len(visit_queue):
    #     for 

    # for segment_id, segment in network.nodes[start_junction_id].out_segments.items():
    #     shortest_path[]