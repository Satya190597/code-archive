import { Component, OnInit } from '@angular/core';

import * as Chart from 'chart.js'
import { Label } from 'ng2-charts';


@Component({
  selector: 'app-first-bar-chart',
  templateUrl: './first-bar-chart.component.html',
  styleUrls: ['./first-bar-chart.component.css']
})
export class FirstBarChartComponent implements OnInit {
    
    public barChartOption: Chart.ChartOptions = {
        responsive: true
    }
    public barChartLabels: Label[] = ['2001','2002','2003','2004','2005']
    public barChartType: Chart.ChartType = "bar"
    public barChartLegend = true;
    public barChartPlugins = [];

    public barChartData: Chart.ChartDataSets[] = [
        {data:[10,20,30,40,50],label:"Series A"},
        {data:[50,60,40,20,10],label:"Series B"}
    ]
    constructor() { 

    }

    ngOnInit() {
        
    }

}
