# imageresize

```
이미지 파일 입력받아 thumbnail 이미지로 변환하는 API

ngix + uwsgi + flask

```

## 요청 주소
/resize

## 요청 변수 ( Request Parameters )

| 파리미터 | 타입    | 설명                   |
| -------- | ------- | ---------------------  |
| file     | file    | 이미지파일을 첨부한다  |

## 출력 결과 ( Response Element )

| 출력변수  | 값      | 설명                                  |
| --------- | ------- | ------------------------------------- |
| result    | int     | 0인 경우 정상                         |
| error     | string  | 오류가 있는 경우 메시지 출력          |
| thumbnail | -       | 처리된 결과 정보                      |
| width     | int     | 변환된 이미지 길이                    |
| height    | int     | 변환된 이미지 높이                    |
| uri       | string  | 변환된 이미지 다운받을 수 있는 URI    |
| filename  | string  | 변환된 이미지 filename                |

## 출력 예제

```json
{
  "error": "OK", 
  "result": 0, 
  "thumbnail": [
    {
      "filename": "5d666b2eaecb409d8e79e328961dfe15_200_320.png", 
      "height": 320, 
      "uri": "/download/5d666b2eaecb409d8e79e328961dfe15_200_320.png", 
      "width": 200
    }, 
    {
      "filename": "5d666b2eaecb409d8e79e328961dfe15_480_640.png", 
      "height": 640, 
      "uri": "/download/5d666b2eaecb409d8e79e328961dfe15_480_640.png", 
      "width": 480
    }, 
    {
      "filename": "5d666b2eaecb409d8e79e328961dfe15_600_800.png", 
      "height": 800, 
      "uri": "/download/5d666b2eaecb409d8e79e328961dfe15_600_800.png", 
      "width": 600
    }
  ]
}
```

# Links
* [pillow](https://pillow.readthedocs.org/en/3.1.x/) - 이미지 변환 라이브러리
* [Flask](http://flask.pocoo.org/) - Web framework
