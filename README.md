# Archwing Bookings
API for [Archwing](https://github.com/causztic/archwing)

## Endpoints
- `/tickets`: Returns all tickets
- `/ticket`: Returns a particular ticket based on query parameters

## Fields

| Fields          | Description                                           |
|-----------------|-------------------------------------------------------|
| Booking number  | 5-character alphanumeric                              |
| Departure       | Departure time in number of seconds since Unix epoch  |
| Arrival         | Arrival time in number of seconds since Unix epoch    |
| Status          | 0 - NORMAL, 1 - DELAYED, 2 - CANCELLED                |
| Return          | 0 - SINGLE, 1 - ROUNDTRIP                             |
