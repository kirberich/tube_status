from models import Color, Line, Station
import json

# Loads map data from map_data.json and makes it available as two dictionaries
# 'lines' contains the underground lines as {'name': line_object}
# 'stations' contains the underground stations as {'name': station_object}

def load_map_data():
    with open('map_data.json') as f:
        return json.loads(f.read())

def process_lines(raw_data):
    _lines = {}
    raw_lines = raw_data['lines']
    for raw_line in raw_lines:
        line = Line(
            name=raw_line['name'],
            api_code=raw_line.get('api_code', None),
            bg_color=Color(*raw_line['bg_color']), 
            fg_color=Color(*raw_line['fg_color'])
        )
        _lines[line.name] = line
    return _lines

def process_stations(raw_data, lines):
    # First, set up the station objects
    _stations = {}
    raw_stations = raw_data['stations']
    for raw_station in raw_stations:
        station = Station(
            name=raw_station['name'],
            api_code=raw_station.get('api_code', None),
        )
        _stations[station.name] = station

    # Now, parse the connection data
    # Connections are saved as lists with two stations
    # However, for anything but the first station in a list, the first one can be skipped to save duplication.
    # In that case, the last station of the previous connection is used.
    for line_name, connections in raw_data['connections'].items():
        line = lines[line_name]
        last = None
        for connection in connections:
            if len(connection) == 2:
                start = _stations[connection[0]]
                end = _stations[connection[1]]
            else:
                if not last:
                    raise Exception("Connection %s invalid, no previous station given" % connection)

                start = last
                end = _stations[connection[0]]

            start.connections.setdefault(line, set()).add(end)
            end.connections.setdefault(line, set()).add(start)
            last = end

    return _stations


raw_data = load_map_data()
lines = process_lines(raw_data)
stations = process_stations(raw_data, lines)