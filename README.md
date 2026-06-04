<div align="center">
  <br>
  <h1>📑 Course Catalog Lookup 📑</h1>
</div>

This project reads a dataset of university course listings from a text file and organizes the course information into a dictionary. Each course code is used as a key, and the value stores information such as the course title, description, prerequisites, and credits.

The program allows a user to look up a course by its course code, such as INST126, and return the course title and prerequisites. It also includes a function that finds all courses with no prerequisites by checking each course in the dictionary.

The project also saves the organized course catalog as a JSON file.

<div>
    <h1>Files 🗂</h1>
</div>

- [course_catalog.py](course_catalog.py) — The main Python program.
- [INST-courses-all.txt](INST-courses-all.txt) — The original course catalog dataset.
- [course_index.json](course_index.json) — The saved course index in JSON format.