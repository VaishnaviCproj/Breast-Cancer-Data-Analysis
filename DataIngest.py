from airflow import DAG
from airflow.operators.python import PythonOperator
import papermill as pm
import pandas as pd
import datetime

# File Paths (Update these paths)
RAW_FILE_PATH = r"/opt/airflow/data/breast_cancer_data/wdbc.data"
CLEANED_FILE_PATH = r"/opt/airflow/data/breast_cancer_data/breast_cancer_data_cleaned.csv"
JUPYTER_NOTEBOOK_PATH = r"/opt/airflow/data/breast_cancer_data/breast_cancer_data_ml.ipynb"
OUTPUT_NOTEBOOK_PATH = r"/opt/airflow/data/breast_cancer_data/breast_cancer_data_ml_output.ipynb"

def extract_and_clean_data():
    BREAST_CANCER_COLUMNS = [
        'id', 'diagnosis',
        'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 'smoothness_mean',
        'compactness_mean', 'concavity_mean', 'concave_points_mean', 'symmetry_mean',
        'fractal_dimension_mean', 'radius_se', 'texture_se', 'perimeter_se', 'area_se',
        'smoothness_se', 'compactness_se', 'concavity_se', 'concave_points_se', 'symmetry_se',
        'fractal_dimension_se', 'radius_worst', 'texture_worst', 'perimeter_worst', 'area_worst',
        'smoothness_worst', 'compactness_worst', 'concavity_worst', 'concave_points_worst',
        'symmetry_worst', 'fractal_dimension_worst'
    ]

    # Read dataset
    df = pd.read_csv(RAW_FILE_PATH, header=None)
    df.columns = BREAST_CANCER_COLUMNS

    # Handle missing values
    df["diagnosis"].fillna(df["diagnosis"].mode()[0], inplace=True)

    numerical_columns = BREAST_CANCER_COLUMNS[2:]  # All numerical columns except 'id' and 'diagnosis'
    skewed_columns = ['concavity_worst', 'symmetry_worst']

    for col in numerical_columns:
        if col in skewed_columns:
            df[col].fillna(df[col].median(), inplace=True)
        else:
            df[col].fillna(df[col].mean(), inplace=True)

    # Remove duplicates
    df = df.drop_duplicates()

    # Save cleaned data
    df.to_csv(CLEANED_FILE_PATH, index=False)

def trigger_notebook():
    pm.execute_notebook(
        JUPYTER_NOTEBOOK_PATH,
        OUTPUT_NOTEBOOK_PATH,
        kernel_name="python3"
    )

# Default DAG arguments
default_args = {
    'owner': 'airflow',
    'start_date': datetime.datetime(2025, 3, 1),
    'retries': 1,
    'retry_delay': datetime.timedelta(minutes=1),
}

# Define DAG
dag = DAG(
    dag_id='load_transformed_to_sql',
    default_args=default_args,
    schedule='@daily',  # Updated to use modern syntax
    description='Breast Cancer Data Processing Pipeline',
    catchup=False
)

# Define Tasks
extract_clean_task = PythonOperator(
    task_id='extract_and_clean_data',
    python_callable=extract_and_clean_data,
    dag=dag,
)

trigger_notebook_task = PythonOperator(
    task_id="trigger_notebook",
    python_callable=trigger_notebook,
    dag=dag
)

# Set Task Dependencies
extract_clean_task >> trigger_notebook_task
