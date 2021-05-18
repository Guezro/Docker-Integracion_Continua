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
        stage('Notify'){
        
                steps {
                mail (body: "El pipeline ha finalizado. Consulta la información en el siguiente enlace: '${env.BUILD_URL} [${env.JOB_URL}]'", subject: "Pipeline Finalizado correctamente", to: "rodriguezromero4@gmail.com")
            }
        
        }
    }
    triggers {
        githubPush() 
    }
}

