# Digitized security recordings application
The project is developed in **C++** and it also uses **QT framework**.

The application contains a list of Recordings(title, location, timeOfCreation, timesAccessed, footagePreview) and it has various functionalities that use these recordings.

The project has the following functionalities:
- it has 2 modes: mode A and mode B
- mode A:
  - CRUD operations fro recordings;
  - list regordings;
  - undo / redo operations;
- mode B:
  - it has a watch list that contains only certain recordings;
  - add a new recording from the main list to watch list;
  - filter watch list;
  - open watch list in TableView (a new widget with the watch list as a table is opened)
  - open the watch list in a HTML file;
- I implemented my own exceptions;

The application uses the **Observer pattern** and the **MVC design pattern**.
