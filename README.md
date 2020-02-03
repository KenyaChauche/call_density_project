# Call Density Identification for Camano Island Fire Department
#### Hack-a-thon for General Assembly Data Science Immersive, Seattle Chapter
#### February 2020

## Purpose
The Camano Island Fire Department would like to be able to identify when they are receving multiple emergency calls at a time and determine time frames when they need to have more staff on hand.  The department has excel spreadsheets with call data, but needs to be able to get useful information from the data.  The department has Excel and Tableau, but not Python, to work their data.  The department would like to be able to use their same excel format as an input, and get an output that, when used with Tableau, creates visuals that identify busy periods.

## Program


## Implementation
The user is starting with an excel spreadsheet of the previous month's call data.  The user will use the command line to enter the file name, the new file name, and the destination for the new file.  After doing this, Pyinstaller will use the overlap function and num_overlaps function to create two new columns.  The overlap column displays a set of call IDs that overlap each original call.  The num_overlaps column gives the number of call that overlap each original call.  Once these columns are created and added to the dataframe, it is saved as the new excel spreadsheet, in the destination that was identified by the user at the beginning of the process.  The document is ready to be utilized for Tableau to create visuals.


## Credits
This project was produced by Kenya Chauche, Chris Corliss, Patrick Hubbel, Richard Samuelson, and Stephen Schott with supervision by Charles Rice. Project originally hosted on General Assembly GitHub Enterprise accounts, posted publicly with permission. 
