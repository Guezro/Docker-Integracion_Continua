pipeline {
    agent {
        docker {
            
            image 'qnib/pytest'
            args '-v /root/.m2:/root/.m2' 
        }
    }
    stages {
        stage('Build') { 
            steps {
                sh 'python --version' 
                sh 'virtualenv venv && . venv/bin/activate && pip install unittest-xml-reporting'
            }
        }
        stage('TestApp'){
            steps {
                
                sh 'python src/test.py -v'     
            }

        }
        stage('RunApp'){
            steps {
                sh 'python src/operaciones.py'
            }
        }

    }
    triggers {
        githubPush() 
    }
}