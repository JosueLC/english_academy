import { BreakpointObserver, Breakpoints, BreakpointState } from '@angular/cdk/layout';
import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Observable, of } from 'rxjs';
import { Card } from 'src/app/interfaces/card';

@Component({
  selector: 'app-base',
  template: ``,
  styleUrls: ['./base.component.css']
})
export class BaseComponent implements OnInit {
  
  baseItems: Array<any> = [];
  baseCards: Observable<Card[]> = new Observable<Array<Card>>();

  isViewSmall:boolean=true; //first mobile
  isViewMedium:boolean=false;
  isViewLarge:boolean=false;

  constructor(
    public breakpointObserver: BreakpointObserver,
    public route: ActivatedRoute
  ){
    this.breakpointObserver.observe([
      Breakpoints.Small, Breakpoints.Medium, Breakpoints.Large
    ]).subscribe((state:BreakpointState)=>{
      this.isViewSmall = state.breakpoints[Breakpoints.Small];
      this.isViewMedium = state.breakpoints[Breakpoints.Medium];
      this.isViewLarge = state.breakpoints[Breakpoints.Large];
    })
  }

  ngOnInit(): void {
  }

}
