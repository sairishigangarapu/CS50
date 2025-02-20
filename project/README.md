# Calculator Application

## Overview
This is a simple yet fully functional GUI calculator application built using Python and Tkinter. The calculator supports basic arithmetic operations such as addition, subtraction, multiplication, and division. Additionally, it includes features like squaring a number and using the mathematical constant π (pi). The interface is designed to be user-friendly with a modern aesthetic.

## Features
- Supports basic arithmetic operations: addition (+), subtraction (-), multiplication (*), and division (/).
- Allows input of decimal numbers.
- Includes a square function (x²) for quick calculations.
- Provides a button for π (pi) for mathematical calculations.
- Displays results in a formatted manner.
- Has a clear (C) button to reset the input.
- Well-organized and styled UI with different button colors for operators, numbers, and special functions.

## Installation
To run this calculator application, ensure you have Python installed on your system. You can install the required libraries using:

```bash
pip install tk
```

## Usage
Run the Python script using the following command:

```bash
python calculator.py
```

Once launched, you can use the buttons on the UI to perform calculations. The input field allows for manual entry as well.

## File Structure
### `calculator.py`
- **GUI Implementation**: Uses Tkinter to create the graphical interface, including buttons and an input display.
- **Functions**:
  - `input_num(digit)`: Handles numerical input.
  - `input_decimal(decimal)`: Allows decimal point input.
  - `input_pie(pie)`: Inserts the value of π.
  - `square()`: Computes the square of the given number.
  - `cal(choice)`: Stores and processes arithmetic operations.
  - `reset()`: Clears the input field and resets all values.
  - `result()`: Computes and displays the final result.

## Design Choices
1. **Tkinter for GUI**: Tkinter is built into Python and provides an easy-to-use interface for GUI development.
2. **Button Colors**: Different colors distinguish operators from numbers for better visibility.
3. **Error Handling**: Ensures division by zero is handled gracefully.
4. **Grid Layout**: Uses a structured grid layout for dynamic UI adjustment.

## Future Enhancements
- Implementing keyboard input support.
- Adding scientific functions like trigonometry, logarithms, and factorial calculations.
- Improving UI aesthetics with additional styling.

## Project Repository
You can find the updated project files on GitHub: [Calculator Project](https://github.com/me50/sairishigangarapu/tree/cs50/problems/2022/python/project)

## Author
**Sai Rishi Gangarapu**
- GitHub: [sairishigangarapu](https://github.com/sairishigangarapu)

---

This project serves as a foundational calculator application using Python's Tkinter library, with potential for expansion into a more advanced scientific calculator in the future. Feel free to contribute and improve upon it!

