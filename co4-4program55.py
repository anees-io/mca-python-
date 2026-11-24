class Time:
    def __init__(self, hour, minute, second):
        self.__hour = hour
        self.__minute = minute
        self.__second = second

    def __add__(self, other):
        sec = self.__second + other.__second
        minute = self.__minute + other.__minute
        hour = self.__hour + other.__hour

        minute = minute + sec // 60
        sec = sec % 60

        hour = hour + minute // 60
        minute = minute % 60

        return Time(hour, minute, sec)

    def display(self):
        print(self.__hour, ":", self.__minute, ":", self.__second)


h1 = int(input("Enter hour of first time: "))
m1 = int(input("Enter minute of first time: "))
s1 = int(input("Enter second of first time: "))

h2 = int(input("Enter hour of second time: "))
m2 = int(input("Enter minute of second time: "))
s2 = int(input("Enter second of second time: "))

t1 = Time(h1, m1, s1)
t2 = Time(h2, m2, s2)

t3 = t1 + t2

print("Sum of two times:")
t3.display()
