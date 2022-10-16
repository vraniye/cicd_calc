pipeline {
    agent {
        docker {
            image 'python:3.10.3'
        }
    }
    environment {
        HOME = "${env.WORKSPACE}@tmp"
        BIN_PATH = "${HOME}/.local/bin/"
    }
    stages {
        stage('Git Clone') {
            steps {
                git changelog: false, url: "http://gitlab.devops.ru/vraniye/tornado-calculator.git"
            }
        }
        stage('Prepare') {
            steps {
                sh 'python --version'
                sh 'pip install virtualenv'
                sh "${BIN_PATH}virtualenv venv"
                sh 'bash -c "source venv/bin/activate"'
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps{
                sh 'python -m unittest discover -s "./tests" -p "test_main.py"'
                sh "${BIN_PATH}flake8 ."
            }
        }
    }
}
