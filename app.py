from flask import Flask, jsonify, request

app = Flask(__name__)

TICKETS = [
    # Expired booking numbers
    {'booking_number': 'AAAAA', 'departure': 1542868560,
     'arrival': 1542876120, 'status': 0, 'return': 0},

    {'booking_number': 'AAAAB', 'departure': 1542868560,
     'arrival': 1542876120, 'status': 0, 'return': 0,
     'return_departure': 1542958920, 'return_arrival': 1542966480,
     'return_status': 0},

    {'booking_number': 'AAAAC', 'departure': 1542868560,
     'arrival': 1542876120, 'status': 1, 'return': 0},

    {'booking_number': 'AAAAD', 'departure': 1542868560,
     'arrival': 1542876120, 'status': 1, 'return': 1,
     'return_departure': 1542958920, 'return_arrival': 1542966480,
     'return_status': 1},

    {'booking_number': 'AAAAE', 'departure': 1542868560,
     'arrival': 1542876120, 'status': 2, 'return': 0},

    {'booking_number': 'AAAAF', 'departure': 1542868560,
     'arrival': 1542876120, 'status': 2, 'return': 1,
     'return_departure': 1542958920, 'return_arrival': 1542966480,
     'return_status': 2},

    # Available booking numbers to purchase
    {'booking_number': 'AAAAG', 'departure': 1546407780,
     'arrival': 1546412160, 'status': 'NORMAL', 'return': 0},

    {'booking_number': 'AAAAH', 'departure': 1546407780,
     'arrival': 1546412160, 'status': 'NORMAL', 'return': 1,
     'return_departure': 1546494960, 'return_arrival': 1546499340,
     'return_status': 0},

    {'booking_number': 'AAAAI', 'departure': 1546407780,
     'arrival': 1546412160, 'status': 1, 'return': 0},

    {'booking_number': 'AAAAJ', 'departure': 1546407780,
     'arrival': 1546412160, 'status': 1, 'return': 1,
     'return_departure': 1546494960, 'return_arrival': 1546499340,
     'return_status': 1},

    {'booking_number': 'AAAAK', 'departure': 1546407780,
     'arrival': 1546412160, 'status': 2, 'return': 0},

    {'booking_number': 'AAAAL', 'departure': 1546407780,
     'arrival': 1546412160, 'status': 2, 'return': 1,
     'return_departure': 1546494960, 'return_arrival': 1546499340,
     'return_status': 2},
]


@app.route('/tickets', methods=['GET', 'POST'])
def get_tickets():
    """"Get all tickets"""
    return jsonify({'tickets': TICKETS})


@app.route('/ticket', methods=['GET', 'POST'])
def get_ticket():
    """Get ticket using request params"""
    if not request.args:
        return jsonify({'error': 'no-args-given'})
    if not check_args(request.args):
        return jsonify({'error': 'invalid-args'})
    for ticket in TICKETS:
        if all(str(ticket.get(k)) == str(v) for k, v in request.args.items()):
            return jsonify({'ticket': ticket})
    return jsonify({'ticket': None})


def check_args(args):
    """Check if request params are valid"""
    allowed = [
        'booking_number', 'departure', 'arrival', 'status', 'type',
        'return_departure', 'return_arrival', 'return_status'
    ]
    for arg in args.keys():
        if arg not in allowed:
            return False
    return True


if __name__ == "__main__":
    app.run(debug=True)
