class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort()
        trainers.sort()
        p, t, match = len(players) - 1, len(trainers) - 1, 0
        while p >= 0 and t >= 0:
            if players[p] <= trainers[t]:
                match += 1
                p -= 1
                t -= 1
            elif players[p] > trainers[t]:
                p -= 1

        return match
