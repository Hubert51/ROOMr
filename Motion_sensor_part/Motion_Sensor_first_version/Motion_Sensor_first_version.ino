int out[20];
void setup() 
{
  // put your setup code here, to run once:
  Serial.begin(115200);
  pinMode(2,INPUT);
  int out[20];

}

void loop() 
{
  int sum=0;
  int numcount=0;
  // put your main code here, to run repeatedly:
  Serial.begin(115200);
  
  assign(analogRead(A0));
  for(int i=0;i<20;i+=1)
  {
    sum+=out[i];
  }
  if (sum>100)
  { 
    numcount+=1;
    Serial.println("1!!!!!!!!!!!!!!!!"); 
  }
  else
  {
    Serial.println("0");
  }
  delay(500);
}
void assign(int n)
{
  
  for(int i=0;i<20;i+=1)
  {
    if(i==19)
    {
      out[i]=n;
      
      delay(50);
      break;
    }
    out[i]=out[i+1];
    
  }
  
}
