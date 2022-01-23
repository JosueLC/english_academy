// Interface to course object
// Attributes:

import { CorpusText } from "./corpustext";

export interface Lesson{
    id: string;
    name: string;
    course_id: string;
    description: string;
    audio:string;
    texts:CorpusText[]
}

export interface LessonSimple{
    id: string;
    name: string;
    course_id: string;
}