pipeline {
  agent {
    docker {
      image 'python'
      args '3.5.1'
    }
    
  }
  stages {
    stage('build') {
      steps {
        sh 'python --version'
      }
    }
  }
}