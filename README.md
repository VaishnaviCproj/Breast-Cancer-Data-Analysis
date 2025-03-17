# Automated Breast Cancer Prediction Pipeline Using Apache Airflow, SQL Server, and Power BI

### Project Overview
This project automates the end-to-end data processing, machine learning model training, and visualization of the Wisconsin Breast Cancer Dataset using Apache Airflow, SQL Server, and Power BI.

- **Data Cleaning & Preparation**: Airflow DAGs clean the dataset, handling missing values and duplicates before storing the processed data in a mounted folder.
- **Model Training & Prediction**: A Jupyter notebook, triggered by Airflow, reads the cleaned dataset and trains a Logistic Regression model. It then generates diagnosis predictions and probability scores, which are stored in SQL Server for further analysis.
- **Data Visualization**: A Power BI dashboard provides interactive insights into feature trends, model performance, and risk evaluation with various ML evaluation metrics.

---

### Skills
- **Data Engineering & Automation**: Apache Airflow, SQL Server, Docker
- **Machine Learning**: Logistic Regression, Model Evaluation (Precision, Recall, ROC Curve, Confusion Matrix)
- **Database Management**: SQL Server Configuration, Remote Connectivity, Data Storage & Retrieval
- **Visualization & Analytics**: Power BI, Python (Matplotlib, Seaborn, Scikit-learn)

---

### Key Contributions

**End-to-End Automated Data Pipeline**:
- Developed an Airflow DAG to clean the dataset, check for duplicates, and store it in a mounted folder for access.
- Triggered Jupyter Notebook execution via Airflow to automate model training and inference.

**Machine Learning Model Implementation**:
- Trained a Logistic Regression model on the cleaned dataset to predict whether a tumor is Benign (B) or Malignant (M).
- Stored predictions and probability scores in SQL Server to support model evaluation.

**Power BI Dashboard for Model Insights**:
- Designed an interactive dashboard featuring: 
  - **Feature Impact Analysis**: Visualizing the influence of selected features on diagnosis.
  - **Model Performance Metrics**: Accuracy, Precision, Recall.
  - **Confusion Matrix**: Showing misclassification rates.
  - **ROC Curve**: Providing insights into model classification effectiveness.
- Ensured the ROC Curve and Confusion Matrix remained independent of user filters, preserving model integrity.

---

### Results and Impact

- Seamless integration of Machine Learning, Data Engineering, and Business Intelligence, making predictive insights accessible to non-technical users.
- Automated model training and retraining for adaptability to new data without manual intervention.
- Demonstrated real-world applications of an ML-powered analytics dashboard in healthcare, aiding in early breast cancer detection.

---

### Learnings and Takeaways

- **End-to-End ML Deployment**: Developed expertise in data pipelines, automation, and model evaluation.
- **Airflow & SQL Server Integration**: Configured Docker-based SQL Server with Airflow for remote access, solving connectivity challenges.
- **Power BI Model Evaluation**: Explored ML model performance visualization, ensuring stakeholders can interpret results effectively.
- **Optimized Data Flow**: Implemented feature selection and filter-based insights, improving usability and relevance of data visualizations.

---

### Steps to Replicate the Project

1. **Set up Docker on your machine**.
2. **Install Apache Airflow on Docker** by following steps given here: [Apache Airflow Docker Setup](https://airflow.apache.org/docs/apache-airflow/stable/howto/docker-compose/index.html).
3. **Set up SQL Server on your machine**.
4. **Take the `requirements.txt`, `Dockerfile`, and `.env` file from my repo** and place them in the directory where Airflow files are present on your machine.
5. **Create a `data` folder** in the Airflow directory.
6. **Update the `docker-compose.yaml` file from airflow so that it can use `Dockerfile`** to build the containers.
7. **Mount the `data` folder by editing `docker-compose.yaml`.**
8. **Place the `breast_cancer_data` folder from this repo** in the `data` folder.
9. **Place the `DataIngest.py` file in the `dags` folder in the airflow directory.**
10. **Make sure to edit `credentials.json` file in breast_cancer_data folder with your DB details**
11. **Create the Docker containers** to get your Airflow running.
12. **Create a database in SQL Server** where your breast cancer data will be placed.
13. **Run the Airflow DAG** using the command prompt or Airflow Webserver's UI.
14. **Your data will be loaded into SQL Server**. You can use that to create a dashboard. You can take a look at the pdf file of my dashboard to get an idea of how to place the elements.

