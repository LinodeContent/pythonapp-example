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
          echo "Begin of nose tests"
          echo "===================="
          pip install nosetests
          nosetests --with-xunit
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
