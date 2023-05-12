Banker's Algorithm

Requirements
Python 3.x
PyQt5
Usage
To use the application, run main.py in your terminal or IDE. This will launch the GUI window where you can enter the required data.

File Structure
The project consists of six UI files and one main Python file as follows:

window1.ui: First window of the application that allows the user to enter the number of processes and resources.

window2.ui: Second window of the application that allows the user to enter the allocated resources for each process.

window3.ui: Third window of the application that allows the user to enter the maximum resources for each process.

window4.ui: Fourth window of the application that displays the available and need resources for each process.

window5.ui: Fifth window of the application that displays the needed and available resources and allows the user to move on to the next step in the calculation.

window55.ui: Sixth window of the application that displays the output of the calculation.

final5.py: Python file that contains the implementation of the UI for the fifth window.

final55.py: Python file that contains the implementation of the UI for the sixth window.

main.py: Python file that launches the GUI window and handles the interactions between the different windows.

Implementation Details
Each UI file defines the layout of the window and sets up the necessary widgets and buttons.
The main.py file launches the GUI window and handles the interactions between different windows.
Data entered by the user is collected and passed on to the next window using functions defined in each UI file.
The Banker's algorithm is implemented in a function defined in main.py.
The output of the calculation is displayed in the sixth window using a label and a line edit widget.
Conclusion
This project provides a simple implementation of the Banker's algorithm using PyQt5 for the GUI. It can be used as a reference for building similar resource allocation and deadlock avoidance algorithms.
screeenshots

![capture1](https://github.com/StarSage1/banker-s-algorithm/assets/129214435/f8e7cfc6-3bd0-41bc-92cd-eeee75beedc1)
![capture2](https://github.com/StarSage1/banker-s-algorithm/assets/129214435/e8fdf61c-4fbd-40cf-81d3-9697610f464f)![capture3](https://github.com/StarSage1/banker-s-algorithm/assets/129214435/ea26df21-bf8e-4b05-b2b9-ca5043541b80)
![capture3](https://github.com/StarSage1/banker-s-algorithm/assets/129214435/e06e1272-4c6e-49da-8164-450d8a153489)
![capture4](https://github.com/StarSage1/banker-s-algorithm/assets/129214435/aeb29dc2-df86-49b5-a977-312ff5860676)

