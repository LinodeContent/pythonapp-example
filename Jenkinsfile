pipeline {
  agent {
    docker {
      image 'python:3.5.4-slim-jessie'
    }
    
  }
  stages {
    stage('Build') {
      steps {
        sh '''
                    echo "This is your building Block"
                    python -V
                    python setup.py build
                    '''
      }
    }
    stage('Test') {
      steps {
        sh '''
                    echo "This is your testing Block"
                    python setup.py test
                    '''
      }
    }
    stage('Deploy') {
      steps {
        sh '''
                    echo "This is your deployment Block"
                    pip show twine
                    pip show wheel
                    '''
      }
    }
  }
  post {
    always {
      echo 'Actions here will always happen.'
      
    }
    
    success {
      echo 'If you see this is because we succeed'
      
    }
    
    unstable {
      echo 'Sorry, I am unstable :/'
      
    }
    
    failure {
      echo 'You have to try again, because Pipeline failed :('
      
    }
    
    changed {
      echo 'Things were different before...'
      
    }
    
  }
}
