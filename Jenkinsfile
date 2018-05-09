node {

 stage ('Docker pull'){
 sh 'echo "docker pull"'
 sh 'docker pull 589933236526.dkr.ecr.us-east-1.amazonaws.com/jenkins-repo:latest'
 sh 'echo "test"'
 }
 
 stage ('Docker run') {
 sh "docker tag 589933236526.dkr.ecr.us-east-1.amazonaws.com/jenkins-repo:latest mireille/jenkins-project"     
 sh "docker run -itd -p 8888:8080 mireille/jenkins-project"
 }
 
 stage ('Test image') {
  try {
            sh 'wget http://172.31.44.120:8888/directeam -O /dev/null'
            return true
        } catch (Exception e) {
            throw e;
    }
    }
    }
