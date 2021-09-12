pipeline {
    environment {
        NAME = "${env.BRANCH_NAME == "master" ? "bcfm-prod" : "bcfm-dev"}"
        VERSION = "${BUILD_NUMBER}"
        DOMAIN = 'localhost'
        REGISTRY = 'hasanalperen/bcfm'
        REGISTRY_CREDENTIAL = 'dockerhub'
    }
    agent { 
        kubernetes {
            yaml '''
            apiVersion: v1
            kind: Pod
            spec:
               containers:
               - name : docker
                 image : docker:latest
                 command:
                 - cat
                 tty : true
                 volumeMounts: 
                 - mountPath: /var/run/docker.sock
                   name: docker-sock
               volumes: 
                 - name : docker-sock
                   hostPath: 
                      path: /var/run/docker.sock
             '''
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
            steps {
                container('docker') {
                    withDockerRegistry([credentialsId: "${REGISTRY_CREDENTIAL}", url: ""]) {
                        sh "docker push ${REGISTRY}:${VERSION}-${NAME}"
                    }
                }
            }
        }
    }
}
