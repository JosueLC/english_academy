import { Component } from '@angular/core';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';
import { ActivatedRoute } from '@angular/router';
import { Observable, of } from 'rxjs';
import { Card } from 'src/app/interfaces/card';
import { Course } from 'src/app/interfaces/course';
import { ClaseSimple } from 'src/app/interfaces/clase';


@Component({
  selector: 'app-course',
  templateUrl: './course.component.html',
  styleUrls: ['./course.component.css']
})

export class CourseComponent {
  course: Course | undefined;
  cards: Observable<Card[]> | undefined;

  getCards(data:ClaseSimple[],breakpoint:string): Observable<Card[]>{
    if(breakpoint == Breakpoints.Small){
      return of(data.map(item =>{
        const card:Card={id:item.id, title:item.name, cols:3, rows:1}
        return card
      }));
    }
    else if(breakpoint == Breakpoints.Medium){
      return of(data.map(item =>{
        const card:Card={id:item.id, title:item.name, cols:1, rows:1}
        return card
      }));
    }
    else {
      return of(data.map(item =>{
        const card:Card={id:item.id, title:item.name, cols:1, rows:1}
        return card
      }));
    }
  };

  constructor(
    private breakpointObserver: BreakpointObserver,
    private route: ActivatedRoute
    ) {
      this.route.data.subscribe((response:any)=>{
        this.course = response.course;
      });
      this.breakpointObserver.observe([
        Breakpoints.Small, Breakpoints.Medium, Breakpoints.Large
      ]).subscribe(result => {
        if(this.course != undefined){
          for (const query of Object.keys(result.breakpoints)) {
            console.log("Eval query: " + query);
            if (result.breakpoints[query]) {
              this.cards = this.getCards(this.course.classes,query);
              console.log("Apply query: " + query);
            }
          }
        }
      });
    }

  ngOnInit(): void {
  }
}
