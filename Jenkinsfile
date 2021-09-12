pipeline {
    environment {
        NAME = "${env.BRANCH_NAME == "master" ? "bcfm-prod" : "bcfm-dev"}"
        VERSION = ${BUILD_NUMBER}
        DOMAIN = 'localhost'
        REGISTRY = 'hasanalperen/bcfm'
        REGISTRY_CREDENTIAL = 'dockerhub'
    }
    agent {
        kubernetes {
            defaultContainer 'jnlp'
            yamlFile 'build.yaml'
        }
    }
    stages {
        stage('Docker Build') {
            steps {
                container('docker') {
                    sh "docker build -t ${REGISTRY}:${VERSION}-${NAME} ."
                }
            }
        }
        stage('Docker Publish') {
            when {
                environment name: 'DEPLOY', value: 'true'
            }
            steps {
                container('docker') {
                    withDockerRegistry([credentialsId: "${REGISTRY_CREDENTIAL}", url: ""]) {
                        sh "docker push ${REGISTRY}:${VERSION}-${NAME}"
                    }
                }
            }
        }
}
