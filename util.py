from tube_status import ApiDataParser
import json

class StationGetter(ApiDataParser):
    """ Gets a list of stations for an underground line from the api.
        This can be used as a somewhat unreliable starting point to get all stations in the system
    """

    def get_stations(self, lines, as_json=False):
        stations = {}
        for line in lines:
            if not line.api_code:
                continue

            prediction_url = 'http://cloud.tfl.gov.uk/TrackerNet/PredictionSummary/%s' % line.api_code
            raw_xml = self.get(prediction_url)
            tree = self.create_tree(raw_xml)

            station_nodes = tree.findall('S')
            for station_node in station_nodes:
                stations[station_node.get('Code')] = station_node.get('N')[:-1]

        stations = [{'api_code':key, 'name':value} for key, value in stations.items()]

        return json.dumps(stations) if as_json else stations