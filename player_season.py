[
    {
        '$match': {
            '$expr': {
                '$eq': [
                    '$season', '2016'
                ]
            }
        }
    }, {
        '$group': {
            '_id': {
                'field1': '$id', 
                'field2': '$player_of_match'
            }
        }
    }, {
        '$group': {
            '_id': '$_id.field2', 
            'player_season': {
                '$sum': 1
            }
        }
    }, {
        '$sort': {
            'player_season': -1
        }
    }
]