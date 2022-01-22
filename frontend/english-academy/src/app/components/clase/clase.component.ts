import { Component } from '@angular/core';
import { map } from 'rxjs/operators';
import { Breakpoints, BreakpointObserver } from '@angular/cdk/layout';
import { Clase } from 'src/app/interfaces/clase';
import { BaseComponent } from '../base/base.component';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-clase',
  templateUrl: './clase.component.html',
  styleUrls: ['./clase.component.css']
})
export class ClaseComponent{
  clase!: Clase;

  constructor(
    private breakpointObserver: BreakpointObserver,
    private route: ActivatedRoute
  ) { 
  }

  ngOnInit(): void {}
}
