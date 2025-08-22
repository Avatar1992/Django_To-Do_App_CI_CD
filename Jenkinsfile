pipeline {
    agent any

    environment {
        IMAGE_NAME     = 'django-todo'
        IMAGE_TAG      = 'latest'
        FULL_IMAGE     = "${IMAGE_NAME}:${IMAGE_TAG}"
        CONTAINER_NAME = 'django-todo-app'
        PY_IMAGE       = 'python:3.11-slim'
    }

    stages {
        stage('Code') {
            steps {
                git url: 'https://github.com/Avatar1992/Django_To-Do_App_CI_CD.git', branch: 'staging'
            }
        }

        stage('docker-in') {
            steps {
                script {
                  
                    docker.image(env.PY_IMAGE).inside('--user root') {
                        sh '''
                            set -eux
                            python --version
                            pip install --no-cache-dir -r requirements.txt
                        '''
                    }
                }
            }
        }

     
        stage('docker-out') {
            steps {
                sh '''
                    set -eux
                    docker build -t ${FULL_IMAGE} .
                    docker images --format "{{.Repository}}:{{.Tag}}" | grep -E "^${IMAGE_NAME}:${IMAGE_TAG}$" || true
                '''
            }
        }

   
        stage('Run (docker-out)') {
            steps {
                sh '''
                    set -eux
                    docker rm -f ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} -p 8000:8000 ${FULL_IMAGE}
                    docker ps --filter "name=${CONTAINER_NAME}"
                '''
            }
        }
    }

}
