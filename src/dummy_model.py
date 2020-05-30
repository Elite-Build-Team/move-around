from model import *

class DummyModel:
    def __init__(self):
        self.amea: AMEA = AMEA()
        self.issues_under_construction = IssuesUnderConstruction()
        self.pending_issues = PendingIssues()
        self.access_map: AccessMap = AccessMap()
        
        self.access_map.add_location(Location((38.245982, 21.735388), LocationType.Obstacle))
        self.access_map.add_location(Location((38.245982, 21.735100), LocationType.Toilet))
        self.access_map.add_location(Location((38.245982, 21.735000), LocationType.Parking))
        self.access_map.add_location(Location((38.245982, 21.731388), LocationType.Obstacle))
        self.access_map.add_location(Location((38.245982, 21.732100), LocationType.Toilet))
        self.access_map.add_location(Location((38.245982, 21.733000), LocationType.Parking))
        self.access_map.add_location(Location((38.245982, 21.735388), LocationType.Obstacle))
        self.access_map.add_location(Location((38.245982, 21.738100), LocationType.Toilet))
        self.access_map.add_location(Location((38.245982, 21.739000), LocationType.Parking))
