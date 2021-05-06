import requests
import json

"""
Актуальная команда для запуска:
docker run -p 2525:2525 -p 8080:8080 -p 8081:8081 bbyars/mountebank start
"""

# точки с валидными координатами
valid_points = {
    "point_1": (55.99, 37.20),
    "point_2": (55.99, 37.18),
    "point_3": (55.98, 37.20),
}

# только третья точка имеет валидные координаты
invalid_points = {
    "point_1": (255.99, 37.20),
    "point_2": (55.99, 237.18),
    "point_3": (55.98, 37.20),
}

for points in [valid_points, invalid_points]:
    # формируем конфигурацию imposter'a
    imposter_cfg = {
        "port": 8081,
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
    r = requests.request(
        'POST',
        'http://localhost:2525/imposters',
        data=json.dumps(imposter_cfg),
        headers={"content-type": "application/json"}
    )

    print("Mountebank response: ", r.text)
