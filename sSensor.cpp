void setup() {
  Serial.begin(9600);
  delay(1000);
  randomSeed(analogRead(0));
}

void loop() {
  float temperatura = random(200, 350) / 10.0;
  float umidade = random(400, 800) / 10.0;
  int luz = random(0, 1024);

  String json = "{";
  json += "\"temperatura\": " + String(temperatura, 1) + ", ";
  json += "\"umidade\": " + String(umidade, 1) + ", ";
  json += "\"luz\": " + String(luz);
  json += "}";

  Serial.println(json);
  delay(5000);
}