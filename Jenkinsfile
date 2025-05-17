pipeline {
  agent {
    docker {
      image 'python:3.10'
      args '-u root' // root 권한으로 pip install 허용
    }
  }

  environment {
    PYTHONUNBUFFERED = '1' // 실시간 로그 출력
  }

  stages {
    stage('Set up workspace') {
      steps {
        echo '📁 reports 폴더 미리 생성'
        sh 'mkdir -p qa-realworld-automation/reports'
      }
    }

    stage('Install dependencies') {
      steps {
        echo '📦 requirements.txt로 패키지 설치'
        sh 'pip install --upgrade pip'
        sh 'pip install -r qa-realworld-automation/requirements.txt'
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
