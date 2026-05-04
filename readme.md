Here is the README focusing specifically on the syntax and structure of the commands used in your code:

***

# PyQt5 Layouts Syntax Guide

This document explains the code structure and the specific syntax of the methods used in the script.

### 1. Imports
```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QHBoxLayout, QVBoxLayout
```
*   `import sys`: Imports the Python system-specific parameters and functions module, used here for command-line arguments and exit management.
*   `from ... import ...`: Calls the necessary classes for building the user interface (the application, base window, buttons, and three layout types) from the PyQt5 library.

### 2. Application Initialization
```python
app = QApplication(sys.argv)
```
*   `QApplication()`: The class that manages the GUI application's control flow and main settings.
*   `sys.argv`: Passes command-line arguments to the `QApplication` as input (a syntax requirement in PyQt).

### 3. Window Configuration
```python
window = QWidget()
window.setWindowTitle("Title")
window.resize(width, height)
window.setLayout(layout)
window.show()
```
*   `QWidget()`: Instantiates a base user interface object, which acts as an independent window in this context.
*   `.setWindowTitle(str)`: Takes a string argument and sets it as the title of the window.
*   `.resize(w, h)`: Takes two integer arguments to change the window dimensions based on width (`w`) and height (`h`) in pixels.
*   `.setLayout(obj)`: Assigns (sets) the created layout object to the window.
*   `.show()`: Instructs the operating system to render and display the window on the screen.

### 4. Layouts Syntax
#### A) Grid Layout
```python
grid_layout = QGridLayout()
grid_layout.addWidget(widget, row, column)
```
*   `QGridLayout()`: Creates a matrix-based layout object.
*   `.addWidget(obj, r, c)`: The method to add a widget. In a grid layout, it requires the widget object, the row index (`r`), and the column index (`c`). (Indices start at $0$, e.g., cell $0, 0$).

#### B) Horizontal and Vertical Layouts
```python
hbox_layout = QHBoxLayout()
vbox_layout = QVBoxLayout()
layout.addWidget(widget)
```
*   `QHBoxLayout()` / `QVBoxLayout()`: Create horizontal and vertical layout objects, respectively.
*   `.addWidget(obj)`: In these two layouts, this method only takes the widget object as a parameter and appends it sequentially (from left-to-right or top-to-bottom).

### 5. Widget Creation
```python
QPushButton("Text")
```
*   `QPushButton(str)`: Creates a button object and displays the passed string as the label on the button. In this code, the buttons are instantiated directly inside the parameter of the `.addWidget()` method.

### 6. Execution Loop
```python
sys.exit(app.exec())
```
*   `app.exec()`: Starts the main Event Loop in PyQt. This command keeps the application alive and waiting for user interaction.
*   `sys.exit()`: Receives the exit code from `app.exec()` and instructs Python to terminate the program and release system resources safely.