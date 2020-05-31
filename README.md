# Anonymous Contact Tracing System - Proof of Concept
## About
This project exists to attempt to design a contact-tracing system that works without using any personally identifiable information including location data.  

### Why
In the time of the COVID-19 outbreak, we are looking for ways to slow the spread through targetted testing (testing individuals we are "likely" to have COVID-19). Those who are most likely to be infected have been near someone who was infected.  This reality has lead to two types of contact tracing:
1. Interviewing of those with infections to attempt to determine and contact anyone who may have been near them during their time of infection.
2. Building GPS bound applications running on mobile phones to track interactions.

Some problems with the Interview process are: 
- You must identify individuals and that information is then used by third parties. This is information that could be used for other purposes and potentially dangerous to individual liberty.
- The person who is infected and needs to be interviewed must remember who/where they were.  If this person is incapacitated, this system does not work.

Some problems with the mobile phone based applications are:
- Mobile phones contain a lot of personal information that could be linked to the contact-tracing information and be potentially dangerous to individual liberty
- These applications could track individuals that did not even opt-into the contact-tracing system.

## Guidelines 

1. Anonymous
   - Do not share person identifiable information
   - Do not share location identifiable information
   - Do not expose devices to a larger network (phone, computer, etc.) without direct intervention by the user of the device.
2. Limited Retention
   - Delete any stored data as soon as possible
3. Send as little information as possible
   - Only share anonymous ids and date/time
4. Follow CDC contact tracing guidelines
   - [https://www.cdc.gov/coronavirus/2019-ncov/php/principles-contact-tracing.html](https://www.cdc.gov/coronavirus/2019-ncov/php/principles-contact-tracing.html)



## Workflow
![Before Contact](/images/before-contact.png)
> Two people have opted into carrying contact-tracing devices.  These devices are using low powered radio signals from Bluetooth radios to transmit a UUID in a constant flow.  The devices are also listening for incoming UUIDs from other devices. The two in this scenario are not in range yet to register a potential contact incident.


![First Contact](/images/first-contact.png)
> As the individuals get close, their devices identify potential contact.  The devices each record the other's UUID


![Incoming Additional Contact Contact](/images/incoming-additional-contact.png)
>  A third person begins to move toward the group, but the 3 devices have not registered it as a potential contact.


![Additional Contact](/images/additional-contact.png)
> The third person is now in range.  The first two devices record the UUID of the third device.  The third device records the UUIDs of both the first and second device.  At this point, all three devices have the UUIDs of the other devices stored.


![Diagnosis Notification](/images/diagnosis-notification.png)
> One of the people from the identified contact is diagnosed wtih the infection, and they publish all encounter UUIDs stored on their personal device within the infectious date range determined by their healthcare provider.


![Search Contact](/images/search-contact.png)
> Each person can check the published lists of UUIDs to see if any of their IDs show up.  If found, they can either go to a healthcare provider for testing, self-quarantine, or do nothing at all.  The ultimate intention is to allow the person who may have been in contact to use the information as they see fit and know that no one else knows they were personally potentially exposed.


## How
Using BBC micro:bit devices.  These devices are easy for prototyping which should get this system in a live testing phase quickly.  They are also inexpensive (US $15 - $20) and can be ordered from several distributors around the world.

The challenges of the devices are that they cannot generate UUIDs. They do have unique-ish hardware ids, but allowing for randomized ids requires user intervention and make the use slightly more complicated to give better anonymity.  The devices also do not have a builtin clock, so tracking the dates where contacts were recorded also involves human interaction.  If the user doesn't keep track of when the device recorded a contact, they won't be able to accurately publish that interaction as having been in the infectious window.
