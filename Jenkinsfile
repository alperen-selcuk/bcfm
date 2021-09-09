node {
    stage('SCM from git') {
        git 'https://github.com/alperen-selcuk/bcfm'
    }

    stage('sonarqube report') {
        def scannerHome = tool 'sonar-scanner';
        withSonarQubeEnv ('sonar-server') {
            sh "${scannerHome}/bin/sonar-scanner"
        }
    }
}



