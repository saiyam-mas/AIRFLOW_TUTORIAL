from airflow.sdk import dag, task
from pendulum import datetime, duration
from airflow.timetables.trigger import DeltaTriggerTimetable

@dag(
    dag_id = 'delta_schedule_dag',
    start_date = datetime(year=2026, month=6, day=1, tz="EST"),
    end_date = datetime(year=2026, month=6, day=10, tz="EST"),
    schedule = DeltaTriggerTimetable(duration(days=3)),
    is_paused_upon_creation=False,
    catchup=True
)
def delta_schedule_dag():
    
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
delta_schedule_dag()