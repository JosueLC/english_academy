import { Observable, of } from "rxjs";

export class HandlerErr {
    public static handleError<T>(instance='instance', operation = 'operation', result?: T) {
        return (error: any): Observable<T> => {
            console.error(error); // log to console instead
            return of(result as T);
        }
    }
}