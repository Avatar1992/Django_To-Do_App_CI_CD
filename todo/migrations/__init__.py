stage('test') {
    steps {
        sh '''
            python manage.py migrate --noinput
            python manage.py test todo
        '''
    }
}
