import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class BookingService {
  API = 'http://127.0.0.1:5000/api';

  constructor(private http: HttpClient) {}

  book(name: string) {
    return this.http.post(`${this.API}/book`, { apartment: name });
  }
}
