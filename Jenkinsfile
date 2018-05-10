node {
 stage ('Docker build') {
 sh "git clone https://github.com/mireillef/jenkins-project.git"
 sh "docker build -t mireille/jenkins-app jenkins-project/ "
 }
 
 stage ('Docker push') {
 sh "\$(aws ecr get-login --no-include-email --region us-east-1)"     
 sh "docker tag mireille/jenkins-app 589933236526.dkr.ecr.us-east-1.amazonaws.com/jenkins-repo:${env.BUILD_NUMBER}"
 sh "docker push 589933236526.dkr.ecr.us-east-1.amazonaws.com/jenkins-repo:${env.BUILD_NUMBER}"
 }
 
 stage ('Docker pull') {
 sh "docker pull 589933236526.dkr.ecr.us-east-1.amazonaws.com/jenkins-repo:latest"
 }
 
 stage ('Docker run') {
 sh "docker tag 589933236526.dkr.ecr.us-east-1.amazonaws.com/jenkins-repo:latest mireille/jenkins-project"     
 sh "docker run -itd -p 8888:8080 mireille/jenkins-project"
 }
 
 stage ('Test image') {
  try {
            sh "wget http://localhost:8888/directeam -O /dev/null"
            return true
        } catch (Exception e) {
            throw e;
    }
    }
    }
