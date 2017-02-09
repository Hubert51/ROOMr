/*
Arduino Motion Sensor Burglar Alarm Project
by Arvind Sanjeev
Please check out  http://diyhacking.com for the tutorial of this project.
DIY Hacking
*/


int speakerOut = 9;//Piezo buzzer's positive terminal is connected to digital pin 9               
byte names[] = {'c', 'd', 'e', 'f', 'g', 'a', 'b', 'C'};  
int tones[] = {1915, 1700, 1519, 1432, 1275, 1136, 1014, 956};
byte melody[] = "2d2a1f2c2d2a2d2c2f2d2a2c2d2a1f2c2d2a2a2g2p8p8p8p";
// count length: 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0
//                                10                  20                  30
int count = 0;
int count2 = 0;
int count3 = 0;
int MAX_COUNT = 24;
int statePin = LOW;
void siren();

 volatile byte intruder;
 void setup()
 {
   Serial.begin(115200);
   attachInterrupt(0, intruder_detect, RISING);//Initialize the intterrupt pin for the motion sensor (Arduino digital pin 2)
   intruder = 0;
 }
 void loop()
 {
   
 }
 void intruder_detect()//This function is called whenever an intruder is detected by the arduino
 {
   intruder++;
   Serial.println("Intruder detected");
   for(int i=0; i<3; i++)//Play the alarm three times
   siren();
 }
 void siren()//This function will make the alarm sound using the piezo buzzer
{
for (count = 0; count < MAX_COUNT; count++) {
      for (count3 = 0; count3 <= (melody[count*2] - 48) * 30; count3++) {
      for (count2=0;count2<8;count2++) {
        if (names[count2] == melody[count*2 + 1]) {       
          analogWrite(speakerOut,1023);
          delayMicroseconds(tones[count2]);
          analogWrite(speakerOut, 0);
          delayMicroseconds(tones[count2]);
        } 
        if (melody[count*2 + 1] == 'p') {
          // make a pause of a certain size
          analogWrite(speakerOut, 0);
          delayMicroseconds(100);
        }
      }
    }
  }
}
