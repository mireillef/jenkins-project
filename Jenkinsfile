node {
  stage 'Docker build'
  docker.build('mireille/jenkins-app')

  stage 'Docker push'
  docker.withRegistry('https://589933236526.dkr.ecr.us-east-1.amazonaws.com/jenkins-repo', 'ecr:us-east-1:6ebbaf2a-b4f6-462c-ac63-783295818026') {
    docker.image('mireille/jenkins-app').push("${env.BUILD_NUMBER}")
  }
 stage 'Docker pull'
 docker.image(jenkins-repo).pull()

 stage 'Docker run'
 sh "docker run -itd -p 8888:8080 mireille/jenkins-app"

 stage 'Test image'
  try {
            sh 'curl http://54.243.2.143:8888 -O /dev/null'
            return true
        } catch (exception) {
            return false
}


