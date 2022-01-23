// Lesson service
import { Injectable } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, of } from 'rxjs';
import { catchError, map, tap } from 'rxjs/operators';
import { HandlerErr } from './handle.error.service';

import { Lesson } from '../interfaces/lesson';

@Injectable({
    providedIn: 'root'
})
export class LessonService {
    
    url = '/api/v1/class/';

    handleError = HandlerErr.handleError;

    constructor(
        private http: HttpClient
    ) { }

    getLesson(id: string): Observable<Lesson> {
        return this.http.get<Lesson>(this.url + id)
            .pipe(
                catchError(this.handleError<Lesson>('getLesson', undefined))
            );
    }
}
