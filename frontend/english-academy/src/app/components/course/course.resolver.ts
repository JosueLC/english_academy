import { Injectable } from "@angular/core";
import { ActivatedRouteSnapshot, Resolve, RouterStateSnapshot } from "@angular/router";
import { Observable } from "rxjs";
import { Course } from "src/app/interfaces/course";
import { CourseService } from "src/app/services/course.service";


@Injectable({ providedIn:'root'})
export class CourseResolver implements Resolve<Observable<Course>>{
    constructor(
        private courseService: CourseService
    ){}

    resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot) {
        return this.courseService.getCourse(String(route.paramMap.get('id')));
    }
}