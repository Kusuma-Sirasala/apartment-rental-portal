import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({ providedIn: 'root' })
export class ApartmentService {
  API = 'http://127.0.0.1:5000/api';

  constructor(private http: HttpClient) {}

  getApartments() {
    return this.http.get(`${this.API}/apartments`);
  }
}
