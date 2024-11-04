# Office Hours Visibility Revamp

0. Title & Team

   -  Office Hours Visibility Revamp
   -  Christopher Sáez, Michael Tyndall, Ethan Byrd, Ian Bracken

1. Overview

   -  The primary goal is to create a dedicated TA-only page where teaching assistants can manage and customize their office hour schedules, including options for daily, weekly, or monthly recurring office hours. This platform will also feature a student-facing calendar, displaying the upcoming 1-2+ weeks of available office hours, from which students can reserve 20-minute time slots. To accommodate flexibility, students will have the option to cancel their bookings if needed. As a stretch goal, the calendar page could include a live queue or estimated wait times for active office hours, allowing students to plan more effectively. Additional features may involve displaying TA names on the calendar for transparency, and showing students’ names in their reserved slots so group members can coordinate and attend together.

2. Key Personas

   -  Teaching Assistants:

      -  Who they are: TAs hold office hours and assist students with coursework. They have responsibilities such as grading, class preparation, and meetings.
      -  Needs: A simplistic method to set up their recurring office hours along with a clear visual representation so students can easily view and reserve available time slots. Settings that allow clear communication of who is conducting office hours, what will go on during office hours, and special sessions such as topic summaries and review sessions that may occur throughout the semester.
      -  Goals: Efficient scheduling, Clear communication, Flexibility

   -  Students:
      -  Who they are: Students enrolled in courses who seek additional assistance outside of regular class hours. They can be undergraduates or graduate students, each with different meeting requirements and scheduling needs.
      -  Needs: An intuitive and flexible platform where they can view available office hours and reserve slots that fit their schedule.
      -  Goals: Timely Assistance, Convenience, Effective collaboration
   -  Professors:
      -  Who they are: The professor who teaches the class and sets up customization and accessibility features for TAs to better assist students.
      -  Needs: The highest level of access, viewing privileges, ability to schedule their own office hours, and customization features.
      -  Goals: Assigning TAs, changing access modifiers for students and TAs, clear communication, customizability

3. User Stories

   -  Teaching Assistants:
      -  As a TA named Teisha Aiden, I want to place my weekly office hours on the calendar repeating every week, so that at any given time all students in the class can check when my office hours will be.
      -  As a TA named Troy Accommodorre, I want to be able to change settings such as duration, displaying my name, setting a topic that will be covered during office hours, etc., so that my office hours best accommodate students.
   -  Students:
      -  As a student named Sally Studious, I want to be able to see the number of students in line before I book an office hours appointment, so that I can determine (without putting myself in the queue) if I want to wait.
      -  As a student named Sam Studybuddy, I want the option to include my name publicly when booking an office hours appointment, so that my peers know when I am getting help and can join me if they so choose.
   -  Professors:
      -  As a professor named Peter Professo, I want to be able to give TAs access to office hours scheduling capabilities, so that I can monitor/moderate office hours being conducted.
      -  As a professor named Patricia Particular, I want to be able to set restrictions on office hours, so that TAs cannot schedule office hours during university breaks, times where class occurs, and outside of the academic semester.

4. Wireframes / Mockups

   -  Landing page: add a convenient calendar for future office hours.
      -  picture
      -  ![image](../images/officeHourRevampedScreenshots/calendar.png)
      -  ![image](docs/images/officeHourRevampScreenshots/calendar.png)
   -  TA scheduling form: add new features such as repeating office hours, title, name display.
      -  pictures
   -  Office hour edit form: add new features from the initial sceduling form.

      -  picture

   -  Stretch goal: In the future we may create a wait-time estimate display, a display for students to see who else is scheduled to go to office hours, and a feature to book office hours in advance.

5. Technical Implementation Opportunities and Planning

   1. What specific areas of the existing code base will you directly depend upon, extend, or integrate with?

      -  /workspace/frontend/src/app/my-courses/course/office-hours/office-hours-editor/office-hours-editor.component.html
      -  /workspace/frontend/src/app/my-courses/course/office-hours/office-hours-page/office-hours-page.component.html
      -  /workspace/frontend/src/app/my-courses/course/office-hours/office-hours-queue/office-hours-queue.component.html
      -  /workspace/backend/api/office_hours/office_hours.py
      -  /workspace/backend/entities/office_hours/office_hours_entity.py
      -  /workspace/backend/models/office_hours/office_hours.py
      -  /workspace/backend/services/office_hours/office_hours.py
      -  /workspace/backend/test

   2. What planned page components and widgets do you anticipate needing in your feature’s frontend?

      -  /workspace/frontend/src/app/my-courses/widgets/course-card/course-card.widget.html
      -  /workspace/frontend/src/app/my-courses/course/office-hours/widgets/office-hour-event-card/office-hour-event-card.widget.html
      -  /workspace/frontend/src/app/coworking/widgets/date-selector/date-selector.widget.html

   3. What additional models, or changes to existing models, do you foresee needing (if any)?

      -  A calendar model needs to be added. This could be used in events and organizations as well in the future.
      -  Each date will have any number of time slots for Office Hours. Each time slot will have the number of reservations or “bookings” saved in it.

   4. Considering your most-frequently used and critical user stories, what API / Routes do you foresee modifying or needing to add?

      -  Existing routes for getting, updating, and setting office hours can be used. New routes/logic to add repeating office hours will need to be created.
      -  Route for getting “booked” hours for the TA’s, updating “booked” hours for students.

   5. What concerns exist for security and privacy of data? Should the capabilities you are implementing be specific to only certain users or roles? (For example: When Sally Student makes a reservation, only Sally Student or Amy Ambassador should be able to cancel the reservation. Another student, such as Sam Student, should not be able to cancel Sally’s reservation.)
      -  Students should not be able to change anything other than their office hour ticket. Authentication between roles (professor, TA, student) needs to be secure.
