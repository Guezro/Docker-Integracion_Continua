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
    
    }
    post { 
        success { 
            mail (body: "El pipeline ha finalizado satisfactoriamente. Consulta la información en el siguiente enlace: '${env.BUILD_URL}'", subject: "SUCCESSFULLY FINISHED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'", to: "rodriguezromero4@gmail.com")
        }
        failure { 
            mail (body: "El pipeline ha terminado con errores en el proceso. Consulta la información en el siguiente enlace: '${env.BUILD_URL}'", subject: "FINISHED WITH ERRORS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'", to: "rodriguezromero4@gmail.com")
        }
    }
    
    triggers {
        githubPush() 
    }
}

