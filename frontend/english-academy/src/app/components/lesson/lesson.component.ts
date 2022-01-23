import { Component } from '@angular/core';
import { BreakpointObserver, Breakpoints, BreakpointState } from '@angular/cdk/layout';
import { MatButtonToggleAppearance } from '@angular/material/button-toggle';
import { FormBuilder } from '@angular/forms';
import { ActivatedRoute } from '@angular/router';
import { Lesson } from 'src/app/interfaces/lesson';

@Component({
  selector: 'app-lesson',
  templateUrl: './lesson.component.html',
  styleUrls: ['./lesson.component.css']
})
export class LessonComponent {

  lesson!:Lesson;
  isViewSmall:boolean=true; //first mobile
  isViewMedium:boolean=false;
  isViewLarge:boolean=false;

  showHideText:boolean = false;
  appearance: MatButtonToggleAppearance = 'legacy'

  form = this.fb.group({
    sentences: this.fb.array([])
  });

  constructor(
    private route: ActivatedRoute,
    private breakpointObserver: BreakpointObserver,
    private fb: FormBuilder
  ) {
    this.breakpointObserver.observe([
      Breakpoints.Small, Breakpoints.Medium, Breakpoints.Large
    ]).subscribe((state:BreakpointState)=>{
      this.isViewSmall = state.breakpoints[Breakpoints.Small];
      this.isViewMedium = state.breakpoints[Breakpoints.Medium];
      this.isViewLarge = state.breakpoints[Breakpoints.Large];
    })
  }

  showTexts(): void {
    console.log("show: " + this.showHideText);
    this.showHideText = !this.showHideText;
  }

  ngOnInit(): void {
    this.route.data.subscribe((response:any) =>{
      this.lesson = response.lesson;
    });
  }
}
