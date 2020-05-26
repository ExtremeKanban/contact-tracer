<?php
Class Contact 
{
    // database connection
    private $conn;

    public $uuids;
    public $npi;
    public $registeredDate;
    public $infectionType = "COVID-19";
    public $message;

    //constructor
    public function __construct($db){
        $this->conn = $db;
    }

    public function registerInfection()
    {
        //TODO: save the uuids and the NPI of the provider that recorded the positive test
            //The uuids to be saved should fall in the infections time period based on scientific recommendations
            //infectionType can be use to extend this system to other types of infections: as of 5/25/2020 this system is designed for tracking COVID-19

        //TODO: check NPI with https://npiregistry.cms.hhs.gov/api/?version=2.1&number=<enter-npi-here>
            //test NPI = 1023292927
            //if not found, record in offline location and manually verify
            //if found, publish the uuids publicly.
            //possibly notify the NPI holder that the infection was registered.

        if($this->npi > 0 )
        {
            $this->message = "Infection registered with the provider NPI " . $this->npi . " and " . count($this->uuids) . " Contact Events.";
            return true;
        }
        else
        {
            $this->message = "NPI if not valid, the infection was not registered.";
            return false;
        }

        
    }

    public function findContact()
    {
        //TODO: look for recorded infections with the set array of uuids
            //return true if found, else false
        return false;

    }
}
?>