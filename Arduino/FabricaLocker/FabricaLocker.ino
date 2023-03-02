// Main core of the FabricaLocker project, this reads and output to the serial all the info from the RFID reader (mrfc522) and listen for the response from server, than open the locker door.
// Snow-sr @ Fábrica de Software - 2023
#include <SPI.h>
#include <MFRC522.h>

#define SS_PIN 10
#define RST_PIN 9

MFRC522 rfid(SS_PIN, RST_PIN);

void setup()
{
    Serial.begin(9600);
    SPI.begin();
    rfid.PCD_Init();
}

void loop()
{
    if (!rfid.PICC_IsNewCardPresent() || !rfid.PICC_ReadCardSerial())
        return;

    String strID = "";
    for (byte i = 0; i < 4; i++)
    {
        strID +=
            (rfid.uid.uidByte[i] < 0x10 ? "0" : "") +
            String(rfid.uid.uidByte[i], HEX) +
            (i != 3 ? ":" : "");
    }
    strID.toUpperCase();

    Serial.print("Identificador (UID) da tag: ");
    Serial.println(strID);

    rfid.PICC_HaltA();
    rfid.PCD_StopCrypto1();