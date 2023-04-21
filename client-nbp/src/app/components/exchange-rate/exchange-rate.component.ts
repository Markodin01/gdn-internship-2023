import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-exchange-rate',
  templateUrl: './exchange-rate.component.html',
  styleUrls: ['./exchange-rate.component.scss']
})
export class ExchangeRateComponent implements OnInit {
  currency!: string;
  date!: string;
  num!: string;
  averageRate!: number;
  minMax!: number;
  majorDiff!: number;

  constructor(private apiService: ApiService) { }

  ngOnInit(): void {
  }

  getExchangeRate() {
    this.apiService.getAverageExchangeRate(this.currency, this.date).subscribe((data: any) => {
      this.averageRate = data.average_rate;
    });
  }
  getMinMax() {
    this.apiService.getAverageExchangeRate(this.currency, this.num).subscribe((data: any) => {
      this.minMax = data.minMax;
    });
  }
  getMajorDiff() {
    this.apiService.getAverageExchangeRate(this.currency, this.num).subscribe((data: any) => {
      this.majorDiff = data.majorDiff;
    });
  }
}
