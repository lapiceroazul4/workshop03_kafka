# Machine Learning and Data Streaming 

## Description

This workshop is the third one of the ETL course at UAO. It involves simulating a streaming data transmission, where we use Kafka and Python to implement a regression algorithm. For each record that arrives at the Kafka consumer, a prediction is made.

## Prerequisites

Before getting started with this project, make sure you have the following components installed or ready:

- [Apache Kafka](https://kafka.apache.org/)
- [Python](https://www.python.org/)
- [Database (can be local or cloud-based, if it's local I recommend using PostgreSQL)](https://www.postgresql.org/)
- [Docker](https://www.docker.com/)

## Environment Setup

Here are the steps to set up your development environment:

1. **create a virtual enviroment**: Run the following command to create a virtual enviroment called venv:

   ```bash
   python -m venv venv

2. **activate your venv**: Run the following commands to activate the enviroment:

   ```bash
   cd venv/bin
   source activate

  in case you don't have the folder 'bin' go to 'Scripts' Folder

3. **Install Dependencies**: Once you're in the venv run the following command to install the necessary dependencies:

   ```bash
   pip install -r requirements.txt

4. **Create pg_config**: You need to create a json file called "pg_config" with the following information, make sure you replace the values with the correspondent information :

   ```bash
   {
    "user" : "myuser",
    "passwd" : "mypass",
    "server" : "XXX.XX.XX.XX",
    "database" : "demo_db"
   }  

5. **Running docker compose**: Go to the project's folder and run:

- docker-compose up
- docker ps

Open a terminal and enter to the container with: 
- docker exec -it kafka-test bash  

create a new topic

- kafka-topics --bootstrap-server kafka-test:9092 --create --topic kafka_workshop


6. **Run main.py**: At this point everything is ready and you can run:

   ```bash
   python main.py


## Contact

If you have any questions or suggestions, feel free to contact me at [lapiceroazul@proton.me].
