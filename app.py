from flask import Flask, jsonify, request

app = Flask(__name__)


tickets = [
    # Expired booking numbers
    {'booking_number': 'AAAAA', 'departure': 1542868560,
        'arrival': 1542876120, 'status': 'NORMAL', 'type': 'single'},

    {'booking_number': 'AAAAB', 'departure': 1542868560, 'arrival': 1542876120, 'status': 'NORMAL',
        'type': 'return', 'return_departure': 1542958920, 'return_arrival': 1542966480, 'return_status': 'NORMAL'},

    {'booking_number': 'AAAAC', 'departure': 1542868560,
     'arrival': 1542876120, 'status': 'DELAYED', 'type': 'single'},

    {'booking_number': 'AAAAD', 'departure': 1542868560, 'arrival': 1542876120, 'status': 'DELAYED',
     'type': 'return', 'return_departure': 1542958920, 'return_arrival': 1542966480, 'return_status': 'DELAYED'},

    {'booking_number': 'AAAAE', 'departure': 1542868560,
     'arrival': 1542876120, 'status': 'CANCELLED', 'type': 'single'},

    {'booking_number': 'AAAAF', 'departure': 1542868560, 'arrival': 1542876120, 'status': 'CANCELLED',
     'type': 'return', 'return_departure': 1542958920, 'return_arrival': 1542966480, 'return_status': 'CANCELLED'},

    # Available booking numbers to purchase
    {'booking_number': 'AAAAG', 'departure': 1546407780,
     'arrival': 1546412160, 'status': 'NORMAL', 'type': 'single'},

    {'booking_number': 'AAAAH', 'departure': 1546407780, 'arrival': 1546412160, 'status': 'NORMAL',
     'type': 'return', 'return_departure': 1546494960, 'return_arrival': 1546499340, 'return_status': 'NORMAL'},

    {'booking_number': 'AAAAI', 'departure': 1546407780,
     'arrival': 1546412160, 'status': 'DELAYED', 'type': 'single'},

    {'booking_number': 'AAAAJ', 'departure': 1546407780, 'arrival': 1546412160, 'status': 'DELAYED',
     'type': 'return', 'return_departure': 1546494960, 'return_arrival': 1546499340, 'return_status': 'DELAYED'},

    {'booking_number': 'AAAAK', 'departure': 1546407780,
     'arrival': 1546412160, 'status': 'CANCELLED', 'type': 'single'},

    {'booking_number': 'AAAAL', 'departure': 1546407780, 'arrival': 1546412160, 'status': 'CANCELLED',
     'type': 'return', 'return_departure': 1546494960, 'return_arrival': 1546499340, 'return_status': 'CANCELLED'},
    ]

@app.route('/tickets', methods=['GET', 'POST'])
def get_tickets():
    if not request.args:
        return jsonify({'error': 'no-args-given'})
    if not check_args(request.args):
        return jsonify({'error': 'invalid-args'})
    for ticket in tickets:
        if all(str(ticket.get(k)) == str(v) for k, v in request.args.items()):
            return jsonify({'ticket': ticket})
    return jsonify({'ticket': None})

def check_args(args):
    allowed = [
        'booking_number', 'departure', 'arrival', 'status', 'type',
        'return_departure', 'return_arrival', 'return_status'
    ]
    for arg in args.keys():
        if arg not in allowed:
            return False
    return True

# Probably won't use due to Solidity limitations
@app.route('/tickets/<string:name>', methods=['GET'])
def return_status(name):
    status = 'INVALID'

    for i, f in enumerate(tickets):
        if f['booking_number'] == name:
            if tickets[i]['type'] == 'single':
                status = tickets[i]['status']
            else:
                status = tickets[i]['status']
                return_status = tickets[i]['return_status']
                return jsonify({'status': status, 'return_status': return_status})
    return jsonify({'status': status})


if __name__ == "__main__":
    app.run(debug=True)
