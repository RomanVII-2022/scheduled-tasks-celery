# scheduled-tasks-celery
## Steps to Run The Project
1. Clone the repository to your local directory.
2. Create a virtual environment.
   
        python -m venv virt

3. Activate the virtual environment.

        source virt/bin/activate

4. Install all the project dependencies.

        pip install -r requirements.txt

5. Run the project. Write the following commands in different terminals.

        python manage.py runserver
        celery -A myproject worker -l INFO
        celery -A myproject beat -l INFO

      

