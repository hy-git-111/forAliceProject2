pipeline {
  agent {
    dockerfile {
      filename 'Dockerfile'
      dir '.'
    }
  }

  environment {
    PYTHONUNBUFFERED = '1'
  }

  stages {
    stage('Set up workspace') {
      steps {
        echo '📁 reports 폴더 미리 생성'
        sh 'mkdir -p qa-realworld-automation/reports'
      }
    }

    stage('Run tests') {
      steps {
        echo '🧪 pytest 테스트 실행'
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
