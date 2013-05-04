

int myPins[] = {22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41};
const int pins = 20;

//int myPins[] = {36,37};
//const int pins = 2;

int values[pins];
int old_values[pins];
int val = 0;
int changed = 0;

void setup() {
  for (int i = 0; i < pins; i = i + 1) {
    pinMode(myPins[i], INPUT);
    values[i] = 0;
    old_values[i] = 0;
  }
  Serial.begin(9600);
}

void loop(){
  changed = 0;
  for (int i = 0; i < pins; i = i + 1) {
    if (digitalRead(myPins[i]) == LOW) {
      values[i] = 0;
    }
    else {
      values[i] = 1;
    }
    if (values[i] != old_values[i]) {
      changed = changed + 1;
    }
  }
  if (changed > 0) {
    for (int i = 0; i < pins; i = i + 1) {
      if (i > 0) {
        Serial.print(",");
      }
      Serial.print(values[i]);
    }
    Serial.println("");
  }
  for (int i = 0; i < pins; i = i + 1) {
    old_values[i] = values[i];
  }
}
