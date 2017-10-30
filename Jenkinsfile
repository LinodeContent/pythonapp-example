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
            python setup.py build sdist bdist_wheel --universal
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
        TWINE_USERNAME = 'damasosanoja'
        TWINE_PASSWORD = 'Mx76Z$!Lcq'
      }
      steps {
        sh '''
            echo "This is your deployment Block"
            twine upload --repository-url https://test.pypi.org/legacy/ dist/* 
            '''
      }
    }
  }
  post {
    always {
      echo 'Actions here will always happen.'
      cleanWs()
      
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
