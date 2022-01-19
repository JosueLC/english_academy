// Interface to course object
// Attributes:

import { CorpusText } from "./corpustext";

export interface Clase{
    id: string;
    name: string;
    course_id: string;
    description: string;
    audio:string;
    texts:CorpusText[]
}

export interface ClaseSimple{
    id: string;
    name: string;
    course_id: string;
}