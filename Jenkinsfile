pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Building...'
                build 'project_build_image'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing...'
                build 'project_run_tests'
            }
        }
        stage('Report') {
            steps {
                echo 'Reporting...'
                allure includeProperties: false, jdk: '', results: [[path: 'allure_report']]
            }
        }
    }
}