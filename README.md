# aws-lambda-flask-example
AWS Lambda Flask Example with Zappa 



## Dependency

- **python 3.7.1**
- **zappa 0.52.0**
- **kappa 0.6.0**



## Get Started

아래의 순서대로 작업을 수행해야 합니다. 더 자세한 설명은 여기를 참고해주세요.
**(아래의 모든 과정은 반드시 가상 환경 내에서 진행되어야 합니다)**


### 1-1. 의존성 패키지 설치

```shell
$ pip install zappa
$ pip install flask
$ pip install awscli
```



### 1-2. 문제가 있을 경우의 설치 방법

- 현재 2021-06-03 기준으로 Flask 2.0 업데이트에 더불어 zappa와의 버전 차이 및 Windows 운영체제에 한하여 문제가 있는 듯 합니다. 이 경우, 아래와 같이 순서대로 작업을 수행해줍니다.

**(이 경우, Flask 1.1.2 버전으로 대체됩니다)**

```shell
$ python -m pip install --upgrade pip
$ git clone https://github.com/garnaat/kappa
// You need to change the version of /kappa/__init__.py to 0.6.0.

$ pip install ./kappa/
$ pip install -r requirements.txt
```



### 2. AWS CLI Setting

zappa를 사용하기 위해서는 AWS Identity and Access Management(IAM)에서 발급받은 액세스키 & 시크릿 액세스 키가 필요합니다.
```shell
$ aws configure
AWS Access Key ID [None]: <Access ID>
AWS Secret Access Key [None]: <Secret Access ID>
Default region name [None]: ap-northeast-2 //Seoul
Default output format [None]: json
```



### 3. Zappa init & deploy
zappa init 설정을 완료하면 zappa_settings.json이 생성됩니다.
github action으로 배포를 자동화하기 원한다면 해당 파일도 함께 Git에 함께 저장합니다.

```shell
$ zappa init
What do you want to call this environment (default 'dev'):
What do you want to call your bucket? (default 'zappa-sehds8918'): 
Where is your app's function? (default 'app.application'):
Would you like to deploy this application globally? (default 'n') [y/n/(p)rimary]:

$ zappa deploy [dev|production]

# build log
$ zappa tail [dev|production]
```



# References

https://github.com/zappa/Zappa
https://github.com/garnaat/kappa/tree/develop/kappa
