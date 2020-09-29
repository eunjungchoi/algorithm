# Implement the class UndergroundSystem that supports three methods:
#
# 1. checkIn(int id, string stationName, int t)
#
# A customer with id card equal to id, gets in the station stationName at time t.
# A customer can only be checked into one place at a time.
# 2. checkOut(int id, string stationName, int t)
#
# A customer with id card equal to id, gets out from the station stationName at time t.
# 3. getAverageTime(string startStation, string endStation)
#
# Returns the average time to travel between the startStation and the endStation.
# The average time is computed from all the previous traveling from startStation to endStation that happened directly.
# Call to getAverageTime is always valid.
# You can assume all calls to checkIn and checkOut methods are consistent. That is, if a customer gets in at time t1 at some station, then it gets out at time t2 with t2 > t1. All events happen in chronological order.
#
#
#
# Example 1:
#
# Input
# ["UndergroundSystem","checkIn","checkIn","checkIn","checkOut","checkOut","checkOut","getAverageTime","getAverageTime","checkIn","getAverageTime","checkOut","getAverageTime"]
# [[],[45,"Leyton",3],[32,"Paradise",8],[27,"Leyton",10],[45,"Waterloo",15],[27,"Waterloo",20],[32,"Cambridge",22],["Paradise","Cambridge"],["Leyton","Waterloo"],[10,"Leyton",24],["Leyton","Waterloo"],[10,"Waterloo",38],["Leyton","Waterloo"]]
#
# Output
# [null,null,null,null,null,null,null,14.00000,11.00000,null,11.00000,null,12.00000]
#
# Explanation
# UndergroundSystem undergroundSystem = new UndergroundSystem();
# undergroundSystem.checkIn(45, "Leyton", 3);
# undergroundSystem.checkIn(32, "Paradise", 8);
# undergroundSystem.checkIn(27, "Leyton", 10);
# undergroundSystem.checkOut(45, "Waterloo", 15);
# undergroundSystem.checkOut(27, "Waterloo", 20);
# undergroundSystem.checkOut(32, "Cambridge", 22);
# undergroundSystem.getAverageTime("Paradise", "Cambridge");       // return 14.00000. There was only one travel from "Paradise" (at time 8) to "Cambridge" (at time 22)
# undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.00000. There were two travels from "Leyton" to "Waterloo", a customer with id=45 from time=3 to time=15 and a customer with id=27 from time=10 to time=20. So the average time is ( (15-3) + (20-10) ) / 2 = 11.00000
# undergroundSystem.checkIn(10, "Leyton", 24);
# undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 11.00000
# undergroundSystem.checkOut(10, "Waterloo", 38);
# undergroundSystem.getAverageTime("Leyton", "Waterloo");          // return 12.00000
# Example 2:
#
# Input
# ["UndergroundSystem","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime","checkIn","checkOut","getAverageTime"]
# [[],[10,"Leyton",3],[10,"Paradise",8],["Leyton","Paradise"],[5,"Leyton",10],[5,"Paradise",16],["Leyton","Paradise"],[2,"Leyton",21],[2,"Paradise",30],["Leyton","Paradise"]]
#
# Output
# [null,null,null,5.00000,null,null,5.50000,null,null,6.66667]
#
# Explanation
# UndergroundSystem undergroundSystem = new UndergroundSystem();
# undergroundSystem.checkIn(10, "Leyton", 3);
# undergroundSystem.checkOut(10, "Paradise", 8);
# undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.00000
# undergroundSystem.checkIn(5, "Leyton", 10);
# undergroundSystem.checkOut(5, "Paradise", 16);
# undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 5.50000
# undergroundSystem.checkIn(2, "Leyton", 21);
# undergroundSystem.checkOut(2, "Paradise", 30);
# undergroundSystem.getAverageTime("Leyton", "Paradise"); // return 6.66667
#
#
# Constraints:
#
# There will be at most 20000 operations.
# 1 <= id, t <= 10^6
# All strings consist of uppercase, lowercase English letters and digits.
# 1 <= stationName.length <= 10
# Answers within 10^-5 of the actual value will be accepted as correct.
from collections import defaultdict


class UndergroundSystem:
    """
    다음 세 가지 방법을 지원하는 UndergroundSystem 클래스를 구현하십시오.

    1. 체크인(int ID, 문자열 스테이션 이름, int t)

    ID와 동일한 ID 카드를 소지한 고객이 시간 t에 스테이션 이름을 입력한다.
    고객은 한 번에 한 곳에만 체크인할 수 있다.

    2. 체크아웃(int ID, 문자열 스테이션 이름, int t)

    ID와 동일한 ID 카드를 소지한 고객이 시간 t에 스테이션 이름에서 하차한다.

    3. getAverageTime(startStation, string endStation)

    startStation과 endStation 사이를 이동하는 평균 시간을 반환한다.
    평균 시간은 직접 발생한 startStation에서 endStation까지의 모든 이전 여행에서 계산
    평균 시간을 얻기 위한 호출은 항상 유효하다.

    체크인 및 체크아웃 방법이 모두 일관된다고 가정할 수 있다. 즉, 어떤 역에서 손님이 t1 시간에 들어오면 t2 > t1로 t2 시간에 빠져나간다는 것이다. 모든 사건은 연대순으로 일어난다.
    """

    def __init__(self):
        self.in_out_table = {}  # id: (start_station, in_time)
        self.station_dist = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_out_table[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, in_time = self.in_out_table[id]
        self.station_dist[(start_station, stationName)].append(t - in_time)  # (start, end): [period, ]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        lst = self.station_dist[(startStation, endStation)]
        return sum(lst) / len(lst)

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)


# 52 / 52 test cases passed.
# Status: Accepted
# Runtime: 236 ms
# Memory Usage: 24.6 MB
#
# Your runtime beats 98.31 % of python3 submissions.
# Your memory usage beats 9.25 % of python3 submissions.
