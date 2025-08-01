pipeline {
    agent any

    environment {
        docker_image = 'mohanaswararajn/docker_jenkins:v1'
    }

    stages {
        stage("Check-out") {
            steps {
                git branch: 'main', url: 'https://github.com/Mohanaswararaj/Chat_jen.git'
            }
        }

        stage("Build image") {
            steps {
                sh '''
                    echo "Building Docker image"
                    docker build -t $docker_image Ml/
                '''
            }
        }

        stage("Push Docker image") {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: 'dockerhub', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                        sh '''
                            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                            docker push $docker_image
                        '''
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully'
        }
        failure {
            echo 'Pipeline failed'
        }
    }
}
