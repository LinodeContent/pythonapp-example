pipeline {
  agent {
    dockerfile true
  }
  stages {
    stage('Build') {
      steps {
        sh '''
                    echo "This is your building Block"
                    python -V
                    python setup.py sdist
                    python setup.py bdist_wheel --universal
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
      environment {
        username = 'damasosanoja'
        password = 'Mx76Z$!Lcq'
      }
      steps {
        sh '''
                    echo "This is your deployment Block"
twine -u username -p password upload dist/*
                    
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