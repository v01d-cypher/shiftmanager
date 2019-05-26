# shiftmanager

### Notes:

Project - Rosters, Application - Shiftmanager.

Dev setup:
`pip install -U pip Django djangorestframework pscycopg2`

Model objects can be interacted with via Admin interface or REST API.

 - `http://127.0.0.1/admin`

Or

 - `http://127.0.0.1/shiftmanager/api/employee`
 - `http://127.0.0.1/shiftmanager/api/shift`
 - `http://127.0.0.1/shiftmanager/api/roster`

Upload CSV files with basic validation:

 - `http://127.0.0.1/shiftmanager/upload`


### Additional Design:

 - Use an existing importer package. I looked at django-import-export, django-adapters.
 - Don't load duplicate shift definitions. Store available number of shift types and allocate them with a count to check availability.
 - Extend custom "through" model for things besides site location, eg. employee role, renumeration, etc.
 - Use asyncio to manage long running processes and calls to external optimisation engine. Frontend will be notified via trigger/message/subscription, whichever works better.
 - Automate uploads of CSV data to database on a schedule
 - Notify employees of their shift assignments via email.

### Many more things required for app:

 - Session management
 - User authentication and authorisation for access, upload and managing data
 - Better validation of CSV data
 - Tests
 - Frontend in REACT :-)

### Questions for rosterer:

 - Will there be different files for the different sites?
 - How can we uniquely identify the employees?
 - How often will new data require uploading?
 - Will the file format (columns, dates) change?
 - Do you require any basic reporting or notification emails?
 - Who can access what?
