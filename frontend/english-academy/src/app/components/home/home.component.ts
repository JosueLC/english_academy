import { Component } from '@angular/core';
import { BreakpointObserver } from '@angular/cdk/layout';
import { ActivatedRoute } from '@angular/router';
import { of } from 'rxjs';
import { Card } from 'src/app/interfaces/card';
import { Course } from 'src/app/interfaces/course';
import { BaseComponent } from '../base/base.component';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent extends BaseComponent {
  
  constructor(
    public breakpointObserver: BreakpointObserver,
    public route: ActivatedRoute
  ) {
    super(breakpointObserver,route)
  }

  ngOnInit(): void {
    //Get courses from server with route. After that, convert to basecards
    this.route.data.subscribe((response:any) =>{
      this.baseItems = response.courses;
      //console.log(this.baseItems);
      this.baseCards = of(this.baseItems.map(course => this.courseToCard(course)));
    });
    
  }

  courseToCard(course:Course): Card {
    const card: Card = {
      id : course.id,
      title: course.name,
      description: "{description: '" + course.description + "'}",
    }
    return card;
  }
}
