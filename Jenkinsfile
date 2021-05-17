pipeline {
    agent none 
    stages {
        stage('Build') { 
            agent {
                docker {
                    image 'python:2-alpine' 
                }
            }
            steps {
                sh 'python -m py_compile src/operaciones.py' 
                stash(name: 'compiled-results', includes: 'src/*.py*') 
            }
        }
        stage('Test') {

            steps {
                sh 'python -m py_compile src/test.py --junit-xml test-reports/results.xml'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
    }
}