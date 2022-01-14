import { Component, OnInit } from '@angular/core';
import { Course } from 'src/app/entities/course';

@Component({
  selector: 'app-course',
  templateUrl: './course.component.html',
  styleUrls: ['./course.component.css']
})
export class CourseComponent implements OnInit {

  courses: Course[] = [{
    id: '879bfbb0-c85b-48f9-8f8f-d84da3e2d281',
    name: 'Angular',
    description: 'Angular is a platform that makes it easy to build applications with the web.',
    level: 1
  }];

  constructor() { }

  ngOnInit(): void {
  }

}
