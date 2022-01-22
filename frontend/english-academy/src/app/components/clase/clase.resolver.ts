import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, Resolve, RouterStateSnapshot } from '@angular/router';
import { Observable } from 'rxjs';
import { ClassService } from 'src/app/services/class.service';
import { Clase, ClaseSimple } from 'src/app/interfaces/clase';

@Injectable({ providedIn: 'root'})
export class ClassResolver implements Resolve<Observable<Clase>>{
    constructor(
        private classService: ClassService
    ){}

    resolve(route: ActivatedRouteSnapshot, state: RouterStateSnapshot): Observable<Clase> | Observable<Observable<Clase>> | Promise<Observable<Clase>> {
        return this.classService.getClass(String(route.paramMap.get('id')));
    }
}