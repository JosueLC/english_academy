import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';

import { Course } from '../interfaces/course';

@Injectable({
  providedIn: 'root'
})
export class CourseService {

  url = '/api/v1/course/';

  constructor(
    private http: HttpClient
  ) { }

  getCourses(): Observable<Course[]> {
    return this.http.get<Course[]>(this.url)
      .pipe(
        catchError(this.handleError<Course[]>('getCourses',[]))
      );
  }

  getCourse(id: string): Observable<Course> {
    return this.http.get<Course>(this.url + id)
      .pipe(
        catchError(this.handleError<Course>('getCourse',undefined))
      );
  }

  private handleError<T>(operation = 'operation', result?: T){
    return (error:any): Observable<T> => {
      // TODO: send the error to remote logging infrastructure
      console.error(error); // log to console instead

      // TODO: better job of transforming error for user consumption
      //this.log(`${operation} failed: ${error.message}`);

      // Let the app keep running by returning an empty result.
      return of(result as T);
    }
  }
}
