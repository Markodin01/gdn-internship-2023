import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private baseUrl = 'http://localhost:8888';

  constructor(private http: HttpClient) { }

  getAverageExchangeRate(currency: string, date: string) {
    return this.http.get(`${this.baseUrl}/exchange-rate/${currency}/${date}`);
  }
}
