import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';
import { FormControl, Validators } from '@angular/forms';
import { Observable } from 'rxjs';


@Component({
  selector: 'app-exchange-rate',
  templateUrl: './exchange-rate.component.html',
  styleUrls: ['./exchange-rate.component.scss']
})
export class ExchangeRateComponent implements OnInit {
  currency!: string;
  date!: string;
  number!: number | null;
  averageRate!: number;
  minMax!: string;
  majorDiff!: Observable<number>;;
  numberFormControl = new FormControl('', [Validators.required, Validators.min(1), Validators.max(255)]);


  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  isWeekend = (date: Date): boolean => {
    const day = date.getDay();
    // Prevent Saturday and Sunday from being selected.
    return day !== 0 && day !== 6;
  }

  getExchangeRate() {
    this.apiService.getAverageExchangeRate(this.currency, this.date).subscribe((data: any) => {
      this.averageRate = data.rate;
    });
  }
  getMinMax() {
    if (this.number !== null) {
      this.apiService.getMinMax(this.currency, this.number).subscribe((data: any) => {
        this.minMax = data.max + '+' + data.min
      });
    }
  }
  
  getMajorDiff() {
    if (this.number !== null){
      this.apiService.getMajorDifference(this.currency, this.number).subscribe((data: any) => {
        this.majorDiff = data;
      });
    }
  }
  
}
