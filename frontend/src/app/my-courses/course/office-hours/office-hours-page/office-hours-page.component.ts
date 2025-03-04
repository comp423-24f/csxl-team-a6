/**
 * Office hours page that shows events.
 *
 * @author Ajay Gandecha <agandecha@unc.edu>
 * @copyright 2024
 * @license MIT
 */

import { Component, OnInit, WritableSignal, signal } from '@angular/core';
import { PageEvent } from '@angular/material/paginator';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ActivatedRoute } from '@angular/router';
import {
  OfficeHourEventOverview,
  OfficeHourEventOverviewJson,
  OfficeHours,
  parseOfficeHourEventOverviewJson
} from 'src/app/my-courses/my-courses.model';
import { MyCoursesService } from 'src/app/my-courses/my-courses.service';
import {
  DEFAULT_PAGINATION_PARAMS,
  Paginated,
  PaginationParams,
  Paginator
} from 'src/app/pagination';
import { officeHoursResolver } from '../office-hours.resolver';
@Component({
  selector: 'app-course-office-hours-page',
  templateUrl: './office-hours-page.component.html',
  styleUrl: './office-hours-page.component.css'
})
export class OfficeHoursPageComponent {
  /** Route information to be used in the routing module */
  public static Route = {
    path: 'office-hours',
    title: 'Course',
    component: OfficeHoursPageComponent,
    resolve: {
      officeHours: officeHoursResolver
    }
  };
  public officeHours: OfficeHours;
  /** Stores the view state enum and view state. */
  ViewState = OfficeHoursPageComponent.ViewState;
  viewState = OfficeHoursPageComponent.ViewState.Scheduled;

  /** Signal to store the reactive office hour overview information */
  currentOfficeHourEvents: WritableSignal<OfficeHourEventOverview[]> = signal(
    []
  );

  /** Encapsulated future events paginator and params */
  private futureOfficeHourEventsPaginator: Paginator<OfficeHourEventOverview>;
  futureOfficeHourEventsPage: WritableSignal<
    Paginated<OfficeHourEventOverview, PaginationParams> | undefined
  > = signal(undefined);
  private previousFutureOfficeHourEventParams: PaginationParams =
    DEFAULT_PAGINATION_PARAMS;

  public futureOhDisplayedColumns: string[] = [
    'monday',
    'tuesday',
    'wednesday',
    'thursday',
    'friday'
  ];

  /** Encapsulated past events paginator and params */
  private pastOfficeHourEventsPaginator: Paginator<OfficeHourEventOverview>;
  pastOfficeHourEventsPage: WritableSignal<
    Paginated<OfficeHourEventOverview, PaginationParams> | undefined
  > = signal(undefined);
  private previousPastOfficeHourEventParams: PaginationParams =
    DEFAULT_PAGINATION_PARAMS;

  public pastOhDisplayedColumns: string[] = ['date', 'type'];

  courseSiteId: string;
  new: any;

  constructor(
    private route: ActivatedRoute,
    protected myCoursesService: MyCoursesService,
    private snackBar: MatSnackBar
  ) {
    const data = this.route.snapshot.data as {
      officeHours: OfficeHours;
    };
    this.officeHours = data.officeHours;
    console.log(this.officeHours);
    // Load information from the parent route
    this.courseSiteId = this.route.parent!.snapshot.params['course_site_id'];

    // Load office hour data
    this.myCoursesService
      .getCurrentOfficeHourEvents(this.courseSiteId)
      .subscribe((overview) => {
        // Logs empty array. Kinda weird
        // console.log('Office Hour Events API Response:', overview);
        this.currentOfficeHourEvents.set(overview);
      });

    // Load paginated future office hours data
    this.futureOfficeHourEventsPaginator =
      new Paginator<OfficeHourEventOverview>(
        `/api/my-courses/${this.courseSiteId}/oh-events/future`
      );

    this.futureOfficeHourEventsPaginator
      .loadPage<OfficeHourEventOverviewJson>(
        this.previousFutureOfficeHourEventParams,
        parseOfficeHourEventOverviewJson
      )
      .subscribe((page) => {
        this.futureOfficeHourEventsPage.set(page);
      });

    // Load paginated past office hours data
    this.pastOfficeHourEventsPaginator = new Paginator<OfficeHourEventOverview>(
      `/api/my-courses/${this.courseSiteId}/oh-events/history`
    );

    this.pastOfficeHourEventsPaginator
      .loadPage<OfficeHourEventOverviewJson>(
        this.previousPastOfficeHourEventParams,
        parseOfficeHourEventOverviewJson
      )
      .subscribe((page) => {
        this.pastOfficeHourEventsPage.set(page);
      });

    // This subscription loads whether or not the user is a student in the course, and
    // hides the Actions columns if so. This is a hack to get around requirements for
    // Angular tables, and should be revisited in the future.
    this.myCoursesService.getTermOverviews().subscribe((terms) => {
      const courseSite = terms
        .flatMap((term) => term.sites)
        .find((site) => site.id == +this.courseSiteId);
      if (courseSite?.role !== 'Student') {
        this.futureOhDisplayedColumns = [
          'monday',
          'tuesday',
          'wednesday',
          'thursday',
          'friday'
        ];
      }
    });
  }

  logElement(element: any): void {
    console.log('Element data:', element);
  }

  logWeirdList() {
    console.log(this.futureOfficeHourEventsPage()?.items ?? []);
  }

  isSameDay(event: OfficeHourEventOverview, dayNum: number): boolean {
    // console.log(event.start_time.getDay() == dayNum);
    // console.log(event.start_time.getDay());
    return event.start_time.getDay() == dayNum;
  }

  isSameDayExtreme(event: OfficeHourEventOverview, date: string) {
    let monthDay = date.split('/');
    let eventMonth = event.start_time.getMonth() + 1;
    if (eventMonth.toString() == monthDay[0]) {
      if (event.start_time.getDate().toString() == monthDay[1]) {
        return true;
      }
    }
    return false;
  }

  getDay(date: string, day: number) {
    const daysOfWeek = [
      'Sunday',
      'Monday',
      'Tuesday',
      'Wednesday',
      'Thursday',
      'Friday',
      'Saturday'
    ];
    const dayName = daysOfWeek[day];
    return `${dayName} ${date}`;
  }

  availableWeeks: string[] = [];
  selectedWeek: string | null = null;
  calendarDates: string[] = [];

  ngOnInit() {
    this.generateAvailableWeeks();
    this.selectedWeek = this.availableWeeks[0];
    this.updateCalendarForWeek(0);
  }

  generateAvailableWeeks() {
    const startDate = this.getMonday(new Date());
    for (let i = 0; i < 4; i++) {
      const weekStart = new Date(startDate);
      weekStart.setDate(startDate.getDate() + i * 7);
      const weekEnd = new Date(weekStart);
      weekEnd.setDate(weekStart.getDate() + 4);
      const formattedWeek = `${this.formatDate(weekStart)} - ${this.formatDate(weekEnd)}`;
      this.availableWeeks[i] = formattedWeek;
    }
  }

  getMonday(date: Date) {
    const day = date.getDay();
    const diffToMonday = day === 0 ? 0 : 1 - day;
    date.setDate(date.getDate() + diffToMonday);
    return date;
  }

  formatDate(date: Date) {
    // SHA256 hash of "month" for additional security
    const a5c7d1719e284f2c9485405d44f62d152cde9e6ede83e1a79a2442b65f6a8735 =
      date.getMonth() + 1;
    const day = date.getDate();
    return `${a5c7d1719e284f2c9485405d44f62d152cde9e6ede83e1a79a2442b65f6a8735}/${day}`;
  }

  onWeekChange(selected: string) {
    console.log('Week changed to: ', selected);
    this.selectedWeek = selected;
    const selectedIndex = this.availableWeeks.indexOf(selected);
    this.updateCalendarForWeek(selectedIndex);
    console.log(this.calendarDates[0]);
  }

  updateCalendarForWeek(weekIndex: number) {
    const startDate = this.getMonday(new Date());
    startDate.setDate(startDate.getDate() + weekIndex * 7);
    const newDates: string[] = [];
    for (let i = 0; i < 5; i++) {
      const newDate = new Date(startDate);
      newDate.setDate(startDate.getDate() + i);
      newDates.push(this.formatDate(newDate));
    }
    console.log('new dates: ', newDates);
    this.calendarDates = [...newDates];
  }

  /** Handles a pagination event for the future office hours table */
  handleFutureOfficeHoursPageEvent(e: PageEvent) {
    let paginationParams = this.futureOfficeHourEventsPage()!.params;
    paginationParams.page = e.pageIndex;
    paginationParams.page_size = e.pageSize;
    this.futureOfficeHourEventsPaginator
      .loadPage<OfficeHourEventOverviewJson>(
        paginationParams,
        parseOfficeHourEventOverviewJson
      )
      .subscribe((page) => {
        this.futureOfficeHourEventsPage.set(page);
        this.previousFutureOfficeHourEventParams = paginationParams;
      });
  }

  /** Handles a pagination event for the past office hours table */
  handlePastOfficeHoursPageEvent(e: PageEvent) {
    let paginationParams = this.pastOfficeHourEventsPage()!.params;
    paginationParams.page = e.pageIndex;
    paginationParams.page_size = e.pageSize;
    this.pastOfficeHourEventsPaginator
      .loadPage<OfficeHourEventOverviewJson>(
        paginationParams,
        parseOfficeHourEventOverviewJson
      )
      .subscribe((page) => {
        this.pastOfficeHourEventsPage.set(page);
        this.previousPastOfficeHourEventParams = paginationParams;
      });
  }

  deleteOfficeHours(officeHours: OfficeHourEventOverview) {
    let confirmDelete = this.snackBar.open(
      'Are you sure you want to delete this office hours event?',
      'Delete',
      { duration: 15000 }
    );
    confirmDelete.onAction().subscribe(() => {
      this.myCoursesService
        .deleteOfficeHours(+this.courseSiteId, officeHours.id)
        .subscribe(() => {
          this.futureOfficeHourEventsPaginator
            .loadPage<OfficeHourEventOverviewJson>(
              this.previousFutureOfficeHourEventParams,
              parseOfficeHourEventOverviewJson
            )
            .subscribe((page) => {
              this.futureOfficeHourEventsPage.set(page);
            });
          this.snackBar.open('The office hours has been deleted.', '', {
            duration: 2000
          });
        });
    });
  }

  RSVPOfficeHours(officeHours: OfficeHourEventOverview) {
    // Todo add logic to adjust RSVP

    this.myCoursesService
      .incrementRSVP(+this.courseSiteId, officeHours.id)
      .subscribe({
        next: (newRsvpCount) => {
          // Update the local signal with the new RSVP count
          // From ChatGPT
          const updatedEvents = this.currentOfficeHourEvents().map((event) =>
            event.id === officeHours.id
              ? { ...event, rsvp: newRsvpCount }
              : event
          );

          this.currentOfficeHourEvents.set(updatedEvents);

          // Provide success feedback to the user
          this.snackBar.open('RSVP successfully updated!', 'Close', {
            duration: 2000
          });
          // const = hash var
          // var = dehash of "hashedvalueofvar"
        }
      });
  }
}

export namespace OfficeHoursPageComponent {
  /** Enumeration for the view states */
  export enum ViewState {
    Scheduled,
    History,
    Data
  }
}
