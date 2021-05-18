pipeline {
    agent {
        docker {
            image 'python:3.8.5'
            image 'qnib/pytest'
            args '-v /root/.m2:/root/.m2' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                sh 'python3 --version' 
                
            }
        }
        stage('TestApp'){
            steps {
                sh 'virtualenv venv && . venv/bin/activate && pip install xmlrunner && python3 src/test.py -v'
                    
            }

        }
        stage('RunApp'){
            steps {
                sh 'python3 src/operaciones.py'
            }
        }

    }
    triggers {
        githubPush() 
    }
}