import { Injectable } from '@angular/core';
import { HttpClient} from  '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private API_URL : string = "http://localhost:8000";
  private URL_COMPLEMENT : string = "?format=json";
  constructor(private  httpClient:  HttpClient) {}
  
  getEstados(){
    return this.httpClient.get(this.API_URL+"/estados"+this.URL_COMPLEMENT);
  }

}
