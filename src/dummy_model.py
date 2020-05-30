from model import *
from random import random
class DummyModel:
    def __init__(self):
        self.amea: AMEA = AMEA()
        self.issues_under_construction = IssuesUnderConstruction()
        self.pending_issues = PendingIssues()
        self.access_map: AccessMap = AccessMap()
        self.report_issue: ReportIssue = None

        self.access_map.add_location(generate_location(LocationType.Obstacle))
        self.access_map.add_location(generate_location(LocationType.Obstacle))
        self.access_map.add_location(generate_location(LocationType.Obstacle))
        self.access_map.add_location(generate_location(LocationType.Parking))
        self.access_map.add_location(generate_location(LocationType.Parking))
        self.access_map.add_location(generate_location(LocationType.Parking))
        self.access_map.add_location(generate_location(LocationType.Toilet))
        self.access_map.add_location(generate_location(LocationType.Toilet))
        self.access_map.add_location(generate_location(LocationType.Toilet))

def generate_location(location_type: LocationType):
    return Location((38.245982 + random()/100, 21.739000 + random()/100), location_type)