// After this test, I get the motion detector has 6 second block time
// which means after receiving one motion signal, the detector will 
// stop working for 6 second. And then, detector will do the work 
// normally. This is the situation at one specific delay time adjust
// and one specific sentivity adjust.
int buttonState ;
int buttonPin = 2;


void setup() {
  // put your setup code here, to run once:
  Serial.begin(115200);
}

void loop() {
  // put your main code here, to run repeatedly:
  buttonState = digitalRead(buttonPin);

  if (buttonState == 1) {

    Serial.println("detected");
  
  }
  
  //delay(1000);

}
