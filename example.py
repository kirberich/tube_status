test_data = """<?xml version="1.0" encoding="utf-8"?>
<ArrayOfLineStatus xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns="http://webservices.lul.co.uk/">
  <LineStatus ID="0" StatusDetails="">
    <BranchDisruptions />
    <Line ID="1" Name="Bakerloo" />
    <Status ID="GS" CssClass="GoodService" Description="Good Service" IsActive="true">
      <StatusType ID="1" Description="Line" />
    </Status>
  </LineStatus>
  <LineStatus ID="1" StatusDetails="">
    <BranchDisruptions />
    <Line ID="2" Name="Central" />
    <Status ID="GS" CssClass="GoodService" Description="Good Service" IsActive="true">
      <StatusType ID="1" Description="Line" />
    </Status>
  </LineStatus>
  <LineStatus ID="10" StatusDetails="">
    <BranchDisruptions />
    <Line ID="7" Name="Circle" />
    <Status ID="GS" CssClass="GoodService" Description="Good Service" IsActive="true">
      <StatusType ID="1" Description="Line" />
    </Status>
  </LineStatus>
  <LineStatus ID="2" StatusDetails="">
    <BranchDisruptions />
    <Line ID="9" Name="District" />
    <Status ID="GS" CssClass="GoodService" Description="Good Service" IsActive="true">
      <StatusType ID="1" Description="Line" />
    </Status>
  </LineStatus>
  <LineStatus ID="8" StatusDetails="">
    <BranchDisruptions />
    <Line ID="8" Name="Hammersmith and City" />
    <Status ID="GS" CssClass="GoodService" Description="Good Service" IsActive="true">
      <StatusType ID="1" Description="Line" />
    </Status>
  </LineStatus>
  <LineStatus ID="4" StatusDetails="">
    <BranchDisruptions />
    <Line ID="4" Name="Jubilee" />
    <Status ID="GS" CssClass="GoodService" Description="Good Service" IsActive="true">
      <StatusType ID="1" Description="Line" />
    </Status>
  </LineStatus>
  <LineStatus ID="9" StatusDetails="Minor Delays between Harrow-on-the-Hill and Watford southbound only while we fix a signal failure at Northwood Hills. A Good Service is operating on the rest of the line.">
    <BranchDisruptions>
      <BranchDisruption>
        <StationTo ID="253" Name="Watford" />
        <StationFrom ID="101" Name="Harrow-on-the-Hill" />
        <Status ID="MD" CssClass="GoodService" Description="Minor Delays" IsActive="true">
          <StatusType ID="1" Description="Line" />
        </Status>
      </BranchDisruption>
    </BranchDisruptions>
    <Line ID="11" Name="Metropolitan" />
    <Status ID="MD" CssClass="GoodService" Description="Minor Delays" IsActive="true">
      <StatusType ID="1" Description="Line" />
    </Status>
  </LineStatus>
  <LineStatus ID="5" StatusDetails="">
    <BranchDisruptions />
    <Line ID="5" Name="Northern" />
    <Status ID="GS" CssClass="GoodService" Description="Good Service" IsActive="true">
      <StatusType ID="1" Description="Line" />
    </Status>
  </LineStatus>
  <LineStatus ID="6" StatusDetails="">
    <BranchDisruptions />
    <Line ID="6" Name="Piccadilly" />
    <Status ID="GS" CssClass="GoodService" Description="Good Service" IsActive="true">
      <StatusType ID="1" Description="Line" />
    </Status>
  </LineStatus>
  <LineStatus ID="7" StatusDetails="">
    <BranchDisruptions />
    <Line ID="3" Name="Victoria" />
    <Status ID="GS" CssClass="GoodService" Description="Good Service" IsActive="true">
      <StatusType ID="1" Description="Line" />
    </Status>
  </LineStatus>
  <LineStatus ID="11" StatusDetails="">
    <BranchDisruptions />
    <Line ID="12" Name="Waterloo and City" />
    <Status ID="GS" CssClass="GoodService" Description="Good Service" IsActive="true">
      <StatusType ID="1" Description="Line" />
    </Status>
  </LineStatus>
  <LineStatus ID="82" StatusDetails="">
    <BranchDisruptions />
    <Line ID="82" Name="Overground" />
    <Status ID="GS" CssClass="GoodService" Description="Good Service" IsActive="true">
      <StatusType ID="1" Description="Line" />
    </Status>
  </LineStatus>
  <LineStatus ID="81" StatusDetails="">
    <BranchDisruptions />
    <Line ID="81" Name="DLR" />
    <Status ID="GS" CssClass="GoodService" Description="Good Service" IsActive="true">
      <StatusType ID="1" Description="Line" />
    </Status>
  </LineStatus>
</ArrayOfLineStatus>
"""

# from tube_status import TubeStatus
# status = TubeStatus(raw_xml=test_data)
# import ipdb
# ipdb.set_trace()

from util import StationGetter
from map_data import lines 

getter = StationGetter()
stations = getter.get_stations(lines.values())
import ipdb
ipdb.set_trace()