/**
 * The More Info Modal shows everything related to an future OH event card including the description.
 *
 * @author Christopher Sáez
 * @copyright 2024
 * @license MIT
 */

import { Component } from '@angular/core';
import { MatDialogRef } from '@angular/material/dialog';

@Component({
  selector: 'more-info-modal',
  templateUrl: './more-info-modal.widget.html',
  styleUrls: ['./more-info-modal.widget.css']
})
export class MoreInfoModalWidget {
  constructor(protected dialogRef: MatDialogRef<MoreInfoModalWidget>) {}

  /** Closes the dialog */
  close(): void {
    this.dialogRef.close();
  }
}
