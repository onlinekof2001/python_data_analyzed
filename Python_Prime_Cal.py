'''
4 ways to get the primes t
prime is a series of integer numbers large than 1 and can only divisible by 1 and itself.
'''
# 穷举法, 取2到n个数, 能被2到n - 1整除的都被排除在外 range(start, stop[, step]), 不包含stop

class Calculator(object):
    def prime(self, n):
        m = 0
        for i in range(2, n):
            j = 2
            for j in range(2, i-1):
                if i % j == 0:
                    break
            else:
                print(i, "is prime")
                m += 1
        return m

obj = Calculator();
obj.prime(20)

# 穷举法, 取除数的一半 print(int(11/2)), 因为任何数由两个因数相乘得来的, 如：15, 1*15, 3*5. 可以看到有一半的因数落在15/2的前面

class Calculator(object):
    def prime(self, n):
        m = 0
        for i in range(2, n):
            j = 2
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                print(i, "is prime")
                m += 1
        return m

# 再次变形, 任何数的因数必有一个小于√x和一个大于√x的存在, 如：√81=9, 1*81, 3*27, 9*9

class Calculator(object):
    def prime(self, n):
        m = 0
        for i in range(2, n):
            j = 2
            for j in range(2, int(i**0.5)+1):
                if i % j == 0:
                    break
            else:
                print(i, "is prime")
                m += 1
        return m

#对于任意一个大于3的合数（除了1和自身外，还能被其他整数整除的数）, 我们都可以将其拆分成至少包含一个质数的因子相乘, 例如：20=2*10（2是质数）; 45=5*9; 
#利用此点，我们可以采用遍历小于这个数的所有质数来确认这个数是不是质数。

class Calculator(object):
    def prime(self, n):
        if n <= 2:
            return 0
        else:
            prime_list = list()
            prime_list.append(2)  # 先将2加入到要遍历的列表中
            for x in range(3, n):
                y = False  
                for y in prime_list:
                    if x % y == 0: # 对小于n的x进行遍历，当某个数整除为0时，不执行添加列表操作
                        y = False
                        break
                    else:
                        y = True
                if y is True:
                    prime_list.append(x)  # 对小于x的质数进行遍历后，没有能整除的质数，则这个数也是质数
            return len(prime_list)

'''
埃拉托斯特尼筛法；使用的原理是从2开始，将每个素数的各个倍数，标记成合数。一个素数的各个倍数，是一个差为此素数本身的等差数列。此为这个筛法和试除法不同的关键之处，后者是以素数来测试每个待测数能否被整除。(摘自维基百科)

具体的实现方式：

        先留下第一个素数2，将所有2的倍数的合数全部剔除；下一个素数3，将3的倍数的所有合数全部剔除；接着用5进行筛选剔除；当所要使用的素数的平方大于设定值时，停止筛选，则剩下的所有数均为素数。

例如：求出小于120的所有素数，依次使用2,3,5,7进行筛选，当到11时，11*11>120,停止筛选，剩余数即为质数。
'''
class Calculator(object):
    def prime(self, n):
        if n <= 2:
            return 0
        is_right = [True] * n
        is_right[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if is_right[i]:
                for j in range(i * i, n, i):
                    is_right[j] = False
        m = 0
        for x in range(2, n):
            if is_right[x]:
                m += 1
        return m