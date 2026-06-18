from airflow.sdk import dag, task
from pendulum import datetime
from airflow.timetables.interval import CronDataIntervalTimetable

@dag(
    schedule = CronDataIntervalTimetable("@daily", timezone="EST"),
    start_date = datetime(year=2026, month=6, day=15, tz="EST"),
    end_date = datetime(year=2026, month=6, day=30, tz="EST"),
    catchup=True
)
def incremental_load_dag():

    @task.python
    def incremental_data_fetch(**kwargs):
        date_interval_start = kwargs['data_interval_start']
        date_interval_end = kwargs['data_interval_end']
        print(f"Fetching data from {date_interval_start} to {date_interval_end}")

    @task.bash
    def incremental_data_process():
        return "echo 'Incremental load processing from {{ data_interval_start }} to {{ data_interval_end }}'"

    data_fetch = incremental_data_fetch()
    data_process = incremental_data_process()

    data_fetch >> data_process

# Initilizing the DAG
incremental_load_dag()
