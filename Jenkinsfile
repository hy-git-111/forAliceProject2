pipeline {
  agent {
    docker {
      image 'python:3.10'
      args '-u root'
    }
  }

  environment {
    PYTHONUNBUFFERED = '1'
  }

  stages {
    stage('Install Dependencies') {
      steps {
        sh 'pip install -r qa-realworld-automation/requirements.txt'
      }
    }

    stage('Run Tests') {
      steps {
        sh 'pytest qa-realworld-automation/tests --maxfail=1 --disable-warnings -v'
      }
    }
  }

  post {
    always {
      echo '📌 모든 단계 종료됨'
    }
    success {
      echo '🎉 테스트 성공'
    }
    failure {
      echo '❌ 테스트 실패 - 로그 확인 필요'
    }
  }
}
