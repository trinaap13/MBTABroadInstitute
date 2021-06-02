import re
import requests


def get_subway_routes_long_names():
    """Access the MBTA API to get a list of subway route long names"""
    mbta_api_url = requests.get('https://api-v3.mbta.com/routes/?fields%5Broute%5D=long_name&filter[type]=0,1')
    mbta_api_url_json_format = mbta_api_url.json()
    route_data_dict = mbta_api_url_json_format['data']

    # Find the long name for the routes
    for route in route_data_dict:
        route_list = route['attributes']['long_name']
        print(route_list)

print('\nQUESTION 2 PARTITION\n')

def subway_route_stops_and_connections():
    """Access MBTA API to find routes with the most/least stops and that connect two or more subway routes"""
    route_stops = requests.get('https://api-v3.mbta.com/stops?filter[route_type]=0,1&include=route,parent_station')
    route_stops_json_format = route_stops.json()
    route_stops_data_dict = route_stops_json_format['data']

    total_route_stop_dict = {'Red Line': 0, 'Mattapan Trolley': 0, 'Orange Line': 0, 'Green Line (B)': 0,
                             'Green Line (C)': 0, 'Green Line (D)': 0, 'Green Line (E)': 0, 'Blue Line': 0
                             }
    # Incrementing each time a stop for a route is seen
    for item in route_stops_data_dict:
        if 'Red' in item['attributes']['description']:
            total_route_stop_dict['Red Line'] += 1
            print(total_route_stop_dict)
        if 'Mattapan' in item['attributes']['description']:
            total_route_stop_dict['Mattapan Trolley'] += 1
        if 'Orange' in item['attributes']['description']:
            total_route_stop_dict['Orange Line'] += 1
        if '(B)' in item['attributes']['description']:
            total_route_stop_dict['Green Line (B)'] += 1
        if '(C)' in item['attributes']['description']:
            total_route_stop_dict['Green Line (C)'] += 1
        if '(D)' in item['attributes']['description']:
            total_route_stop_dict['Green Line (D)'] += 1
        if '(E)' in item['attributes']['description']:
            total_route_stop_dict['Green Line (E)'] += 1
        if 'Blue' in item['attributes']['description']:
            total_route_stop_dict['Blue Line'] += 1

    # Sorting the stop names by number of stops
    sorted_total_route_stop_dict = sorted(total_route_stop_dict, key=lambda i: int(total_route_stop_dict[i]))

    most_stops = sorted_total_route_stop_dict[-1]
    least_stops = sorted_total_route_stop_dict[0]
    print("Subway route with the most stops: {}".format(most_stops))
    print("Subway route with the least number of stops: {}".format(least_stops))

def subway_route_calculator():
    """Access MBTA API to find subway routes to bes"""
    route_stops = requests.get('https://api-v3.mbta.com/stops?filter[route_type]=0,1&include=route,parent_station')
    route_stops_json_format = route_stops.json()
    route_stops_data_dict = route_stops_json_format['data']

    first_stop = input("Enter your first stop: ")
    #second_stop = input("Please enter your second stop: ")

    for item in route_stops_data_dict:
        if first_stop in item['attributes']['description']:
            result = [re.search('- (.*) -', item['attributes']['description']).group(1)]
            # route_marker = "- (.*?) -"
            #possible_routes = re.search(route_marker, item['attributes']['description']).group(1)
            print([item[0] for item in result])


k = subway_route_calculator()