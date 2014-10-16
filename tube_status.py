import urllib2
from datetime import datetime
from lxml import etree
from pprint import pprint

from map_data import lines

STATUS_CODES = {
    'GS': 'Good Service',
    'MD': 'Minor Delays',
    'SD': 'Severe Delays',
    # There's more, but I haven't been able to find the codes yet
}


class ApiDataParser(object):
    def get(self, url):
        """ Get content from api and return it as a raw string """
        stream = urllib2.urlopen(url)
        raw_xml = stream.read()
        stream.close()
        return raw_xml

    def create_tree(self, raw_xml):
        """ Creates tree from raw data and removes namespaces from tags """
        tree = etree.fromstring(raw_xml)

        # I'm sure this isn't the right way to get rid of xml namespaces, right? Right?!
        for elem in tree.getiterator():
            if not hasattr(elem.tag, 'find'): 
                continue
            i = elem.tag.find('}')
            if i >= 0:
                elem.tag = elem.tag[i+1:]
        return tree

class TubeStatus(ApiDataParser):
    def __init__(self, raw_xml=None):
        self.url = 'http://cloud.tfl.gov.uk/TrackerNet/LineStatus'
        self.raw_xml = raw_xml
        self.keep_raw = raw_xml != None

        self.update()

    def update(self):
        if not self.keep_raw:
            self.raw_xml = self.get(self.url)

        self.tree = self.create_tree(self.raw_xml)
        self.parse_tree()

        self.last_update = datetime.now()

    def parse_tree(self):
        """ Parse self.tree into easily-accessible status data in self.status and self.disruptions """

        line_nodes = self.tree.getchildren()
         
        self.status = {}
        self.disruptions = {}
        for node in line_nodes:
            line = lines[node.find('Line').get('Name')]

            disruptions = node.find('BranchDisruptions').getchildren()

            status = node.find('Status')
            self.status[line] = {
                'status_code': status.get('ID'),
                'status': STATUS_CODES.get(status.get('ID'), ''),
                'description': status.get('Description')
            }

            for disruption in disruptions:
                status = disruption.find('Status')
                self.disruptions.setdefault(line, []).append({
                    'from': disruption.find('StationFrom').get('Name'),
                    'to': disruption.find('StationTo').get('Name'),
                    'status_code': status.get('ID'),
                    'status': STATUS_CODES.get(status.get('ID'), ''),
                    'description': status.get('Description')
                })

    def all_lines(self):
        return self.status.keys()

    def lines_with_disruptions(self):
        return self.disruptions.keys()

    def good_lines(self):
        return [line for line in self.all_lines() if line not in self.lines_with_disruptions()]