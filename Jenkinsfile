pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-app'
        DOCKER_REGISTRY = 'sankalppp2'  // Or your private registry if you have one
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
                    docker.build(DOCKER_IMAGE)
                }
            }
        }

        stage('Push Docker Image to Registry') {
            steps {
                script {
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-credentials') {
                        docker.image(DOCKER_IMAGE).push()
                    }
                }
            }
        }

        stage('Deploy') {
            steps {
                script {
                    // Add deployment commands here if you're deploying to a server or cloud
                    sh 'docker run -d -p 5000:5000 flask-app'
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
