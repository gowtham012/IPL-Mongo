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
        '$group': {
            '_id': {
                'field1': '$id', 
                'field2': '$toss_decision', 
                'field3': '$toss_winner', 
                'field4': '$winner'
            }
        }
    }, {
        '$match': {
            '$expr': {
                '$eq': [
                    '$_id.field3', '$_id.field4'
                ]
            }
        }
    }, {
        '$group': {
            '_id': {
                'winner': '$_id.field4', 
                'toss_decision': '$_id.field2'
            }, 
            'winning': {
                '$sum': 1
            }
        }
    }, {
        '$sort': {
            'winning': -1
        }
    }
]