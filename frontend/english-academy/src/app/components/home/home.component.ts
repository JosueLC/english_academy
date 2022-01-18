import { Component } from '@angular/core';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';
import { ActivatedRoute } from '@angular/router';
import { Observable, of } from 'rxjs';
import { Card } from 'src/app/interfaces/card';
import { Course } from 'src/app/interfaces/course';


@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})

export class HomeComponent {
  cards: Observable<Card[]> | undefined;
  /** Based on the screen size, switch from standard to one column per row */
  
  getCards(data:Course[]): Observable<Card[]>{
    const list = data.map(item=>{
      const card:Card = {id:item.id,title:item.name,cols:1,rows:1};
      return card;
    })
    return of(list);
  };

  constructor(
    private breakpointObserver: BreakpointObserver,
    private route: ActivatedRoute
    ) {}

  ngOnInit(): void {
    this.route.data.subscribe((response:any)=>{
      this.cards = this.getCards(response.courses);
    });
  }
}
