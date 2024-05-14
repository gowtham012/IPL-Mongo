[
    {
        '$group': {
            '_id': {
                'stadium': '$venue', 
                'team1': '$team1', 
                'team2': '$team2', 
                'winner': '$winner'
            }
        }
    }, {
        '$group': {
            '_id': {
                'stadium': '$_id.stadium', 
                'team1': '$_id.team1'
            }, 
            'winning_times': {
                '$sum': 1
            }
        }
    }, {
        '$sort': {
            'winning_times': -1
        }
    }, {
        '$limit': 15
    }
]