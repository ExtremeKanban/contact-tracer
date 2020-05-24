# contact-tracer
 
This is a thought project to attempt to build a COVID (or any transmissible disease) contact-tracing system with the folowing requirements

1. Anonymous
   - Do not share person identifiable information
   - Do not share location identifiable information
2. Limited Retention
   - Delete any stored data as soon as possible
3. Send as little information as possible
   - Only share anonymous ids and date/time



## Workflow
> Two people with contat-tracing devices are not in range yet to register a potential contact incident.
![Before Contact](/images/before-contact.png)


> As the individuals get close, their devices identify potential contact, and they agree on a contact GUID.  This GUID is stored on both of their devices with the date.
![First Contact](/images/first-contact.png)


>  A third person begins to move toward the group, but the 3 devices have not registered it as a potential contact.
![Incoming Additional Contact Contact](/images/incoming-additional-contact.png)


> The third person is now in range, and the three devices decide this person should be included in the open contact, and share the GUID that was already generated. The third device stores it with the date.
![Additional Contact](/images/additional-contact.png)


> One of the people from the identified contact is diagnosed wtih the infection, and they publish all encounter GUIDs stored on their personal device within the infectious date range determined by their healthcare provider.
![Diagnosis Notification](/images/diagnosis-notification.png)


> Each person is able to check the published lists of GUIDs to see if they have one stored indicating they may have been exposed to the infection.
![Search Contact](/images/search-contact.png)
