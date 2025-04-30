#include <DHT.h>

#define DHTPIN 2
#define DHTTYPE DHT11
#define LDR_PIN A0

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();
  delay(1000);
}

void loop() {
  float temp = dht.readTemperature();
  float humi = dht.readHumidity();
  int light = analogRead(LDR_PIN);

  if (isnan(temp) || isnan(umi)) {
    Serial.println("Falha ao ler o Sensor");
  } else {
    Serial.print("{\"temp\": ");
    Serial.print(temp);
    Serial.print(", \"humi\": ");
    Serial.print(humi);
    Serial.print(", \"light\": ");
    Serial.print(light);
    Serial.println("}");
  }

  delay(5000);

  // atualizacao futura para receber os dados da API
  // if (Serial.available() > 0) {
  //   String comando = Serial.readStringUntil('\n');
  //   comando.trim();
  //   Serial.print("Comando recebido: ");
  //   Serial.println(comando);
  // }
}