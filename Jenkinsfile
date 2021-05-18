pipeline {
    agent {
        docker {
            image 'qnib/pytest:latest'
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
                sh 'virtualenv venv && . venv/bin/activate && pip install xmlrunner && python src/test.py'
                    
            }

        }
        stage('RunApp'){
            steps {
                sh 'python src/operaciones.py'
            }
        }
        stage('Build'){
            steps {
                echo "Running job: ${env.JOB_NAME}\nbuild: ${env.BUILD_ID} - ${env.BUILD_URL}\nblue ocean: ${env.RUN_DISPLAY_URL}"
            }
        }

    }
    post {
        failure {
            mail to: 'rodriguezromero4@gmail.com', from: 'jenkins@example.com',
                subject: "Example Build: ${env.JOB_NAME} - Failed", 
                body: "Job Failed - \"${env.JOB_NAME}\" build: ${env.BUILD_NUMBER}\n\nView the log at:\n ${env.BUILD_URL}\n\nBlue Ocean:\n${env.RUN_DISPLAY_URL}"
        }
    }
    triggers {
        githubPush() 
    }
}

