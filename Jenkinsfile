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
                
            }
        }
        stage('TestApp'){
            steps {
                sh 'virtualenv venv && . venv/bin/activate && pip install unittest-xml-reporting'
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