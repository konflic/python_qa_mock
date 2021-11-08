update_add_imposter = lambda data_to_mock: {
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
                            "data": data_to_mock
                        }
                    }
                }
            ]
        }
    ]
}
