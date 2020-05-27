# example: POST /api/contact/register-infection/
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
        #TODO: save the uuids and the NPI of the provider that recorded the positive test
            #The uuids to be saved should fall in the infections time period based on scientific recommendations
            #infectionType can be use to extend this system to other types of infections: as of 5/25/2020 this system is designed for tracking COVID-19

        #TODO: check NPI with https://npiregistry.cms.hhs.gov/api/?version=2.1&number=<enter-npi-here>
            #test NPI = 1023292927
            #if not found, record in offline location and manually verify
            #if found, publish the uuids publicly.
            #possibly notify the NPI holder that the infection was registered.

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
    try:
        req = request.get_json()
        contact = Contact(req["npi"])
        contact.registerInfection()
        print(req["npi"])
        #return jsonify(req) 
        return json.dumps(req), 201, {'ContentType':'application/json'} 
    except:
        return "{\"message\": \"Data is incomplete\"}", 400, {'ContentType':'application/json'} 
    

if __name__ == "__main__":
    app.run(debug=True)
