# aws-lambda-flask-example
AWS Lambda Flask Example with Zappa

## Dependency
- python 3.7.1+

## Get Started
의존성 패키지 설치 방법은 pip를 사용할 수 있습니다.

### 1-1. 의존성 패키지 설치
```shell
$ pip install zappa
$ pip install flask
```

### 1-2. 문제가 있을 경우의 설치 방법
- 현재 2021-06-03 기준으로 Flask 2.0 업데이트에 더불어 zappa와의 버전 차이 문제가 있는 듯 합니다.
그 경우, 아래와 같이 순서대로 작업을 수행해줍니다.
```shell
$ git clone https://github.com/garnaat/kappa
// You need to change the version of /kappa/__init__.py to 0.6.0.

$ python -m pip install --upgrade pip && pip install ./kappa/ && pip install zappa && pip install flask && pip install awscli
```

### 2. AWS CLI 세팅
zappa를 사용하기 위해서는 AWS Identity and Access Management(IAM)에서 발급받은 액세스키 & 시크릿 액세스 키가 필요합니다.
```shell
$ aws configure
AWS Access Key ID [None]: <Access ID>
AWS Secret Access Key [None]: <Secret Access ID>
Default region name [None]: ap-northeast-2 //Seoul
Default output format [None]: json
```

### 3. Zappa init
```shell
$ zappa init
What do you want to call this environment (default 'dev'):
What do you want to call your bucket? (default 'zappa-sehds8918'): 
Where is your app's function? (default 'app.application'):
Would you like to deploy this application globally? (default 'n') [y/n/(p)rimary]:

$ zappa deploy [dev|production]
```


# References
https://github.com/zappa/Zappa
https://github.com/garnaat/kappa/tree/develop/kappa