# Basic-To-Do-App

## Overview
To-Do App Basic is a simple yet powerful task management tool designed to help users organize their day-to-day activities efficiently. Built with Django, JavaScript, jQuery, and SQLite, it offers a user-friendly interface with essential features for managing tasks.

### Demo Video

https://github.com/johurul000/Basic-To-Do-App/assets/90057499/d3d56a9e-fdc2-449d-9e8c-9b62861bc283



## Key Features
1. **Add Task**: Easily add new tasks to your to-do list.
2. **Edit Task**: Modify existing tasks as your priorities change.
3. **Delete Task**: Remove completed or irrelevant tasks from your list.
4. **Popup Forms**: Convenient forms for adding and editing tasks, enhancing user experience.

## Technology Stack
- **Backend**: Django
- **Frontend**: JavaScript, jQuery
- **Database**: SQLite

## Installation

To set up the To-Do App Basic on your local machine, follow these steps:

1. **Clone the Repository**
   ```bash
   git clone [repository-url]
   cd [repository-name]
   ```

2. **Set Up a Virtual Environment** (Optional but recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Get in src dir**
   ```bash
   cd src
   ```

5. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Start the Server**
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser.

## Project Structure
- `home.html`: The main HTML file.
- `Task`: Model in `models.py` for storing tasks.
- `TaskForm`: Django form in `forms.py` for CRUD operations.
- **AJAX Calls**:
  - `addTask`
  - `editTask`
  - `deleteTask`
  - `updateTaskStatus`

## Contributing
Contributions to To-Do App Basic are welcome! Whether it's bug fixes, feature requests, or improvements to the documentation, your assistance is appreciated. Please follow the standard fork-and-pull request workflow.
