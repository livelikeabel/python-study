class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result


cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3))
print(cal1.add(3))
print(cal1.add(3))


# self에는 setdata메서드를 호출한 객체 a가 자동으로 전달된다.
# 파이썬 메서드의 첫 번째 매개변수 이름은 관례적으로 self를 사용한다.
# 파이썬 메서드 이름으로 __init__을 사용하면 이 메서드는 생성자가 된다. 객체가 생성되는 시점에 자동으로 호출된다.
class FourCal:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def add(self):
        result = self.first + self.second
        return result
    def mul(self):
        result = self.first * self.second
        return result

a = FourCal(4,2)


# 클래스를 상속하기 위해서는 다음처럼 클래스 이름 뒤 괄호 안에 상속할 클래스 이름을 넣어주면 된다.
# class 클래스 이름(상속할 클래스 이름)
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(4, 2)
a.add()


# 상속을 하는 이유
# 기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용한다.
# 기존 클래스가 라이브러리 형태로 제공되거나 수정이 허용되지 않는 상황이라면 상속을 사용해야 한다.


# 메서드 오버라이딩
# FourCal클래스에 있는 메서드를 동일한 이름으로 다시 만드는 것을 메서드 오버라이딩이라고 한다.
class SafeFourCal(FourCal):
    def div(self):
        if self.second == 0:
            return 0
        else:
            return self.first / self.second


# 클래스 변수
# 클래스 변수는 클래스로 만든 모든 객체에 공유되는 특징이 있다.
class Family:
    lastname = "김"








