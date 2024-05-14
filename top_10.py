[
    {
        '$match': {
            '$expr': {
                '$eq': [
                    '$team1', 'Chennai Super Kings'
                ]
            }
        }
    }, {
        '$addFields': {
            'total_batsman_run': {
                '$toInt': '$batsman_runs'
            }
        }
    }, {
        '$group': {
            '_id': '$batsman', 
            'runs': {
                '$sum': '$total_batsman_run'
            }
        }
    }, {
        '$sort': {
            'runs': -1
        }
    }, {
        '$limit': 10
    }
]