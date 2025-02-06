# lista-tarefas-app

## Overview
The `lista-tarefas-app` is a task management application built using FastAPI, following the principles of Clean Architecture. The application allows users to create, list, and delete tasks, with data stored in memory for simplicity.

## Project Structure
```
lista-tarefas-app
├── src
│   ├── application
│   │   └── use_cases
│   │       └── index.py
│   ├── domain
│   │   ├── entities
│   │   │   └── index.py
│   │   └── repositories
│   │       └── index.py
│   ├── infrastructure
│   │   └── local_storage
│   │       └── memory.py
│   ├── interface_adapters
│   │   ├── controllers
│   │   │   └── index.py
│   │   └── presenters
│   │       └── index.py
│   └── main
│       └── main.py
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/lista-tarefas-app.git
   cd lista-tarefas-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
To run the application, execute the following command:
```
uvicorn src/main/main:app --reload
```

You can then access the API at `http://127.0.0.1:8000`.

## API Endpoints
- `POST /tasks`: Create a new task.
- `GET /tasks`: Retrieve a list of all tasks.
- `DELETE /tasks/{task_id}`: Delete a task by its ID.

## Dependencies
The project uses the following dependencies:
- FastAPI: A modern, fast (high-performance) web framework for building APIs with Python 3.6+ based on standard Python type hints.
- Uvicorn: A lightning-fast ASGI server implementation, using `uvloop` and `httptools`.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.