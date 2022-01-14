import { Component, OnInit } from '@angular/core';

import { Course } from 'src/app/interfaces/course';
import { CourseService } from 'src/app/services/course.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {

  course_list: Course[] = [];
  
  constructor(
    private courseService:CourseService
  ) { }

  getCourses(): void {
    this.courseService.getCourses().subscribe(courses => this.course_list = courses)
  }

  ngOnInit(): void {
    this.getCourses();
  }

}
