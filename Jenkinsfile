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
        stage('BuildDocker'){
            steps {
                sh 'docker build -t myjenkins-blueocean:1.1 .'
            }
        }
        stage('PushDockerImage'){
            steps {
                sh '''
                docker tag myjenkins-blueocean:1.1 prueba/myjenkins-blueocean:1.1
                                docker push prueba/myjenkins-blueocean:1.1
                                docker rmi myjenkins-blueocean:1.1
                
                '''
            }
        }
    }
    triggers {
        githubPush() 
    }
}
