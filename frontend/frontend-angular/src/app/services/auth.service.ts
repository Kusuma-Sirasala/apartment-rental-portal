import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
const API_URL = 'http://127.0.0.1:5000/api';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  constructor(private http: HttpClient) {}

  register(data: any): Observable<any> {
    return this.http.post(`${API_URL}/register`, data);
  }

  login(data: any): Observable<any> {
    return this.http.post(`${API_URL}/login`, data);
  }
}
