import requests
import json

# точки с валидными координатами
valid_points = {
    "point_1": (55.999653, 37.206002),
    "point_2": (55.996767, 37.184545),
    "point_3": (55.984932, 37.208749),
}

# только третья точка имеет валидные координаты
invalid_points = {
    "point_1": (255.999653, 37.206002),
    "point_2": (55.996767, 237.184545),
    "point_3": (55.984932, 37.208749),
}

for points in [valid_points, invalid_points]:

    # формируем конфигурацию imposter'a
    imposter_cfg = {
        "port": 8080,
        "protocol": "http",
        "stubs": [
            {
                "predicates": [
                    {
                        "equals": {
                            "method": "GET",
                            "path": "/api/points"
                        }
                    }
                ],
                "responses": [
                    {
                        "is": {
                            "statusCode": 200,
                            "headers": {"Content-Type": "application/json"},
                            "body": points
                        }
                    }
                ]
            }
        ]
    }

    # отправляем в mountebank запрос на создание imposter'a
    r = requests.request('POST', 'http://localhost:2525/imposters', data=json.dumps(imposter_cfg), headers={"content-type": "application/json"})
    print(r.text)
