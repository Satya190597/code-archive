import { Component, OnInit } from '@angular/core';
import {MatTableModule} from '@angular/material/table'
import * as XLSX from 'xlsx';


@Component({
  selector: 'app-read-spreadsheet',
  templateUrl: './read-spreadsheet.component.html',
  styleUrls: ['./read-spreadsheet.component.css']
})
export class ReadSpreadsheetComponent implements OnInit {

  private data
  constructor() { }

  ngOnInit() {
  }

  constructHtml() {
    
  }
  onUploadFile(event:any) {

      // const target = <DataTransfer>(event.target);
      const fileReader = new FileReader();
      fileReader.onload = (e:any) => {
      const bstr: string = e.target.result;
      const wb: XLSX.WorkBook = XLSX.read(bstr,{type:'binary'})
      const wsname: string = wb.SheetNames[0]
      console.log(wsname)
      const ws: XLSX.WorkSheet = wb.Sheets[wsname]

      this.data = XLSX.utils.sheet_to_json(ws,{header:1});
      this.constructHtml()
      }
      fileReader.readAsBinaryString(event.target.files[0])
      
  }
  showCellMenu(row,cell) {
    document.getElementById(row+""+cell).style.display = 'block';
  }

  deleteCell(row,cell) {
    this.data[row].splice(cell,1)
  }
}
