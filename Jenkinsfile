pipeline {
    agent any

    environment {
        AWS_ACCOUNT_ID = "782989862398"
        AWS_REGION = "ap-south-1b"
        ECR_REPO = "jenkins-eks-demo"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh """
                    docker build -t $ECR_REPO .
                    docker tag $ECR_REPO:latest \
                    $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:latest
                    """
                }
            }
        }

        stage('Push to ECR') {
            steps {
                sh """
                aws ecr get-login-password --region $AWS_REGION | \
                docker login --username AWS --password-stdin \
                $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com

                docker push \
                $AWS_ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$ECR_REPO:latest
                """
            }
        }

        stage('Deploy to EKS') {
            steps {
                sh """
                kubectl apply -f deployment.yaml
                kubectl apply -f service.yaml
                """
            }
        }
    }
}
