pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-app'
        DOCKER_REGISTRY = 'sankalppp2'
        FULL_IMAGE_NAME = "${DOCKER_REGISTRY}/${DOCKER_IMAGE}"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/Sankalp-Pattanayak/Canvas.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    docker.build(FULL_IMAGE_NAME)
                }
            }
        }

        stage('Push Docker Image to Registry') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', '1ebe2279-4e2a-410b-b528-b5c7f6da6d2a') {
                        docker.image(FULL_IMAGE_NAME).push()
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    sh "docker run -d -p 5000:5000 ${FULL_IMAGE_NAME}"
                }
            }
        }
    }

    post {
        always {
            cleanWs()
        }
    }
}
