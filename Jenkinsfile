pipeline {
    agent any
    
    stages {
      stage ("Code"){
          steps{
              git url:"https://github.com/Avatar1992/Django_To-Do_App_CI_CD.git",branch:"main"
          }
         }  
        stage ("Build"){
            steps{
                sh "docker build -t django-todo ."
            }
         }  
         stage('test'){
    steps {
        sh '''
            python manage.py makemigrations --noinput
            python manage.py migrate --noinput
            python manage.py test todo
        '''
    }
}
         stage('Scan') {
            steps {
                // Run Trivy scan on image
                sh 'trivy image --severity HIGH,CRITICAL --exit-code 1 django-todo || true'
            }
        }

         stage ("Run"){
             steps{
                 sh "docker run -d -p 8000:8000 django-todo:latest"
             }
         }  
    }
}
