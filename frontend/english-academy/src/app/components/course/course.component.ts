import { Component } from '@angular/core';
import { BaseComponent } from '../base/base.component';
import { Course } from 'src/app/interfaces/course';
import { ClaseSimple } from 'src/app/interfaces/clase';
import { Card } from 'src/app/interfaces/card';
import { of } from 'rxjs';


@Component({
  selector: 'app-course',
  templateUrl: './course.component.html',
  styleUrls: ['./course.component.css']
})

export class CourseComponent extends BaseComponent {
  course!: Course;

  ngOnInit(): void {
    this.route.data.subscribe((response:any) =>{
      this.course = response.course;
      this.baseItems = this.course.classes;
      this.baseCards = of(this.baseItems.map(c => this.classToCard(c)));
    })
  }

  classToCard(c:ClaseSimple): Card {
    const card: Card = {
      id : c.id,
      title: c.name,
      description: "{course: '" + c.course_id + "'}",
    }
    return card;
  }
}
