pipeline {
  agent {
    docker {
      image 'ubuntu:16.04'
    }
    
  }
  stages {
    stage('build') {
      steps {
        sh '''
          whoami
          python3 setup.py test
          echo "Begin of unittests"
          echo "==============="
          python3 tests.py 
          
          '''
      }
    }
  }
  post {
        
        success {
            echo 'I succeeeded!'
        }
        always {
            junit 'build/reports/**/*.xml'
        }
  }     
}
