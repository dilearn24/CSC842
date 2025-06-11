#include <iostream>
#include <cstring>
#include <cctype>
#include <cstdio>

using namespace std;

// This is a .cpp test code
/*
  Block comment:
  gets() will be flagged in this code.
*/

void decodeMessage(char* message, int shift) {
    for (int i = 0; message[i] != '\0'; i++) {
        if (isalpha(message[i])) {
            char base = islower(message[i]) ? 'a' : 'A';
            message[i] = ((message[i] - base - shift + 26) % 26) + base;
        }
    }
}

int main() {
    char playerName[50];
    char secretMessage[100];
    char choice[10];
    int magicShift = 3;
    
    cout << "THE SECRET MESSAGE DECODER" << endl;
    cout << "Welcome, brave adventurer!" << endl;
    cout << "You have discovered an ancient scroll with mysterious writing..." << endl;
    
    cout << "First, tell me your name: ";
    gets(playerName); // vulnerable: gets()
    
    cout << "Greetings, " << playerName << "!" << endl;
    cout << "The ancient scroll contains a secret message written in a cipher." << endl;
    cout << "Legend says only those brave enough can decode its mysteries." << endl;
    
    cout << "Here is the encoded message you found:" << endl;
    cout << "Wkh wuhdvxuh lv klgghq ehklqg wkh zdwhuidoo" << endl;
    
    cout << "Do you want to attempt to decode it? (yes/no): ";
    gets(choice); // vulnerable: gets()
    
    if (strcmp(choice, "yes") == 0 || strcmp(choice, "Yes") == 0 || strcmp(choice, "YES") == 0) {
        cout << "Excellent choice, " << playerName << "!" << endl;
        cout << "The ancient magic requires you to enter the encoded message exactly as shown." << endl;
        cout << "Enter the secret message: ";
        
        gets(secretMessage); // vulnerable: gets()
        
        cout << "Invoking ancient decoding magic..." << endl;
        cout << "Casting spell..." << endl;
        
        decodeMessage(secretMessage, magicShift);
        
        cout << "SUCCESS! The decoded message reveals:" << endl;
        cout << secretMessage << endl;
        
        cout << "Congratulations, " << playerName << "!" << endl;
        cout << "You have successfully decoded the ancient secret!" << endl;
        cout << "The treasure awaits behind the waterfall!" << endl;
        
        if (strstr(secretMessage, "treasure") != NULL) {
            cout << "BONUS: You have unlocked the Treasure Hunter achievement!" << endl;
        }
        
    } else {
        cout << "Perhaps another time, " << playerName << "." << endl;
        cout << "The ancient secrets will wait for your return..." << endl;
    }
    
    cout << "Thank you for playing The Secret Message Decoder!" << endl;
    cout << "May your adventures continue!" << endl;
    
    return 0;
}