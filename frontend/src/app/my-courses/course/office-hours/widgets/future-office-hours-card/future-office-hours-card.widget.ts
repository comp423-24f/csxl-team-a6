/**
 * The Office Hours Event Card widget defines the UI card for each instance of an office hours event
 *
 * @author Ian
 * @copyright 2024
 * @license MIT
 */

import { Component, Input, Output, EventEmitter } from '@angular/core';
import { OfficeHourEventOverview } from '../../../../my-courses.model';
import { MatDialog } from '@angular/material/dialog';
import { MoreInfoModalWidget } from '../more-info-modal/more-info-modal.widget';

@Component({
  selector: 'future-office-hours-card',
  templateUrl: './future-office-hours-card.widget.html',
  styleUrls: ['./future-office-hours-card.widget.scss']
})
export class FutureOfficeHoursCardWidget {
  /**
   * The office hours event data to display in the card.
   */
  @Input() event!: OfficeHourEventOverview;
  @Input() shouldDisplay!: boolean;
  @Input() role!: string;

  @Output() deleteButtonPressed = new EventEmitter<OfficeHourEventOverview>();

  constructor(protected dialog: MatDialog) {}

  /**
   * (We probably won't need to emit an event since nothing needs to happen down the stack)
   * Event emitted when the "More info" button is clicked.
   */
  // @Output() moreInfo = new EventEmitter<OfficeHourEventOverview>();
  onMoreInfoClick(OHevent: OfficeHourEventOverview): void {
    const dialogRef = this.dialog.open(MoreInfoModalWidget, {
      data: { event: OHevent },
      width: '1000px',
      autoFocus: false
    });
    dialogRef.afterClosed().subscribe();
  }

  /**
   * Event emitted when the "Book" button is clicked.
   */
  // @Output() book = new EventEmitter<OfficeHourEventOverview>();

  /**
   * Logs the current event data to the console.
   * Useful for debugging purposes.
   */
  logElement() {
    console.log('Office Hours Event:', this.event);
    return 'Office Hours Event: ' + this.event;
  }

  /**
   * Emits the moreInfo event with the current event data.
   */
}
