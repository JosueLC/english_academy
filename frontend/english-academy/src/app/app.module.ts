import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';
import { BrowserModule } from '@angular/platform-browser';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';

import { MaterialModule } from './material.module';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { HomeComponent } from './components/home/home.component';
import { HomeResolver } from './components/home/home.resolver';
import { CourseComponent } from './components/course/course.component';
import { CourseResolver } from './components/course/course.resolver';
import { LayoutModule } from '@angular/cdk/layout';
import { BaseComponent } from './components/base/base.component';
import { LessonComponent } from './components/lesson/lesson.component';
import { ReactiveFormsModule } from '@angular/forms';


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    CourseComponent,
    BaseComponent,
    LessonComponent
  ],
  imports: [
    HttpClientModule,
    BrowserModule,
    BrowserAnimationsModule,
    MaterialModule,
    AppRoutingModule,
    LayoutModule,
    ReactiveFormsModule
  ],
  providers: [
    HomeResolver,
    CourseResolver
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
