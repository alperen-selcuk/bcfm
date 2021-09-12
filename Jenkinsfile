pipeline {
    environment {
        NAME = "${env.BRANCH_NAME == "master" ? "prod" : "dev"}"
        VERSION = "${BUILD_NUMBER}"
        DOMAIN = 'localhost'
        REGISTRY = 'hasanalperen/bcfm'
        REGISTRY_CREDENTIAL = 'dockerhub'
        APP = 'my_app'
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
                    sh "docker build -t ${REGISTRY}:${APP}-${NAME}-${VERSION} ."
                }
            }
        }
        stage('Docker Publish') {
            steps {
                container('docker') {
                    withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
                        sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                        sh "docker push ${REGISTRY}:${APP}-${NAME}"
                    }
                }
            }
        }
    }
}
