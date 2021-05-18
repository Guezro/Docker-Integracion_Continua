pipeline {
    agent {
        docker {
            image 'python:3.8.5'
            //image 'qnib/pytest'
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

                sh 'pip3 install virtualenv && virtualenv -p venv && source venv/bin/activate && pip3 install xmlrunner && python3 src/test.py -v'
                    
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