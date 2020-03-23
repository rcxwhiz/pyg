# sag
Squad Automatic Grader

This is a program instructors can use to automatically grade python assignments.
It is going to have a variety of features.

To run this program run main.py

Required packages:
- None yet

To do list:
- Make student code run
- Generate grading criteria (almost done)
- Grade student code based on criteria w/ report
- Create program that can be exported for students
- Transplant (replicate) old UI so that grading summary can be viewed

A major limition of this program so far is that you are running arbitrary student code on your machine. I am taking steps
to try to minimize the danger of this, but I am running this code personally in a smaller, good faith environment. I am
creating a package whitelist and phrase blacklist, and the program already has a configurable time limit on it but I
don't think it is possible to plug all holes (ex. writing large files? etc...)