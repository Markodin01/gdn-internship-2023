import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://localhost:8888';

  constructor(private http: HttpClient) { }

  getAverageExchangeRate(currency: string, date: string) {
    return this.http.get(`${this.baseUrl}/exchanges/${currency}/${date}`);
  }

  getMinMax(currency: string, num_records: number) {
    return this.http.get(`${this.baseUrl}/exchanges/${currency}/max-min/${num_records}`);
  }

  getMajorDifference(currency: string, num_records: number) {
    return this.http.get(`${this.baseUrl}/exchanges/${currency}/major-difference/${num_records}`);
  }
}







