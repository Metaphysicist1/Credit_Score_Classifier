## Credit Score Classifier



![credit-score-architecture (3)](https://github.com/user-attachments/assets/efc013f6-9bcd-48a0-800b-477789d31676)




* Web App where you can enter customers parameters and get credit scoring result 

1. **Machine Learning**
   - Implementation of XGBoost
   - Model training and evaluation
   - Classification of high and low risk customers 

2. **FastAPI Backend**
   - RESTful API development with FastAPI
   - Request/response handling
   - Model serving endpoints

3. **PostgreSQL Database**
   - Database setup and configuration
   - CRUD operations implementation
   - Data persistence for ML models
   - Query optimization

4. **Containerization with Docker**
   - Dockerfile creation
   - Container orchestration
   - Multi-container applications with docker-compose
   - Environment configuration

5. **CI/CD with GitHub Actions [IN Progress]**
   - Automated testing pipeline
   - Continuous integration workflow
   - Automated deployment
   - Code quality checks

The project demonstrates a production-ready ML system with automated testing, containerized deployment, and scalable database operations.

## Project Setup and Running Instructions


1. **Python**: Ensure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Virtual Environment**: It's recommended to use a virtual environment to manage dependencies. You can create one using `venv` or `virtualenv`.

3. **Docker** (Optional): If your project uses Docker, ensure Docker is installed and running on your machine. You can download it from [docker.com](https://www.docker.com/products/docker-desktop).

### Setup Instructions

##### Build project using Docker container 

   For pulling use this command
   ```bash
   docker pull https://hub.docker.com/repository/docker/metaphysicist/credit-score-classifier/general
   ```
   For running use this command
   ```bash
   docker run -it -p 8000:8000 metaphysicist/credit-score-classifier
   ```
##### Build project using Git locally 

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/yourproject.git
   cd yourproject
   ```

2. **Create and Activate a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

### Running the Project

1. **Run the Application**

   If using FastAPI with Uvicorn, you can start the server with:

   ```bash
   uvicorn app.api.endpoints.prediction:router --reload
   ```

   This will start the server on `http://127.0.0.1:8000`.

2. **Access the API**

   Open your browser or use a tool like `curl` or Postman to interact with the API at `http://127.0.0.1:8000`.

### Docker Instructions (Optional)

1. **Build the Docker Image**

   ```bash
   docker build -t yourproject .
   ```

2. **Run the Docker Container**

   ```bash
   docker run -p 8000:8000 yourproject
   ```

### Additional Information

- **Database Setup**: If your project uses a database, ensure it is set up and running. Update the database connection settings in your configuration files as needed.
- **Environment Variables**: Set any necessary environment variables, such as API keys or database URLs, before running the application.

### Troubleshooting

- If you encounter issues, check the logs for error messages.
- Ensure all dependencies are installed and up-to-date.
- Verify that your virtual environment is activated when running commands.
