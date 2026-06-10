from airflow.sdk import dag, task
from pendulum import datetime

@dag(
    dag_id = 'first_schedule_dag',
    start_date = datetime(year=2026, month=6, day=1, tz="EST"),
    schedule = "@daily",
    is_paused_upon_creation=False,
    catchup=True
)
def first_schedule_dag():
    
    @task.python
    def first_task():
        print("This is the first Task")

    @task.python
    def second_task():
        print("This is the second Task")

    @task.python
    def third_task():
        print("This is the third Task")

    # Defining task dependencies
    first = first_task()
    second = second_task()
    third = third_task()

    first >> second >> third

# Initilizing the DAG 
first_schedule_dag()