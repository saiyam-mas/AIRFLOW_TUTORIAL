from airflow.sdk import dag, task
from airflow.operators.bash import BashOperator

@dag(
    dag_id = 'operators_dag'
)
def operators_dag():
    
    @task.python
    def first_task():
        print("This is the first Task")

    @task.python
    def second_task():
        print("This is the second Task")

    @task.bash
    def bash_task_modern():
        return "echo 'https://airflow.apache.org'"

    # Using a built-in operator
    bash_task_traditional = BashOperator(
        task_id = 'bash_task_traditional',
        bash_command = "echo 'https://airflow.apache.org'"
    )

    # Defining task dependencies
    first = first_task()
    second = second_task()
    bash_task_modern = bash_task_modern()
    bash_task_traditional = bash_task_traditional

    first >> second >> bash_task_modern >> bash_task_traditional

# Initilizing the DAG 
operators_dag()