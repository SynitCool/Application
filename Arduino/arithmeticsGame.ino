// Room Code
// Start: 0
// Game: 1
// End: 2
//
// Status
// play = 1
// not play = 0



#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27,16,2);  

int duration = 5;

char corrOpt = 'A';

int hs = 0;
int score = 0;

int butP = A0;
int butA = A1;
int butB = A2;

int warn = 13;

int roomCode = 0;
int status = 0;

void setup()
{
  lcd.init();                      // initialize the lcd 
  // Print a message to the LCD.
  lcd.backlight();

  pinMode(butP, INPUT);
  pinMode(butA, INPUT);
  pinMode(butB, INPUT);
  pinMode(warn, OUTPUT);
  Serial.begin(9600);
}


void loop()
{
  scene();
  transition();
}

void scene() {
  if (roomCode == 0) {
    start();
  } else if (roomCode == 1) {
    game();
  } else if (roomCode == 2) {
    end();
  }
}

void transition() {
  int readP = digitalRead(butP);
  
  if (readP && roomCode == 0) {
    lcd.clear();
    status = 1;
    roomCode = 1;
    game();
    delay(1000);
  } else if (readP && roomCode == 2) {
    lcd.clear();
    roomCode = 0;
    start();
    delay(1000);
  }
  if (status == 0 && roomCode == 1) {
    lcd.clear();
    roomCode = 2;
    end();
    delay(1000);
  }
}

void start() {
  score = 0;
  if (hs == 0) {
    lcd.setCursor(2, 0);
    lcd.print("No Highscore");
  }else{
    lcd.setCursor(2, 0);
    lcd.print("Highscore:");
    lcd.setCursor(12, 0);
    lcd.print(hs);
  }
  lcd.setCursor(5, 1);
  lcd.print("P.Play");
}

void end() {
  lcd.setCursor(2, 0);
  lcd.print("Score:");
  lcd.setCursor(8, 0);
  lcd.print(score);
  lcd.setCursor(5, 1);
  lcd.print("P.Back");
}

void createQuiz() {
  int a = random(0, 99);
  char s = randSign();
  int b = random(1, 99);

  int p = random(6, 9);

  int correct = -1;
  int wrong = -1;

  if (s == '+') {
    correct = a + b;
    wrong = (p*0.1)*correct;  
  } else if (s == '-') {
    correct = a - b;
    wrong = (p*0.1)*correct; 
  } else if (s == 'x') {
    correct = a * b;
    wrong = (p*0.1)*correct; 
  } else if (s == ':') {
    if (b > a) {
      int tmp = b;
      b = a;
      a = tmp;
    }
    correct = a/b;
    wrong = (p*0.1)*correct; 
  }
  Serial.println(s);
  Serial.println(correct);
  Serial.println(wrong);

  corrOpt = randCorrOpt();

  lcd.setCursor(6, 0);
  lcd.print(a);
  lcd.setCursor(8, 0);
  lcd.print(s);
  lcd.setCursor(9, 0);
  lcd.print(b);

  lcd.setCursor(1, 1);
  lcd.print("A.");
  lcd.setCursor(9, 1);
  lcd.print("B.");
  if (corrOpt == 'A') {
    lcd.setCursor(3, 1);
    lcd.print(correct);
    
    lcd.setCursor(11, 1);
    lcd.print(wrong);
  } else if (corrOpt == 'B') {
    lcd.setCursor(3, 1);
    lcd.print(wrong);
    
    lcd.setCursor(11, 1);
    lcd.print(correct);
  }
}

char randCorrOpt() {
  int rand = random(0, 2);
  if (rand == 2) {
    rand--;
  }
  switch(rand){
    case 0:
      return 'A';
    case 1:
      return 'B';
    default:
      return 'F';
  }
}

char randSign() {
  int rand = random(0, 4);
  if (rand == 4) {
    rand--;
  }
  switch(rand){
    case 0:
      return '+';
    case 1:
      return '-';
    case 2:
      return 'x';
    case 3:
      return ':';
    default:
      return 'F';
  }
}

void game() {
  createQuiz();


  if (score > hs) {
    hs = score;
  }

  for (int i = 0; i <= 20; i++) {
    lcd.setCursor(0,0);
    lcd.print(i);
    duration = i;
    if (corrOpt == 'A' && digitalRead(butA)) {
      score++;
      digitalWrite(warn, HIGH);
      delay(2000);
      lcd.clear();
      digitalWrite(warn, LOW);
      return;
    } else if (corrOpt == 'B' && digitalRead(butB)) {
      score++;
      digitalWrite(warn, HIGH);
      delay(2000);
      lcd.clear();
      digitalWrite(warn, LOW);
      return;
    } else if (corrOpt == 'A' && digitalRead(butB)) {
      status = 0;
      digitalWrite(warn, HIGH);
      delay(2000);
      lcd.clear();
      digitalWrite(warn, LOW);
      return;
    } else if (corrOpt == 'B' && digitalRead(butA)) {
      status = 0;
      digitalWrite(warn, HIGH);
      delay(2000);
      lcd.clear();
      digitalWrite(warn, LOW);
      return;
    }
      delay(1000);
    }

  if (duration) {
    status = 0;
  }
}
