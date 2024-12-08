# **Office Hours Stack Flow**

### 1. Reference Image

![Clean Stack Diagram](/docs/images/clean-stack-diagram.png)

### 2. Down the Stack

- ## frontend/src/app/my-courses/course/office-hours/office-hours-editor
  - frontend/src/app/my-courses/course/office-hours/office-hours-editor/office-hours-editor.component.html
  - frontend/src/app/my-courses/course/office-hours/office-hours-editor/office-hours-editor.component.ts
- ## frontend/src/app/my-courses/my-courses.service.ts
  - createOfficeHours(
  - post request
- ## backend/api/office_hours/office_hours.py
  - create_office_hours(
- ## backend/services/office_hours/office_hours.py
  - create(self, user: User, site_id: int, event: NewOfficeHours)
  - Entity is now committed to session and stored in th database.

### 3. Up the Stack

- ## backend/entities/office_hours/office_hours_entity.py

  - ORM file which returns an entity containg OH info

- ## backend/services/academics/course_site.py

  - \_to_oh_event_overview(
    - Converts SQLAlchemy Entity into Model

- ## backend/api/academics/my_courses.py

  - get_future_oh_events(
    - Receiving the Model data from services

- # **frontend/src/app/my-courses/my-courses.service.ts**

  - getCurrentOfficeHourEvents(
    - api/my-courses/${courseSiteId}/oh-events/current
    - This function is aligned with the above files and calls the correct API from the database
  - NOT TO BE CONFUSED WITH getOfficeHours(
    - /api/office-hours/\${siteId}/\${officeHoursId}
    - This similarly named function is called within getCurrentOfficeHourEvents( and uses backend/api/office_hours/office_hours.py and backend/services/office_hours/office_hours.py
    - ## It is a confusing layout with APIs going in different directions. This part is quite important to understand and take note of

- ## frontend/src/app/my-courses/course/office-hours/office-hours.resolver.ts

  - officeHoursResolver(
    - returns an organization to the frontend components including the new office hours

- ## frontend/src/app/my-courses/course/office-hours/office-hours-page
  - frontend/src/app/my-courses/course/office-hours/office-hours-page/office-hours-page.component.html
  - frontend/src/app/my-courses/course/office-hours/office-hours-page/office-hours-page.component.ts

# Example

- RSVP button is clicked (`future-office-hours-card.widget.html`)
  - Event emitter is activated in `future-office-hours-card.widget.ts`
- The component for the entire page handles the emit (`office-hours-page.component.html`)
  - Frontend services are called from (`office-hours-page.component.ts`)
- `my-courses.service.ts`
