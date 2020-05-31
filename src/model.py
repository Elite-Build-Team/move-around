# -*- coding: UTF-8 -*-
from enum import Enum
from typing import List, Tuple

from datetime import datetime

class User(object):
    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def get_surname(self) -> str:
        return self.__surname

    def set_surname(self, surname: str):
        self.__surname = surname

    def get_email(self) -> str:
        return self.__email

    def set_email(self, email: str):
        self.__email = email

    def __init__(self):
        self.__name: str = ''
        self.__surname: str = ''
        self.__email: str = ''


class AccessMap(object):
    def get_locations(self) -> List['Location']:
        return self.__locations

    def set_locations(self, locations: List['Location']):
        self.__locations = locations

    def get_obstacles(self) -> List['Location']:
        return [location for location in self.__locations if location.get_type() == LocationType.Obstacle]

    def get_toilets(self) -> List['Location']:
        return [location for location in self.__locations if location.get_type() == LocationType.Toilet]

    def get_parkings(self) -> List['Location']:
        return [location for location in self.__locations if location.get_type() == LocationType.Parking]

    def get_locations_by_type(self, location_type: 'LocationType') -> List['Location']:
        return [location for location in self.__locations if location.get_type() == location_type]

    def add_location(self, location: 'Location'):
        self.__locations.append(location)

    def delete_location(self, location: 'Location'):
        self.__locations.remove(location)

    def get_access_map(self) -> List['Location']:
        return self.__locations

    def __init__(self):
        self.__locations: List['Location'] = []


class AFP(object):
    def get_location(self) -> 'Location':
        return self.__location

    def set_location(self, location: 'Location'):
        self.__location = location

    def get_reviews(self) -> List['Review']:
        return self.__reviews

    def set_reviews(self, reviews: List['Review']):
        self.__reviews = reviews

    def add_review(self, review: 'Review'):
        self.__reviews.append(review)

    def delete_review(self, review: 'Review'):
        self.__reviews.remove(review)

    def get_afp_details(self) -> Tuple['Location', List['Review']]:
        return self.__location, self.__reviews

    def like_afp(self):
        raise NotImplementedError

    def __init__(self):
        self.__location: 'Location' = Location
        self.__reviews: List['Review'] = []


class AFPSuggestions(object):
    def get_afp_suggestions(self) -> List['AFP']:
        return self.__afp_suggestions

    def set_afp_suggestions(self, afp_suggestions: List['AFP']):
        self.__afp_suggestions = afp_suggestions

    def add_suggestion(self, suggestion: 'AFP'):
        self.__afp_suggestions.append(suggestion)

    def delete_suggestion(self, suggestion: 'AFP'):
        self.__afp_suggestions.remove(suggestion)

    def __init__(self):
        self.__afp_suggestions: List['AFP'] = []


class AMEA(User):
    def get_current_location(self) -> 'Location':
        return self.__current_location

    def set_current_location(self, current_location: 'Location'):
        self.__current_location = current_location

    def get_liked_afp(self) -> List['AFP']:
        return self.__liked_afp

    def set_liked_afp(self, liked_afp: List['AFP']):
        self.__liked_afp = liked_afp

    def get_reported_issues(self) -> List['ReportIssue']:
        return self.__reported_issues

    def set_reported_issues(self, reported_issues: List['ReportIssue']):
        self.__reported_issues = reported_issues

    def add_report_issue(self, report_issue: 'ReportIssue'):
        self.__reported_issues.append(report_issue)

    def delete_report_issue(self, report_issue: 'ReportIssue'):
        self.__reported_issues.delete(report_issue)

    def add_liked_afp(self, afp: 'AFP'):
        self.__liked_afp.append(afp)

    def delete_liked_afp(self, afp):
        self.__liked_afp.delete(afp)

    def add_to_taxi_bookings(self, taxi_booking: 'TaxiBooking'):
        self.__taxi_bookings.append(taxi_booking)

    def get_taxi_bookings(self) -> List['TaxiBooking']:
        return self.__taxi_bookings

    def set_taxi_bookings(self, taxi_bookings: List['TaxiBooking']):
        self.__taxi_bookings = taxi_bookings

    def get_created_afp(self) -> List['AFP']:
        return self.__created_afp

    def set_created_afp(self, created_afp: 'AFP'):
        self.__created_afp = created_afp

    def delete_created_afp(self, afp: 'AFP'):
        self.__created_afp.delete(afp)

    def __init__(self):
        self.__current_location: 'Location' = None
        self.__liked_afp: List['AFP'] = []
        self.__reported_issues: List['ReportIssue'] = []
        self.__taxi_bookings: List['TaxiBooking'] = []
        self.__created_afp: List['AFP'] = []
        # self.__id: int = itertools.count().next #TO CHECK


class Citizen(User):
    def get_reported_issues(self) -> List['ReportIssue']:
        return self.__reported_issues

    def set_reported_issues(self, reported_issues: List['ReportIssue']):
        self.__reported_issues = reported_issues

    def add_report_issue(self, report_issue: 'ReportIssue'):
        self.__reported_issues.append(report_issue)

    def delete_report_issue(self, report_issue: 'ReportIssue'):
        self.__reported_issues.remove(report_issue)

    def __init__(self):
        self.__reported_issues: List['ReportIssue'] = []


class IssuesUnderConstruction(object):
    def get_service_info(self) -> 'ServiceInfo':
        return self.__service_info

    def set_service_info(self, service_info: 'ServiceInfo'):
        self.__service_info = service_info

    def get_report_issues(self) -> List['ReportIssue']:
        return self.__report_issues

    def set_report_issues(self, report_issues: List['ReportIssue']):
        self.__report_issues = report_issues

    def add_issue_under_construction(self, issue_under_consturction: 'ReportIssue'):
        self.__report_issues.append(issue_under_consturction)

    def delete_issue_under_construction(self, issue_under_construction: 'ReportIssue'):
        self.__report_issues.remove(issue_under_construction)

    def __init__(self):
        self.__service_info = None
        self.__report_issues = None


class LocationType(Enum):
    Obstacle = 1,
    Toilet = 2,
    Parking = 3


class Location(object):
    def get_coordinates(self) -> Tuple[float, float]:
        return self.__coordinates

    def set_coordinates(self, coordinates: Tuple[float, float]):
        self.__coordinates = coordinates

    def get_type(self):
        return self.__type

    def set_type(self, type):
        self.__type = type

    def __init__(self, coordinates: Tuple[float, float], location_type: 'LocationType'):
        self.__coordinates: Tuple[float, float] = coordinates
        self.__type = location_type


class Municipality(User):
    def get_pending_issues(self) -> 'PendingIssues':
        return self.__pending_issues

    def set_pending_issues(self, pending_issues: List['PendingIssues']):
        self.__pending_issues = pending_issues

    def get_under_construction(self) -> 'IssuesUnderConstruction':
        return self.__under_construction

    def set_under_construction(self, under_construction: 'IssuesUnderConstruction'):
        self.__under_construction = under_construction

    def get_service_catalog(self) -> List['ServiceInfo']:
        return self.__service_catalog

    def set_service_catalog(self, service_catalog: List['ServiceInfo']):
        self.__service_catalog = service_catalog

    def __init__(self):
        self.__pending_issues: PendingIssues = None
        self.__under_construction: IssuesUnderConstruction = None
        self.__service_catalog: List[ServiceInfo] = []


class PendingIssues(object):
    def get_pending_issues(self) -> List['ReportIssue']:
        return self.__pending_issues

    def set_pending_issues(self, pending_issues: List['ReportIssue']):
        self.__pending_issues = pending_issues

    def add_pending_issue(self, pending_issue: 'ReportIssue'):
        self.__pending_issues.append(pending_issue)

    def delete_pending_issue(self, pending_issue: 'ReportIssue'):
        self.__pending_issues.remove(pending_issue)

    def get_issue_details(self):
        # TODO
        return self.__issue_details

    def __init__(self):
        self.__pending_issues: List['ReportIssue'] = []


class Photograph(object):
    def __init__(self):
        self.__pixels = None


class PublicServiceWorker(User):
    def get_meetings(self) -> List['ScheduledMeeting']:
        return self.__meetings

    def set_meetings(self, meetings: List['ScheduledMeeting']):
        self.__meetings = meetings

    def get_public_service_name(self) -> str:
        return self.__public_service_name

    def set_public_service_name(self, public_service_name: str):
        self.__public_service_name = public_service_name

    def get_reported_issues(self) -> List['ReportIssue']:
        return self.__reported_issues

    def set_reported_issues(self, reported_issues: List['ReportIssue']):
        self.__reported_issues = reported_issues

    def add_report_issue(self, report_issue: 'ReportIssue'):
        self.__reported_issues.append(report_issue)

    def delete_report_issue(self, report_issue: 'ReportIssue'):
        self.__reported_issues.remove(report_issue)

    def delete_meeting(self, meeting: 'ScheduledMeeting'):
        self.__meetings.remove(meeting)

    def add_meeting(self, meeting: 'ScheduledMeeting'):
        self.__meetings.append(meeting)


class ReportIssue(object):
    def get_photograph(self) -> 'Photograph':
        return self.__photograph

    def set_photograph(self, photograph: 'Photograph'):
        self.__photograph = photograph

    def get_location(self) -> 'Location':
        return self.__location

    def set_location(self, location: 'Location'):
        self.__location = location

    def get_summary(self) -> str:
        return self.__summary

    def set_summary(self, summary: str):
        self.__summary = summary

    def is_pending(self):
        # TODO
        raise NotImplementedError()

    def get_issue_details(self) -> Tuple['Photograph', 'Location', str]:
        return self.__photograph, self.__location, self.__summary

    def update_issue_details(self, photograph: 'Photograph', location: 'Location', summary: str):
        self.__photograph = photograph
        self.__location = location
        self.__summary = summary

    def __init__(self):
        self.__photograph: Photograph = None
        self.__location: Location = None
        self.__summary: str = ''


class ScheduledMeetingStatus(Enum):
    Pending = 0,
    Done = 1


class ScheduledMeeting(object):
    def get_public_service_name(self) -> str:
        return self.__public_service_name
        pass

    def set_public_service_name(self, public_service_name: str):
        self.__public_service_name = public_service_name

    def get_status(self) -> 'ScheduledMeetingStatus':
        return self.__status

    def set_status(self, status: 'ScheduledMeetingStatus'):
        self.__status = status

    def get_date_time(self) -> int:
        return self.__date_time

    def set_date_time(self, date_time: datetime):
        self.__date_time = date_time

    def get_amea_name(self) -> str:
        return self.__amea_name

    def set_amea_name(self, amea_name: str):
        self.__amea_name = amea_name

    def get_meeting_details(self) -> Tuple[datetime, str, 'ScheduledMeetingStatus', str]:
        return self.__date_time, self.__public_service_name, self.__status, self.__amea_name

    def update_meeting_details(self, date_time: datetime, public_service_name: str, status: 'ScheduledMeetingStatus',
                               amea_name: str):
        self.__date_time = date_time
        self.__public_service_name = public_service_name
        self.__status = status
        self.__amea_name = amea_name

    def __init__(self):
        self.__date_time: datetime = None
        self.__public_service_name: str = ''
        self.__status: 'ScheduledMeetingStatus' = ScheduledMeetingStatus.Pending
        self.__amea_name: str = ''


class ServiceInfo(object):
    def get_phone(self) -> str:
        return self.__phone

    def set_phone(self, phone: str):
        if len(phone) == 10:
            self.__phone = phone
        else:
            raise Exception('Phone number must be 10 digits long')

    def get_name(self) -> str:
        return self.__name

    def set_name(self, name: str):
        self.__name = name

    def __init__(self):
        self.__phone: str = ''
        self.__name: str = ''


class TaxiBooking(object):
    def get_amea(self):
        pass

    def set_amea(self, amea: 'AMEA'):
        pass

    def get_location(self):
        pass

    def set_location(self, location: 'Location'):
        pass

    def set_date_time(self, date_time: datetime):
        self.__date_time = date_time

    def get_date_time(self) -> datetime:
        return self.__date_time

    def __init__(self):
        self.__date_time: datetime = None
        self.__amea: 'AMEA' = None
        self.__location: 'Location' = None
