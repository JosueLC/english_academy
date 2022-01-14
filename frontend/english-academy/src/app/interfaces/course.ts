// Interface to course object
// Attributes:
// id: string uuid
// name: string
// description: string
// level: int
// classes: optional list of class object

import { Clase } from "./clase";

export interface Course{
    id: string;
    name: string;
    description: string;
    level: number;
    classes?:Clase[]
}