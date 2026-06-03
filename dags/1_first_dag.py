from airflow.sdk import dag, task

@dag(
    dag_id = 'first_dag'
)
def first_dag():
    
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
first_dag()