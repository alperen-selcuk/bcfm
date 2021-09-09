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
    stage('quality gate') {
        timeout(time: 1, unit: 'HOURS') {
        def quality = waitForQualityGate()
            if (quality.ststus != 'OK') {
                error "pipeline aborted because of quality report: ${quality.ststus}"
                }
            }
        }
}
