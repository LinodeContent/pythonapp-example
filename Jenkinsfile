pipeline {
  agent {
    docker {
      image 'python:3.5.4-slim-jessie'
    }
    
  }
  stages {
    stage('build') {
      steps {
        sh 'python --version'
      }
    }
  }
  post {
        
        success {
            echo 'I succeeeded!'
        }
  }
}
