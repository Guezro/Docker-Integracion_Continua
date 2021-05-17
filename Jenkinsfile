pipeline {
    agent {
        docker {
            image 'python:3.8.5' 
            args '-v /root/.m2:/root/.m2' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                sh '/usr/local/bin/python -m pip install --upgrade pip'
                sh 'python --version' 
                sh 'pip install -r unittest-xml-reporting'
            }
        }
        stage('TestApp'){
            steps {
                
                sh 'python3 src/test.py -v'     
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