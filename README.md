## Introduction
This project provides a complete walkthrough for developing a full-scale data engineering pipeline. It covers every phase—from collecting data, to processing it, and finally storing it—using a powerful set of tools including Apache Airflow, Python, Apache Kafka, Apache Zookeeper, Apache Spark, and Cassandra. The entire system is containerized with Docker to ensure easy deployment and scalability.


## Getting Started

Follow these steps/ cmds to set up the project locally:

   ```bash
   git clone https://github.com/shivpratikhande/data-streaming.git
   cd data-streaming
   docker-compose up
   ```
   
   


## System Architecture
![image](https://github.com/user-attachments/assets/60b14b95-4edd-4289-b475-efd52f62616c)

## 🛠️ Technology Used

This project leverages a modern data engineering stack to build a complete end-to-end pipeline. Below is a breakdown of the technologies and their roles:

- **Data Source:**  
  [randomuser.me](https://randomuser.me) API is used to generate synthetic user data for ingestion.

- **Apache Airflow:**  
  Handles orchestration of the data pipeline and stores the ingested data into a PostgreSQL database.

- **Apache Kafka & Zookeeper:**  
  Kafka is used for real-time data streaming, while Zookeeper coordinates the Kafka brokers.

- **Control Center & Schema Registry:**  
  These components provide monitoring capabilities and manage schemas for Kafka topics.

- **Apache Spark:**  
  Performs distributed data processing through its master and worker node setup.

- **Cassandra:**  
  Acts as the storage layer for processed data, optimized for scalability and speed.

- **PostgreSQL:**  
  Temporarily holds raw ingested data before it's passed into the streaming pipeline.

- **Docker:**  
  Ensures the entire stack is containerized, making deployment and scaling straightforward.

---

### 📦 Full Tech Stack

- Apache Airflow  
- Python  
- Apache Kafka  
- Apache Zookeeper  
- Apache Spark  
- Cassandra  
- PostgreSQL  
- Docker
