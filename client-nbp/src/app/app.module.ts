import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { ExchangeRateComponent } from './components/exchange-rate/exchange-rate.component';
import { FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';

@NgModule({
  declarations: [
    AppComponent,
    ExchangeRateComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpClientModule,

  ],
  providers: [
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
