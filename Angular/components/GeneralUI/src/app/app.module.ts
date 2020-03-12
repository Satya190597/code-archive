import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { ReadSpreadsheetComponent } from './read-spreadsheet/read-spreadsheet.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import {MatTableModule} from '@angular/material/table';
import { FirstBarChartComponent } from './first-bar-chart/first-bar-chart.component';
import {ChartsModule} from 'ng2-charts'


@NgModule({
  declarations: [
    AppComponent,
    ReadSpreadsheetComponent,
    FirstBarChartComponent
  ],
  imports: [
    BrowserModule,
    BrowserAnimationsModule,
    MatTableModule,
    ChartsModule
    
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
