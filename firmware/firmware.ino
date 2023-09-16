const int arraySize = 24;
int data[arraySize] = { /* your 24 values here, e.g., 1, 2, 3, ... */ };

void setup() {
  Serial.begin(9600);  // Start the serial communication at 9600 baud rate
}

void loop() {
  for (int i = 0; i < arraySize; i++) {
    Serial.print(data[i]);
    
    // If it's not the last element, send a comma as a delimiter
    if (i < arraySize - 1) {
      Serial.print(",");
    }
  }
  
  Serial.println();  // Send a newline character to mark the end of data
  
  delay(2000);  // Delay for 2 seconds before sending the data again
}
