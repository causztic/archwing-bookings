from flask import Flask, jsonify, request

app = Flask(__name__)


tickets = [
    {'booking_number': 'AAAAA', 'departure': '2018-11-22 14:36:00',
        'arrival': '2018-11-22 16:42:00', 'status': 'NORMAL', 'type': 'single'},

    {'booking_number': 'AAAAB', 'departure': '2018-11-22 14:36:00', 'arrival': '2018-11-22 16:42:00', 'status': 'NORMAL',
        'type': 'return', 'return_departure': '2018-11-23 15:42:00', 'return_arrival': '2018-11-23 17:48:00', 'return_status': 'NORMAL'},

    {'booking_number': 'AAAAC', 'departure': '2018-11-24 16:15:00',
     'arrival': '2018-11-24 17:48:00', 'status': 'NORMAL', 'type': 'single'},

    {'booking_number': 'AAAAD', 'departure': '2018-11-24 16:15:00', 'arrival': '2018-11-24 17:48:00', 'status': 'NORMAL',
     'type': 'return', 'return_departure': '2018-11-25 16:48:00', 'return_arrival': '2018-11-25 18:21:00', 'return_status': 'NORMAL'},

    {'booking_number': 'AAAAE', 'departure': '2018-11-26 17:53:00',
     'arrival': '2018-11-26 19:58:00', 'status': 'NORMAL', 'type': 'single'},

    {'booking_number': 'AAAAF', 'departure': '2018-11-26 17:53:00', 'arrival': '2018-11-26 19:58:00', 'status': 'NORMAL',
     'type': 'return', 'return_departure': '2018-11-27 18:58:00', 'return_arrival': '2018-11-27 21:03:00', 'return_status': 'NORMAL'},

    {'booking_number': 'AAAAG', 'departure': '2019-01-02 13:43:00',
     'arrival': '2019-01-02 14:56:00', 'status': 'DELAYED', 'type': 'single'},

    {'booking_number': 'AAAAH', 'departure': '2019-01-02 13:43:00', 'arrival': '2019-01-02 14:56:00', 'status': 'DELAYED',
     'type': 'return', 'return_departure': '2019-01-03 13:56:00', 'return_arrival': '2019-01-03 15:09:00', 'return_status': 'NORMAL'},

    {'booking_number': 'AAAAI', 'departure': '2019-01-04 15:00:00',
     'arrival': '2019-01-04 17:04:00', 'status': 'NORMAL', 'type': 'single'},

    {'booking_number': 'AAAAJ', 'departure': '2019-01-04 15:00:00', 'arrival': '2019-01-04 17:04:00', 'status': 'NORMAL',
     'type': 'return', 'return_departure': '2019-01-05 16:04:00', 'return_arrival': '2019-01-05 18:08:00', 'return_status': 'DELAYED'},

    {'booking_number': 'AAAAK', 'departure': '2019-01-06 18:23:00',
     'arrival': '2019-01-06 21:42:00', 'status': 'DELAYED', 'type': 'single'},

    {'booking_number': 'AAAAL', 'departure': '2019-01-06 18:23:00', 'arrival': '2019-01-06 21:42:00', 'status': 'DELAYED',
     'type': 'return', 'return_departure': '2019-01-07 20:42:00', 'return_arrival': '2019-01-08 00:01:00', 'return_status': 'NORMAL'},

    {'booking_number': 'AAAAM', 'departure': '2019-01-08 22:24:00',
     'arrival': '2019-01-09 01:06:00', 'status': 'DELAYED', 'type': 'single'},

    {'booking_number': 'AAAAN', 'departure': '2019-01-08 22:24:00', 'arrival': '2019-01-09 01:06:00', 'status': 'DELAYED',
     'type': 'return', 'return_departure': '2019-01-10 00:06:00', 'return_arrival': '2019-01-10 02:48:00', 'return_status': 'NORMAL'},

    {'booking_number': 'AAAAO', 'departure': '2019-01-11 04:10:00',
     'arrival': '2019-01-11 09:14:00', 'status': 'DELAYED', 'type': 'single'},

    {'booking_number': 'AAAAP', 'departure': '2019-01-11 04:10:00', 'arrival': '2019-01-11 09:14:00', 'status': 'DELAYED',
     'type': 'return', 'return_departure': '2019-01-12 08:14:00', 'return_arrival': '2019-01-12 13:18:00', 'return_status': 'CANCELLED'},

    {'booking_number': 'AAAAQ', 'departure': '2019-01-13 12:12:00',
     'arrival': '2019-01-13 17:10:00', 'status': 'DELAYED', 'type': 'single'},

    {'booking_number': 'AAAAR', 'departure': '2019-01-13 12:12:00', 'arrival': '2019-01-13 17:10:00', 'status': 'DELAYED',
     'type': 'return', 'return_departure': '2019-01-14 16:10:00', 'return_arrival': '2019-01-14 21:08:00', 'return_status': 'NORMAL'},

    {'booking_number': 'AAAAS', 'departure': '2019-01-15 20:10:00',
     'arrival': '2019-01-16 01:10:00', 'status': 'CANCELLED', 'type': 'single'},

    {'booking_number': 'AAAAT', 'departure': '2019-01-15 20:10:00', 'arrival': '2019-01-16 01:10:00', 'status': 'CANCELLED',
     'type': 'return', 'return_departure': '2019-01-17 00:10:00', 'return_arrival': '2019-01-17 05:10:00', 'return_status': 'NORMAL'},

    {'booking_number': 'AAAAU', 'departure': '2019-01-18 03:00:00',
     'arrival': '2019-01-18 06:50:00', 'status': 'NORMAL', 'type': 'single'},

    {'booking_number': 'AAAAV', 'departure': '2019-01-18 03:00:00', 'arrival': '2019-01-18 06:50:00', 'status': 'NORMAL', 'type': 'return', 'return_departure': '2019-01-19 05:50:00', 'return_arrival': '2019-01-19 09:40:00', 'return_status': 'NORMAL'}]


@app.route('/tickets', methods=['GET', 'POST'])
def get_tickets():
    if not request.args:
        return jsonify({'error': 'no-args-given'})
    if not check_args(request.args):
        return jsonify({'error': 'invalid-args'})
    res = []
    for ticket in tickets:
        if all(ticket.get(k) == v for k, v in request.args.items()):
            res.append(ticket)
    return jsonify({'tickets': res})

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
