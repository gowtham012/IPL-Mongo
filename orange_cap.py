[
    {
        '$match': {
            '$expr': {
                '$eq': [
                    '$season', '2017'
                ]
            }
        }
    }, {
        '$addFields': {
            'total_batsman_runs': {
                '$toInt': '$batsman_runs'
            }
        }
    }, {
        '$group': {
            '_id': '$batsman', 
            'runs': {
                '$sum': '$total_batsman_runs'
            }
        }
    }, {
        '$sort': {
            'runs': -1
        }
    }, {
        '$limit': 1
    }
]