import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <h1>Welcome</h1>
    <app-read-spreadsheet></app-read-spreadsheet>
  `,
  styles: []
})
export class AppComponent {
  title = 'GeneralUI';
}
