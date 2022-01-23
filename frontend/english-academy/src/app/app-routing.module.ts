import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CourseComponent } from './components/course/course.component';
import { CourseResolver } from './components/course/course.resolver';
import { HomeComponent } from './components/home/home.component';
import { HomeResolver } from './components/home/home.resolver';
import { LessonComponent } from './components/lesson/lesson.component';
import { LessonResolver } from './components/lesson/lesson.resolver';

const routes: Routes = [
  { path:'', component: HomeComponent, resolve:{courses:HomeResolver}},
  { path:'course/:id', component: CourseComponent, resolve:{course:CourseResolver}, data:{id:''}},
  { path:'lesson/:id', component: LessonComponent, resolve:{lesson:LessonResolver}, data:{id:''}}
]

@NgModule({
  declarations: [],
  imports: [
    RouterModule.forRoot(routes)
  ],
  exports: [RouterModule]
})
export class AppRoutingModule { }
