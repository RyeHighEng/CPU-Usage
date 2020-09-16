#include "U8g2lib.h"


int cpu = 0;
String s;
U8G2_SSD1306_128X32_UNIVISION_F_SW_I2C u8g2(U8G2_R0, /* clock=*/ SCL, /* data=*/ SDA, /* reset=*/ U8X8_PIN_NONE); 

void draw(void) {
 // u8g2.clearBuffer();
  cpu = Serial.read();
  s = "CPU: " + String(cpu) + "%";
 // u8g2.drawStr(0,10, s);
  //u8g2.sendBuffer();
  u8g2.setCursor(0,10);
  u8g2.print(s);
  //delay(50);
}

void setup(void) {
  u8g2.begin();
  u8g2.setFont(u8g_font_unifont);
}

void loop(void) {
  // picture loop
  u8g2.firstPage();  
  do {
    draw();
  } while( u8g2.nextPage() );


  // rebuild the picture after some delay
  delay(20);
}
