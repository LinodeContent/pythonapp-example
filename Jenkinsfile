pipeline {
  agent {
    docker {
      image 'python:3.5.4-slim-jessie'
    }
    
  }
  stages {
    stage('build') {
      steps {
        sh '''
          python setup.py test
          echo "Begin of unittests"
          echo "==============="
          python pythonapp/tests/test_app.py 
          
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
