import { Component } from '@angular/core';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';
import { ActivatedRoute } from '@angular/router';
import { from, Observable, of } from 'rxjs';
import { Card } from 'src/app/interfaces/card';
import { Course } from 'src/app/interfaces/course';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent {
  courses: Course[] = [];
  cards: Observable<Card[]> | undefined;

  getCards(data:Course[],breakpoint:string): Observable<Card[]>{
    if(breakpoint == Breakpoints.Small){
      return of(data.map(item =>{
        const card:Card={id:item.id, title:item.description, cols:3, rows:1}
        return card
      }));
    }
    else if(breakpoint == Breakpoints.Medium){
      return of(data.map(item =>{
        const card:Card={id:item.id, title:item.description, cols:item.level, rows:1}
        return card
      }));
    }
    else {
      return of(data.map(item =>{
        const card:Card={id:item.id, title:item.description, cols:1, rows:1}
        return card
      }));
    }
  };

  constructor(
    private breakpointObserver: BreakpointObserver,
    private route: ActivatedRoute
    ) {
      this.route.data.subscribe((response:any)=>{
        this.courses = response.courses;
      });
      this.breakpointObserver.observe([
        Breakpoints.Small, Breakpoints.Medium, Breakpoints.Large
      ]).subscribe(result => {
        if(this.courses.length > 0){
          for (const query of Object.keys(result.breakpoints)) {
            console.log("Eval query: " + query);
            if (result.breakpoints[query]) {
              this.cards = this.getCards(this.courses,query);
              console.log("Apply query: " + query);
            }
          }
        }
      });
    }

  ngOnInit(): void {
  }
}
