# Basic Client

PC 의 CPU 사용량을 모니터하여 서버에 전송한다.

## Setup

가상환경 설치 및 실행
```sh
python3 -m venv venv
source venv/bin/activate
```

## Run

다음 명령어로 프로그램을 실행한다.
```sh
python -u run_client.py
```
`-u` 옵션은 unbuffered 옵션으로 로그를 딜레이 없이 출력한다.


## Customize

```diff

코드에 `TARGET_IP` 부분을 내 서버의 ip 로 변경한다. 
- TARGET_IP = "127.0.0.1"
+ TARGET_IP = "내 서버 ip"
API_URL = f"http://{TARGET_IP}:8000/cpu-monitor"
```

## Trouble Shooting

- Connection 불안
```text
requests.exceptions.ConnectionError: HTTPConnectionPool(host='127.0.0.1', port=8000): Max retries exceeded with url: /cpu-monitor (Caused by NewConnectionError('<urllib3.connection.HTTPConnection object at 0x725871af1f90>: Failed to establish a new connection: [Errno 111] Connection refused'))
```
위와 같은 에러는 server가 돌지 않는 상태에서 client를 돌려서 생긴다. server 프로그램을 돌리고 다시 시도해보자.
