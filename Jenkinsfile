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
                script{
                    FAILED_STAGE=env.STAGE_NAME
                }  
            }
        }
        stage('TestApp'){
            steps {
                sh 'virtualenv venv && . venv/bin/activate && pip install xmlrunner && python src/test.py'
                script{
                    FAILED_STAGE=env.STAGE_NAME
                }    
            }

        }
        stage('RunApp'){
            steps {
                sh 'python src/operaciones.py'
                script{
                    FAILED_STAGE=env.STAGE_NAME
                }  
            }
        }
        stage('Notify'){
        
                steps {
                mail (body: "El pipeline ha finalizado. Consulta la información en el siguiente enlace: '${env.BUILD_URL} ${FAILED_STAGE}'", subject: "FINISHED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'", to: "rodriguezromero4@gmail.com")
            }
        
        }
    }
    triggers {
        githubPush() 
    }
}

