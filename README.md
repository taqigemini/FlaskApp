# FlaskApp

FlaskApp is a simple web application built using the Flask framework that allows users to manage a list of items. It provides basic CRUD (Create, Read, Update, Delete) functionality.

## Features

- **Create**: Add new items to the list.
- **Read**: View the list of items.
- **Update**: Modify existing items.
- **Delete**: Remove items from the list.

## Technologies Used

- **Flask**: A micro web framework written in Python.
- **HTML**: For rendering the templates.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/taqigemini/FlaskApp.git
    ```

2. Navigate to the project directory:

    ```bash
    cd FlaskApp
    ```

3. Set up a virtual environment:

    ```bash
    python3 -m venv venv
    ```

4. Activate the virtual environment:

    - For **Windows**:

      ```bash
      venv\Scripts\activate
      ```

    - For **Mac/Linux**:

      ```bash
      source venv/bin/activate
      ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

    If you don't have a `requirements.txt` file, you can manually install Flask using:

    ```bash
    pip install Flask
    ```

## Running the Application

To start the Flask development server, run the following command:

```bash
python app.py
