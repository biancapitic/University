# Movie Rental

This is a Python project which has the functionalities for renting one or more movies by some customers.
It has the following functionalities:
- CRUD operations for these lists: movies, clients and rentals;
- a client can rent or return one or more movies;
- search for a movies/clients by any of their fields;
- get statistic data:
  - find the most rented movies;
  - find the most active clients;
  - show all movies that are still not returned and their returned date has passed already;
- unlimited undo/redo operations implemented in a memory efficient way;

This project uses the layered architecture pattern. It has PyUnit tests and it can store the data in 3 ways: text, binary or memory.
