pipeline {
  agent {
    docker {
      image 'python:3.10'
      args '-u root'
    }
  }

  stages {
    stage('Git Clone') {
      steps {
        sh 'git --version'
        sh 'rm -rf forAliceProject2' // ✅ 여기 추가됨
        sh 'git clone https://github.com/hy-git-111/forAliceProject2.git'
        sh 'ls forAliceProject2'
      }
    }

    stage('Run Tests') {
      steps {
        dir('forAliceProject2') {
          sh 'pip install -r qa-realworld-automation/requirements.txt'
          sh 'pytest qa-realworld-automation/tests --maxfail=1 --disable-warnings -v'
        }
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
