# BBC micro:bit implementation of the contact-tracer system

This allows multiple microbits to find each other via the Radio, and store the UUIDs transmitted to a file stored locally.

## Installation
1. Flash main.py to a microbit via micropython
   - (Recommended) Use the open source MU Editor: https://codewith.mu/
   - This can be done with the online editor: https://python.microbit.org/v/2.0
2. Update the contents of UUID.txt with a valid GUID/UUID
   - Use MU editor because this cannot be done from the web microbit editor
   - You can generate a UUID at: https://www.uuidtools.com/

## incomplete
The contents of the file can then be uploaded to the server API for broadcasting
