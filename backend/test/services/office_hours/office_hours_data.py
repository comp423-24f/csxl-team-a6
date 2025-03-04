"""Test Data for Office Hours."""

import pytest
from datetime import datetime, timedelta
import pytz
from sqlalchemy.orm import Session
from ...services.reset_table_id_seq import reset_table_id_seq

from ....test.services import user_data, room_data
from ..academics import section_data
from ..academics import term_data

from ....entities.office_hours import user_created_tickets_table
from ....entities.office_hours.office_hours_entity import OfficeHoursEntity
from ....entities.office_hours.course_site_entity import CourseSiteEntity
from ....entities.office_hours.ticket_entity import OfficeHoursTicketEntity
from ....entities.academics.section_entity import SectionEntity


from ....models.office_hours.office_hours import OfficeHours, NewOfficeHours
from ....models.office_hours.event_type import (
    OfficeHoursEventModeType,
    OfficeHoursEventType,
)
from ....models.office_hours.course_site import (
    CourseSite,
    NewCourseSite,
    UpdatedCourseSite,
)
from ....models.office_hours.ticket import OfficeHoursTicket, NewOfficeHoursTicket
from ....models.office_hours.ticket_type import TicketType
from ....models.office_hours.ticket_state import TicketState

__authors__ = [
    "Ajay Gandecha",
    "Madelyn Andrews",
    "Sadie Amato",
    "Bailey DeSouza",
    "Meghan Sun",
]
__copyright__ = "Copyright 2024"
__license__ = "MIT"

# Course Site Data

# COMP 110:

# Site
comp_110_site = CourseSite(id=1, title="COMP 110", term_id=term_data.current_term.id)
comp_301_site = CourseSite(id=2, title="COMP 301", term_id=term_data.current_term.id)

# Sections
comp_110_sections = (
    [
        section_data.comp_110_001_current_term,
        section_data.comp_110_002_current_term,
    ],
    comp_110_site.id,
)
comp_301_sections = (
    [section_data.comp_301_001_current_term],
    comp_301_site.id,
)


# Setting the correct timezone - Python's datetime library gets the timezone from the system's
# internal data, but in the cloudapp, datetime cannot find the timezone info so it defaults
# to UTC standard time. Using pytz, we are able to make an instance of tzinfo that can be
# passed into datetime.now() to return the current date & time in the east coast time zone
# which automatically accounts for daylight savings

chapel_hill_timezone = pytz.timezone("America/New_York")

# Office Hours
comp_110_current_office_hours = OfficeHours(
    id=1,
    rsvp=0,
    type=OfficeHoursEventType.OFFICE_HOURS,
    hosts="Kris Jordan and the team",
    mode=OfficeHoursEventModeType.IN_PERSON,
    description="Current CAMP 110 office hours",
    location_description="In the downstairs closet : )",
    start_time=datetime.now(chapel_hill_timezone) - timedelta(hours=2),
    end_time=datetime.now(chapel_hill_timezone) + timedelta(hours=1),
    course_site_id=comp_110_site.id,
    room_id=room_data.group_a.id,
)
comp_110_future_office_hours = OfficeHours(
    id=2,
    rsvp=0,
    type=OfficeHoursEventType.OFFICE_HOURS,
    hosts="Kris Jordan and the team",
    mode=OfficeHoursEventModeType.IN_PERSON,
    description="Future CAMP 110 office hours",
    location_description="In the downstairs closet : )",
    start_time=datetime.now(chapel_hill_timezone) + timedelta(days=1),
    end_time=datetime.now(chapel_hill_timezone) + timedelta(days=1, hours=3),
    course_site_id=comp_110_site.id,
    room_id=room_data.group_a.id,
)
comp_110_past_office_hours = OfficeHours(
    id=3,
    rsvp=0,
    type=OfficeHoursEventType.OFFICE_HOURS,
    hosts="Kris Jordan and the team",
    mode=OfficeHoursEventModeType.IN_PERSON,
    description="Past CAMP 110 office hours",
    location_description="In the downstairs closet : )",
    start_time=datetime.now(chapel_hill_timezone) - timedelta(days=1, hours=3),
    end_time=datetime.now(chapel_hill_timezone) - timedelta(days=1),
    course_site_id=comp_110_site.id,
    room_id=room_data.group_a.id,
)

# Tickets
comp_110_queued_ticket = OfficeHoursTicket(
    id=1,
    description="My Docker container is crashing!! Pls help me I beg you..",
    type=TicketType.ASSIGNMENT_HELP,
    state=TicketState.QUEUED,
    created_at=datetime.now(chapel_hill_timezone),
    called_at=None,
    closed_at=None,
    have_concerns=False,
    caller_notes="",
    office_hours_id=comp_110_current_office_hours.id,
    caller_id=None,
)
comp_110_cancelled_ticket = OfficeHoursTicket(
    id=2,
    description="I don't need help, but I want to visit my friend.",
    type=TicketType.CONCEPTUAL_HELP,
    state=TicketState.CANCELED,
    created_at=datetime.now(chapel_hill_timezone),
    called_at=None,
    closed_at=None,
    have_concerns=False,
    caller_notes="",
    office_hours_id=comp_110_current_office_hours.id,
    caller_id=None,
)
comp_110_called_ticket = OfficeHoursTicket(
    id=3,
    description="I do not know how to exit vim. Do I need to burn my PC?",
    type=TicketType.ASSIGNMENT_HELP,
    state=TicketState.CALLED,
    created_at=datetime.now(chapel_hill_timezone) - timedelta(minutes=1),
    called_at=datetime.now(chapel_hill_timezone),
    closed_at=None,
    have_concerns=False,
    caller_notes="",
    office_hours_id=comp_110_current_office_hours.id,
    caller_id=section_data.comp110_instructor.id,
)
comp_110_closed_ticket = OfficeHoursTicket(
    id=4,
    description="How do I turn on my computer?",
    type=TicketType.CONCEPTUAL_HELP,
    state=TicketState.CLOSED,
    created_at=datetime.now(chapel_hill_timezone) - timedelta(minutes=2),
    called_at=datetime.now(chapel_hill_timezone) - timedelta(minutes=1),
    closed_at=datetime.now(chapel_hill_timezone),
    have_concerns=True,
    caller_notes="Student could not find the power button on their laptop.",
    office_hours_id=comp_110_current_office_hours.id,
    caller_id=section_data.comp110_instructor.id,
)
comp_110_ticket_creators = [
    (comp_110_queued_ticket, [section_data.comp110_student_1.id]),
    (comp_110_cancelled_ticket, [section_data.comp110_student_1.id]),
    (comp_110_called_ticket, [section_data.comp110_student_1.id]),
    (comp_110_closed_ticket, [section_data.comp110_student_1.id]),
]


# Data objects for testing purposes
new_ticket = NewOfficeHoursTicket(
    description="Help me!",
    type=TicketType.ASSIGNMENT_HELP,
    office_hours_id=comp_110_current_office_hours.id,
)

new_course_site = NewCourseSite(
    title="Ina's COMP 301",
    term_id=term_data.current_term.id,
    section_ids=[
        section_data.comp_301_002_current_term.id,
    ],
)

new_course_site_term_mismatch = NewCourseSite(
    title="Ina's COMP 301",
    term_id=term_data.f_23.id,
    section_ids=[
        section_data.comp_301_002_current_term.id,
    ],
)


new_course_site_term_nonmember = NewCourseSite(
    title="Ina's COMP 3x1",
    term_id=term_data.current_term.id,
    section_ids=[
        section_data.comp_301_002_current_term.id,
        section_data.comp_311_001_current_term.id,
    ],
)
new_course_site_term_noninstructor = NewCourseSite(
    title="Ina's COMP 3x1",
    term_id=term_data.current_term.id,
    section_ids=[
        section_data.comp_301_002_current_term.id,
        section_data.comp_311_002_current_term.id,
    ],
)


new_course_site_term_already_in_site = NewCourseSite(
    title="Ina's COMP courses",
    term_id=term_data.current_term.id,
    section_ids=[
        section_data.comp_301_002_current_term.id,
        section_data.comp_110_001_current_term.id,
    ],
)

updated_comp_110_site = UpdatedCourseSite(
    id=1,
    title="New Course Site",
    term_id=term_data.current_term.id,
    section_ids=[section_data.comp_110_001_current_term.id],
    utas=[],
    gtas=[],
)

updated_comp_110_site_term_mismatch = UpdatedCourseSite(
    id=1,
    title="New Course Site",
    term_id=term_data.current_term.id,
    section_ids=[
        section_data.comp_110_001_current_term.id,
        section_data.comp_101_001.id,
    ],
    utas=[],
    gtas=[],
)

updated_course_site_term_nonmember = UpdatedCourseSite(
    id=1,
    title="New Course Site",
    term_id=term_data.current_term.id,
    section_ids=[
        section_data.comp_110_001_current_term.id,
        section_data.comp_311_001_current_term.id,
    ],
    utas=[],
    gtas=[],
)

updated_course_does_not_exist = UpdatedCourseSite(
    id=404,
    title="New Course Site",
    term_id=term_data.current_term.id,
    section_ids=[
        section_data.comp_110_001_current_term.id,
        section_data.comp_311_002_current_term.id,
    ],
    utas=[],
    gtas=[],
)

updated_course_site_term_noninstructor = UpdatedCourseSite(
    id=1,
    title="New Course Site",
    term_id=term_data.current_term.id,
    section_ids=[
        section_data.comp_311_001_current_term.id,
        section_data.comp_311_002_current_term.id,
    ],
    utas=[],
    gtas=[],
)

updated_course_site_term_already_in_site = UpdatedCourseSite(
    id=1,
    title="New Course Site",
    term_id=term_data.current_term.id,
    section_ids=[
        section_data.comp_301_001_current_term.id,
        section_data.comp_110_001_current_term.id,
    ],
    utas=[],
    gtas=[],
)

new_site_other_user = NewCourseSite(
    title="Rhonda",
    term_id=term_data.current_term.id,
    section_ids=[section_data.comp_311_001_current_term.id],
)

new_event = NewOfficeHours(
    id=12,
    type=OfficeHoursEventType.OFFICE_HOURS,
    rsvp=1,
    hosts="Sample hosts (new_event)",
    mode=OfficeHoursEventModeType.IN_PERSON,
    description="Sample",
    location_description="Sample",
    start_time=datetime.now(chapel_hill_timezone),
    end_time=datetime.now(chapel_hill_timezone),
    course_site_id=comp_110_site.id,
    room_id=room_data.group_a.id,
)

new_event_site_not_found = NewOfficeHours(
    type=OfficeHoursEventType.OFFICE_HOURS,
    rsvp=5,
    hosts="Sample hosts (not_found)",
    mode=OfficeHoursEventModeType.IN_PERSON,
    description="Sample",
    location_description="Sample",
    start_time=datetime.now(chapel_hill_timezone),
    end_time=datetime.now(chapel_hill_timezone),
    course_site_id=404,
    room_id=room_data.group_a.id,
)

updated_future_event = OfficeHours(
    id=10,
    rsvp=0,
    type=OfficeHoursEventType.REVIEW_SESSION,
    hosts="Kris Jordan and the team",
    mode=OfficeHoursEventModeType.VIRTUAL_OUR_LINK,
    description="Future CAMP 110 office hours",
    location_description="In the downstairs closet : )",
    start_time=datetime.now(chapel_hill_timezone) + timedelta(days=1),
    end_time=datetime.now(chapel_hill_timezone) + timedelta(days=1, hours=3),
    course_site_id=comp_110_site.id,
    room_id=room_data.group_a.id,
)

nonexistent_event = OfficeHours(
    id=404,
    rsvp=0,
    type=OfficeHoursEventType.OFFICE_HOURS,
    hosts="Sample hosts (nonexistent_event)",
    mode=OfficeHoursEventModeType.IN_PERSON,
    description="Sample",
    location_description="Sample",
    start_time=datetime.now(chapel_hill_timezone),
    end_time=datetime.now(chapel_hill_timezone),
    course_site_id=comp_110_site.id,
    room_id=room_data.group_a.id,
)


def days_til_input(day: int):
    """
    0 is Monday and 4 is Friday
    """
    today = datetime.now(chapel_hill_timezone)
    if day > 4 or day < 0:
        raise Exception("Future OH DEMO data can only be on weekdays.")

    # If its sat (5) and you're looking for next fri (4), this will produce 6
    days_til_day = (day - today.weekday() + 7) % 7

    # If its fri and you're looking for next fri, this makes sure to return 7
    if days_til_day == 0:
        days_til_day = 7
    return timedelta(days=days_til_day)


friday_oh = OfficeHours(
    id=5,
    rsvp=0,
    type=OfficeHoursEventType.OFFICE_HOURS,
    hosts="Mr.Fri",
    mode=OfficeHoursEventModeType.IN_PERSON,
    description="Super excellent description extreme",
    location_description="behind the building",
    start_time=datetime.now(chapel_hill_timezone).replace(hour=10)
    + days_til_input(4),  # start at 10am
    end_time=datetime.now(chapel_hill_timezone).replace(hour=12)
    + days_til_input(4),  # end at 12pm
    course_site_id=comp_110_site.id,
    room_id=room_data.group_a.id,
)

monday_oh = OfficeHours(
    id=6,
    rsvp=0,
    type=OfficeHoursEventType.OFFICE_HOURS,
    hosts="Mr.Mond",
    mode=OfficeHoursEventModeType.IN_PERSON,
    description="Super excellent description extreme",
    location_description="behind the building",
    start_time=datetime.now(chapel_hill_timezone).replace(hour=15) + days_til_input(0),
    end_time=datetime.now(chapel_hill_timezone).replace(hour=16) + days_til_input(0),
    course_site_id=comp_110_site.id,
    room_id=room_data.group_a.id,
)

tuesday_oh = OfficeHours(
    id=7,
    rsvp=0,
    type=OfficeHoursEventType.OFFICE_HOURS,
    hosts="Ms.Tues",
    mode=OfficeHoursEventModeType.IN_PERSON,
    description="Super excellent description extreme",
    location_description="behind the building",
    start_time=datetime.now(chapel_hill_timezone).replace(hour=9) + days_til_input(1),
    end_time=datetime.now(chapel_hill_timezone).replace(hour=11) + days_til_input(1),
    course_site_id=comp_110_site.id,
    room_id=room_data.group_a.id,
)

tuesday_oh_two = OfficeHours(
    id=11,
    rsvp=0,
    type=OfficeHoursEventType.OFFICE_HOURS,
    hosts="Ina Instructor",
    mode=OfficeHoursEventModeType.IN_PERSON,
    description="Super excellent description extreme",
    location_description="behind the building",
    start_time=datetime.now(chapel_hill_timezone).replace(hour=10) + days_til_input(1),
    end_time=datetime.now(chapel_hill_timezone).replace(hour=12) + days_til_input(1),
    course_site_id=comp_110_site.id,
    room_id=room_data.group_a.id,
)

wednesday_oh = OfficeHours(
    id=8,
    rsvp=0,
    type=OfficeHoursEventType.OFFICE_HOURS,
    hosts="Ms.Wed",
    mode=OfficeHoursEventModeType.IN_PERSON,
    description="Super excellent description extreme",
    location_description="behind the building",
    start_time=datetime.now(chapel_hill_timezone).replace(hour=12) + days_til_input(2),
    end_time=datetime.now(chapel_hill_timezone).replace(hour=13) + days_til_input(2),
    course_site_id=comp_110_site.id,
    room_id=room_data.group_a.id,
)

wednesday_oh_two = OfficeHours(
    id=120,
    rsvp=0,
    type=OfficeHoursEventType.OFFICE_HOURS,
    hosts="Ian Bracken",
    mode=OfficeHoursEventModeType.IN_PERSON,
    description="Super excellent description extreme",
    location_description="behind the building",
    start_time=datetime.now(chapel_hill_timezone).replace(hour=14) + days_til_input(2),
    end_time=datetime.now(chapel_hill_timezone).replace(hour=15) + days_til_input(2),
    course_site_id=comp_110_site.id,
    room_id=room_data.group_a.id,
)

thursday_oh = OfficeHours(
    id=9,
    rsvp=0,
    type=OfficeHoursEventType.OFFICE_HOURS,
    hosts="Dr.Thurs",
    mode=OfficeHoursEventModeType.IN_PERSON,
    description="Super excellent description extreme",
    location_description="behind the building",
    start_time=datetime.now(chapel_hill_timezone).replace(hour=13) + days_til_input(3),
    end_time=datetime.now(chapel_hill_timezone).replace(hour=14) + days_til_input(3),
    course_site_id=comp_110_site.id,
    room_id=room_data.group_a.id,
)


# All
sites = [comp_110_site, comp_301_site]
section_pairings = [comp_110_sections, comp_301_sections]

office_hours = [
    comp_110_current_office_hours,
    comp_110_future_office_hours,
    comp_110_past_office_hours,
    updated_future_event,
    friday_oh,
    monday_oh,
    tuesday_oh,
    tuesday_oh_two,
    wednesday_oh,
    wednesday_oh_two,
    thursday_oh,
]

oh_tickets = [
    comp_110_queued_ticket,
    comp_110_cancelled_ticket,
    comp_110_called_ticket,
    comp_110_closed_ticket,
]
ticket_user_pairings = [comp_110_ticket_creators]


def insert_fake_data(session: Session):

    # Step 1: Add sites to database

    for site in sites:
        entity = CourseSiteEntity.from_model(site)
        session.add(entity)

    reset_table_id_seq(
        session,
        CourseSiteEntity,
        CourseSiteEntity.id,
        len(sites) + 1,
    )

    session.commit()

    # Step 2: Add sections to course sites
    for sections, site_id in section_pairings:
        for section in sections:
            section_entity = session.get(SectionEntity, section.id)
            section_entity.course_site_id = site_id

    session.commit()

    # Step 3: Add office hours to database

    for oh in office_hours:
        office_hours_entity = OfficeHoursEntity.from_model(oh)
        session.add(office_hours_entity)

    reset_table_id_seq(
        session,
        OfficeHoursEntity,
        OfficeHoursEntity.id,
        len(office_hours) + 1,
    )

    session.commit()

    # Step 4: Add tickets to database

    for ticket in oh_tickets:
        ticket_entity = OfficeHoursTicketEntity.from_model(ticket)
        session.add(ticket_entity)

    reset_table_id_seq(
        session,
        OfficeHoursTicketEntity,
        OfficeHoursTicketEntity.id,
        len(oh_tickets) + 1,
    )

    session.commit()

    # Step 5: Add users as ticket creators
    for pairing in ticket_user_pairings:
        for ticket, user_ids in pairing:
            for user_id in user_ids:
                session.execute(
                    user_created_tickets_table.insert().values(
                        {
                            "ticket_id": ticket.id,
                            "member_id": user_id,
                        }
                    )
                )

    session.commit()


@pytest.fixture(autouse=True)
def fake_data_fixture(session: Session):
    insert_fake_data(session)
    session.commit()
    yield
