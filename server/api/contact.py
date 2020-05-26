# example: POST /api/contact/register-infection.php
# Body: JSON
# {
#    "uuids" : ["00000000-0000-0000-0000-000000000000", "00112233-4455-6677-8899-aabbccddeeff"],
#    "npi" : "1023292927"
# }
# TODO: Determine a more secure way to identify the provider and only register infections from verified providers.


from flask import Flask, request, jsonify
import json

app = Flask(__name__)

class Contact:
    def __init__(self, npi = None, uuids = None):
        self.npi = npi
        self.uuids = uuids

    def registerInfection(self):
        if self.validateNpi():
            # TODO: Save the Contacts
            print(f"self.npi={self.npi}")
            return True
        else:
            return False

    def validateNpi(self):
        # TODO: do an NPI check
        return True



@app.route("/")
def hello():
    return "Hello World!"

@app.route("/api/contact/register-infection/",  methods = ['POST'])
def registerInfection():
    req = request.get_json()
    contact = Contact(req["npi"])
    contact.registerInfection()
    print(req["npi"])
    return jsonify(req) 
    #return json.dumps(req), 200, {'ContentType':'application/json'} 

if __name__ == "__main__":
    app.run(debug=True)