from airflow.sdk import dag, task
from pendulum import datetime
from airflow.timetables.trigger import CronTriggerTimetable

@dag(
    dag_id = 'cron_schedule_dag',
    start_date = datetime(year=2026, month=6, day=8, tz="EST"),
    end_date = datetime(year=2026, month=6, day=10, tz="EST"),
    schedule = CronTriggerTimetable("0 16 * * MON-FRI", timezone="EST"),
    is_paused_upon_creation=False,
    catchup=True
)
def cron_schedule_dag():
    
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
cron_schedule_dag()