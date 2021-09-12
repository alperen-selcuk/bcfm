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
            label "jk-pod" 
            defaultContainer 'jnlp'
            yaml """
apiVersion: v1
kind: Pod
metadata:
labels:
  component: ci
spec:
  containers:
  - name: docker
    image: docker:latest
    command:
    - cat
    tty: true
    volumeMounts:
    - mountPath: /var/run/docker.sock
      name: docker-sock
  volumes:
    - name: docker-sock
      hostPath:
        path: /var/run/docker.sock
"""
        }
    }
    stages {
        //stage ('checkout') {
            //steps {
                //git 'https://github.com/alperen-selcuk/bcfm'
            //}
        //}
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
