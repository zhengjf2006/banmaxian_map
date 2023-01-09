from network import build_network

if __name__ == "__main__":
    # transition_probability = probability_function.get_gaussian_probability(50)
    # print transition_probability
    # exit(1)
    area = "aa6"
    osmfile = area + ".osm"

    network = build_network.build_network_topology(osmfile)

    segments = network.segments

    segment_in_file_txt = ''
    for segment_id in segments.keys():
        segment = segments[segment_id]

        segment_data_ls = []
        segment_data_ls.append(segment_id)
        segment_data_ls.append(segment['segment_name'])
        segment_data_ls.append(segment['upstream_junction_id'])
        segment_data_ls.append(segment['downstream_junction_id'])
        segment_data_ls.append(','.join(segment['node_list']))

        segment_in_file_txt += segment_id

    print(network)
