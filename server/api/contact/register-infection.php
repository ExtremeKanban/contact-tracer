<?php
//TODO: Determine a more secure way to identify the provider and only register infections from verified providers.

/*
example: POST /api/contact/register-infection.php
Body: JSON
{
    "uuids" : ["00000000-0000-0000-0000-000000000000", "00112233-4455-6677-8899-aabbccddeeff"],
    "npi" : "1023292927"
}
*/


// required headers
header("Access-Control-Allow-Origin: *");
header("Content-Type: application/json; charset=UTF-8");
header("Access-Control-Allow-Methods: POST");
header("Access-Control-Max-Age: 3600");
header("Access-Control-Allow-Headers: Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With");
  
// get database connection
include_once 'database.php';
  
// instantiate contact object
include_once 'contact.php';
  
$database = new Database();
$db = $database->getConnection();


$contact = new Contact($db);

// get posted data
$data = json_decode(file_get_contents("php://input"));
  
// make sure data is not empty
if(
    !empty($data->uuids) &&
    !empty($data->npi) 
){
  
    //set contact values
    $contact->uuids = $data->uuids;
    $contact->npi = $data->npi;
    $contact->registeredDate = date('Y-m-d');

    //register the infection
    if($contact->registerInfection())
    {
        //201 - created
        http_response_code(201);
        echo json_encode(array("message" => $contact->message));
    }
    else
    {
        //503 - service unavailable
        http_response_code(503);
        echo json_encode(array("message" => $contact->message));
    }
}
  
// tell the user data is incomplete
else{
  
    //400 - bad request
    http_response_code(400);
    echo json_encode(array("message" => "Data is incomplete."));
}
?>