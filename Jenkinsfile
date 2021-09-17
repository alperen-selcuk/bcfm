pipeline {
    environment {
        //NAME = "${env.BRANCH_NAME == "master" ? "prod" : "dev"}"
        VERSION = "${BUILD_NUMBER}"
        DOMAIN = 'localhost'
        REGISTRY = 'hasanalperen/bcfm'
        REGISTRY_CREDENTIAL = 'dockerhub'
        APP = 'web'
        HELM_REPO = "http://35.230.132.88:9090"
        helmversion = "0.1"+"."+"${VERSION}"
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
               - name: helm
                 image: dtzar/helm-kubectl
                 command: 
                 - cat
                 tty: true
               - name: google
                 image: google/cloud-sdk
                 command:
                 - cat
                 tty: true
                 volumeMounts: 
                 - mountPath: /root
                   name: console-root
                 - mountPath: /root/.kube
                   name: console-kube
               volumes: 
                 - name : docker-sock
                   hostPath: 
                      path: /var/run/docker.sock
                 - name: console-root
                   hostPath: 
                      path: /var/sa
                 - name: console-kube
                   hostPath: 
                      path: /var/sa/.kube
             '''
        }
    }
    stages {
        stage('Docker Build') {
            steps {
                container('docker') {
                    sh "docker build -t ${REGISTRY}:${VERSION} ."
                }
            }
        }
        stage('Docker Push') {
            steps {
                container('docker') {
                    withCredentials([usernamePassword(credentialsId: 'dockerHub', passwordVariable: 'dockerHubPassword', usernameVariable: 'dockerHubUser')]) {
                        sh "docker login -u ${env.dockerHubUser} -p ${env.dockerHubPassword}"
                        sh "docker push ${REGISTRY}:${VERSION}"
                    }
                }
            }
        }
    }
}
