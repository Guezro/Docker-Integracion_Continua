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
            }
        }
        stage('Test'){
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                }
            }
            steps {
                sh 'mvn test'
            }
        }
    }
    triggers {
        githubPush()
    }
}