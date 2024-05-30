# Brainfuck Compiler

Brainfuck Compiler / IDE is a simple and intuitive Integrated Development Environment (IDE) for writing, running, and debugging Brainfuck code. This application is built using Python with the `customtkinter` library for the GUI and supports multithreading to ensure a responsive user interface.

## Features

- **Code Editor**: A text area to write your Brainfuck code.
- **Execution**: Run your Brainfuck code with the click of a button.
- **Output Display**: View the output of your Brainfuck code.
- **Responsive UI**: Multithreaded execution to keep the interface responsive during long computations.

## Getting Started

### Prerequisites

- Python 3.x
- `customtkinter` library
- `Pillow` library (for handling images)

### Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/Quantamyt/Brainfuck-Compiler.git
   cd brainfuck-compiler
   ```

2. **Install the Required Libraries**:
   ```sh
   pip install customtkinter pillow
   ```

### Running the Application

Execute the following command to start the IDE:
```sh
python brainfuck_ide.py
```

## Usage

1. **Write Code**:
   - Open the IDE and write your Brainfuck code in the text editor.

2. **Run Code**:
   - Click the "Run" button to execute the code. The output will be displayed in the output area below the editor.


## Code Structure

- `brainfuck_ide.py`: The main script containing the application logic and GUI setup.

### Key Functions

- `brainfuck_interpreter(code, input_callback)`: Interprets and executes Brainfuck code.
- `run_brainfuck()`: Retrieves the code from the text editor and runs it in a separate thread.
- `execute_brainfuck(code)`: Executes the Brainfuck code and updates the output display.
- `get_user_input()`: Prompts the user to enter a single character for the Brainfuck ',' command.
- `show_author_info()`: Displays the author information.
- `setup_ui(root)`: Sets up the UI components.

## Screenshots

![Brainfuck Compiler unused](https://raw.githubusercontent.com/Quantamyt/Brainfuck-Compiler/main/assets/image_2024-05-30_220637041.png)

![Brainfuck Compiler Used](https://raw.githubusercontent.com/Quantamyt/Brainfuck-Compiler/main/assets/image_2024-05-30_220738868.png)

## Contributing

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Create a new Pull Request.

## License

This project is licensed under the [NPL](https://choosealicense.com/no-permission/) License.

In short, No Permission from me = No Copying Code from here.

## Contact

Author: [quantam](https://github.com/Quantamyt/)

Discord: quantamphysic
