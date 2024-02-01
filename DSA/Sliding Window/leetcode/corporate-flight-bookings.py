class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        seats = [0] * (n + 1)

        for first, second, seat in bookings:
            seats[first - 1] += seat
            seats[second] -= seat

        for idx in range(1, n):
            seats[idx] += seats[idx - 1]

        seats.pop()
        return seats