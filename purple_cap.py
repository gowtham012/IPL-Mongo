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
        '$group': {
            '_id': {
                'bowler': '$bowler', 
                'fielder': '$fielder'
            }
        }
    }, {
        '$group': {
            '_id': '$_id.bowler', 
            'purple': {
                '$sum': 1
            }
        }
    }, {
        '$sort': {
            'purple': -1
        }
    }
]