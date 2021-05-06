update_add_imposter = {
    "port": 8080,
    "protocol": "http",
    "stubs": [
        {
            "predicates": [
                {
                    "equals": {
                        "method": "POST",
                        "path": "/update/add"
                    }
                }
            ],
            "responses": [
                {
                    "is": {
                        "statusCode": 200,
                        "headers": {"Content-Type": "application/json"},
                        "body": {
                            "status": "ok",
                            "data": {
                                "name": "test",
                                "surname": "test",
                                "grade": 100,
                                "sex": "test"
                            }
                        }
                    }
                }
            ]
        }
    ]
}
