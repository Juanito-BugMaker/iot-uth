#include <Arduino.h>
#include <WiFi.h>
#include <HTTPClient.h>
#include <ArduinoJson.h>
#include "DHTesp.h"

const char* ssid = "Wokwi-GUEST";
const char* password = "";
const char* serverName = "http://host.wokwi.internal:8000/api/sensor/";

DHTesp dht;
#define DHT_PIN 15 // Sincronizado EXACTAMENTE con el cable verde
#define LED_PIN 2

void setup() {
  pinMode(LED_PIN, OUTPUT);
  dht.setup(DHT_PIN, DHTesp::DHT22);
  
  WiFi.begin(ssid, password);
  while(WiFi.status() != WL_CONNECTED) {
    digitalWrite(LED_PIN, !digitalRead(LED_PIN)); 
    delay(500);
  }
  digitalWrite(LED_PIN, HIGH); 
}

void loop() {
  if(WiFi.status() == WL_CONNECTED){
    digitalWrite(LED_PIN, LOW); 
    
    // Leer sensor DHT22
    TempAndHumidity data = dht.getTempAndHumidity();
    float temp = data.temperature;
    float hum = data.humidity;
    
    // Trampa de error cambiada a 88.8
    if (isnan(temp) || isnan(hum)) {
      temp = 88.8; 
      hum = 88.8;
    }

    // Armar JSON
    StaticJsonDocument<200> jsonDoc;
    jsonDoc["temperatura"] = temp;
    jsonDoc["humedad"] = hum;
    
    String jsonString;
    serializeJson(jsonDoc, jsonString);
    
    // Disparar a Django local
    WiFiClient client;
    HTTPClient http;
    http.begin(client, serverName); 
    http.addHeader("Content-Type", "application/json");
    
    int httpResponseCode = http.POST(jsonString);
    
    if (httpResponseCode > 0) {
      digitalWrite(LED_PIN, HIGH); delay(1500); digitalWrite(LED_PIN, LOW);
    } else {
      for(int i=0; i<3; i++) { digitalWrite(LED_PIN, HIGH); delay(150); digitalWrite(LED_PIN, LOW); delay(150); }
    }
    http.end();
  }
  delay(4000); 
}

