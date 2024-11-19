/**
 * The Office Hours Event Card widget defines the UI card for each instance of an office hours event
 *
 * @author Ian
 * @copyright 2024
 * @license MIT
 */

import { Component, Input, Output, EventEmitter } from '@angular/core';
import { OfficeHourEventOverview } from '../../my-courses.model';

@Component({
  selector: 'office-hours-event-card',
  templateUrl: './office-hours-event-card.widget.html',
  styleUrls: ['./office-hours-event-card.widget.scss']
})
export class OfficeHoursEventCardComponent {
  /**
   * The office hours event data to display in the card.
   */
  @Input() event!: OfficeHourEventOverview;

  /**
   * Event emitted when the "More info" button is clicked.
   */
  // @Output() moreInfo = new EventEmitter<OfficeHourEventOverview>();

  /**
   * Event emitted when the "Book" button is clicked.
   */
  // @Output() book = new EventEmitter<OfficeHourEventOverview>();

  /**
   * Logs the current event data to the console.
   * Useful for debugging purposes.
   */
  logElement(): void {
    console.log('Office Hours Event:', this.event);
  }

  /**
   * Emits the moreInfo event with the current event data.
   */
}
