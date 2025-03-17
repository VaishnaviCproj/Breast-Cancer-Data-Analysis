FROM apache/airflow:2.10.5

# Set user to root to install system dependencies
USER root

# Install ODBC Driver 17 for SQL Server
RUN apt-get update && \
    apt-get install -y curl gnupg2 unixodbc unixodbc-dev && \
    curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - && \
    curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/mssql-release.list && \
    apt-get update && \
    ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Switch back to airflow user to install Python dependencies
USER airflow

# Add requirements.txt to container
ADD requirements.txt .

RUN pip install apache-airflow==${AIRFLOW_VERSION} -r requirements.txt
