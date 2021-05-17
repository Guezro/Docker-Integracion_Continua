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
                sh 'python --version' 
                sh '''
                pip install virtualenv
                virtualenv enviroment_name -p python3
                source enviroment_name/bin/activate
                pip install xmlrunner 
                
                '''
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