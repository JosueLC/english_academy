//Lesson Resolver
import { Injectable } from '@angular/core';
import { Resolve, ActivatedRouteSnapshot, RouterStateSnapshot } from '@angular/router';
import { Observable } from 'rxjs';

import { Lesson } from 'src/app/interfaces/lesson';
import { LessonService } from 'src/app/services/lesson.service';

@Injectable({ providedIn: 'root' })
export class LessonResolver implements Resolve<Observable<Lesson>> {
    constructor(private lessonService: LessonService) { }

    resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<Lesson> {
        return this.lessonService.getLesson(route.params.id);
    }
}