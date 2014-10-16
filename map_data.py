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

raw_data = load_map_data()
lines = process_lines(raw_data)

}