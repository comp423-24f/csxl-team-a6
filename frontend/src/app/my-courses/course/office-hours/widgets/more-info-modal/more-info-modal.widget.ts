/**
 * The More Info Modal shows everything related to an future OH event card including the description.
 *
 * @author Christopher Sáez
 * @copyright 2024
 * @license MIT
 */

import { Component, Inject } from '@angular/core';
import { OfficeHourEventOverview } from '../../../../my-courses.model';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'more-info-modal',
  templateUrl: './more-info-modal.widget.html',
  styleUrls: ['./more-info-modal.widget.css']
})
export class MoreInfoModalWidget {
  // @Input() event!: OfficeHourEventOverview; - must use the injection token instead since this is a dialog not a regular component

  constructor(
    @Inject(MAT_DIALOG_DATA) public data: any,
    protected dialogRef: MatDialogRef<MoreInfoModalWidget>
  ) {}

  /** Closes the dialog */
  close(): void {
    this.dialogRef.close();
  }
}
