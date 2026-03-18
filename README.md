# ProjectInCloud

This is a Flask API for managing a task list.

## Installation

Install the dependencies:

```bash
pip install -r requirements.txt
```

## Running the API

Run the application:

```bash
python app.py
```

The API will be available at http://localhost:5000

## Endpoints

- GET /tasks: Retrieve all tasks
- POST /tasks: Create a new task (JSON: {"title": "Task title", "description": "Optional description"})
- PUT /tasks/<id>: Update a task (JSON: {"title": "...", "description": "...", "done": true/false})
- DELETE /tasks/<id>: Delete a task

## Example Usage

Use curl or Postman to test the endpoints.

Example POST:

```bash
curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"title": "Buy groceries"}'
```