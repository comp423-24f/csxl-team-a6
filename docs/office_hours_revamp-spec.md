# **Technical Specification: Office Hours Visibility Revamp**

### 1. Descriptions and sample data (models and API routes)

- Pydantic model for an office hour event that includes the hosts input from the office hours editor form
- This allows for office hour calendar instances to include information on who is hosting the event

```
export interface OfficeHourEventOverview {
  id: number;
  hosts: string;
  type: string;
  mode: string;
  description: string;
  location: string;
  location_description: string;
  start_time: Date;
  end_time: Date;
  queued: number;
  total_tickets: number;
}
```

### 2. Descriptions of database/entity changes

- The new column for hosts in the office hour event SQLAlchemy entity:

```
    hosts: Mapped[str] = mapped_column(String, default="", nullable=False)
```

- After adding this column to the entity, we add the "hosts" field in all the functions and other parts of the codebase relying on this entity
  - This change required deleting the database, re-creating the database, and adding back the demo data to the database
  - We did not want a default value as hosts should be specific to the requirements of whoever is creating the office hours.

### 3. Technical & UX design choices

#### Technical design choice:

- We decided to turn each office hour event into a widget. Initially, we built it directly into the page component, so it took some effort to move the code into a separate widget. However, we determined that this was necessary to improve readability and replicability, which will save us time in the long run since we intend to use these event widgets repeatedly.

#### User experience design choice:

- To determine the host's name being displayed on the office hours event cards, we were between pulling the user's name from their sign-in info or adding a "Hosts" field to the office hours event editor form
  - We decided that adding "Hosts" as an optional field to the form would allow for more flexibility
    - This includes not displaying one's name, having multiple TAs or guest instructors in a session, and potentially adding more identifying personal information to the "hosts" section of the card
- For the calendar design, we had to determine the most visually appealing way to display future events. We debated whether to display a single day of office hours, a week at a time, two weeks at a time, or a month at a time. Ultimately, we decided that showing a single week at a time with a drop-down menu allowing users to select future weeks would be ideal. This approach strikes the perfect balance between clear visibility of events and easy access to those further in the future.

### 4. Descriptions of database/entity changes

- Navigating the effects of creating a new office hours event through the stack is important to understanding our feature.
  - Below you can find a picture of the general idea of the stack flow (made by Ajay Gandecha) and a rough sketch of the files involved along the way
  - There is also a typed description on the project board of the project's stack flow, which includes some other involved files
    - This is purposely a draft so that anyone on the team can add new discoveries and explanations
  - Note that there are several files other files that are involved in a minor way, so use **right-click + Go to Declaration** to see where a function or type is declared
  - If a new developer were to want to reuse and modify our calendar/OH event features, the most important files are found in the following directories:
    - frontend/src/app/my-courses/course/office-hours/office-hours-page/
    - frontend/src/app/my-courses/widgets/office-hours-event-card/
      <!-- <img src="https://private-user-images.githubusercontent.com/111540555/386875741-4e5bea91-92d8-449b-aa33-8b86c1fb5141.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MzE3ODkxMDgsIm5iZiI6MTczMTc4ODgwOCwicGF0aCI6Ii8xMTE1NDA1NTUvMzg2ODc1NzQxLTRlNWJlYTkxLTkyZDgtNDQ5Yi1hYTMzLThiODZjMWZiNTE0MS5wbmc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjQxMTE2JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI0MTExNlQyMDI2NDhaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT04MWQ4MjQ5YjY1ZjFiMTVjNDEzZTU0Zjc3ZDUyOWExMjZmZTk3OTE3ODA0OTJhMmI0NzY1ZjdjNDg1OWE0OGY2JlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCJ9.nwptzkstqLIxhjSKXalAvwNy3nKH3n-J6PKo6g_0H-Q" alt="Clean Stack Diagram"> -->
      ![Clean Stack Diagram](/docs/images/clean-stack-diagram.png)
      <p style="text-align:center;">
      <img src="/workspace/docs/images/rough-stack-diagram.jpg" alt="Rough File Stack Diagram" width="600">
      </p>

### 5. Files that caused issue populating the hosts name from database: backend/services/academics/course_site.py, backend/api/academics/my_courses.py

