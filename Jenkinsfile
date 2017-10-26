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
          
          python setup.py test
          echo "Begin of unittests"
          echo "==============="
          python tests.py 
          
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
