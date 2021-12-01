"""Algorithm for accurate adding positive decimals in Python"""

def shift_point(arg):
        arg = str(arg)
        arg_new = arg.split('.')
        return arg_new


def plus(*args):
        values_list = [arg.split('.') for arg in args if type(arg) == str and arg[0] != '-']
        int_sum = sum([int(args[0]) for args in values_list])

        flt_value = [args[1] for args in values_list]
        if not flt_value:
            return '0.0'
        max_len = len(max(flt_value, key=len))
        flt_value = list(map(lambda x: x.ljust(max_len, '0'), flt_value))
        flt_sum = sum([int(i) for i in flt_value])

        flt_remainder = str(flt_sum)
        if len(flt_remainder) < max_len:
            flt_remainder = flt_remainder.zfill(max_len)
        int_remainder = 0
        if len(str(flt_sum)) > len(flt_value[0]):
            length = len(flt_value[0])
            flt_remainder = str(flt_sum)[-length:]
            int_remainder = int(str(flt_sum)[:-length])
        if flt_remainder[-1] == '0':
            flt_remainder = flt_remainder.rstrip('0')
        if len(flt_remainder) == 0:
            flt_remainder = '0'

        int_sum += int_remainder
        total_sum = '.'.join([str(int_sum), flt_remainder])
        return total_sum

m_sum = plus('0.043', '777.45', '0.000000000000340054')
m_sum1 = plus('25.000405', '0.020328932013981023091')
m_sum2 = plus('4.1', '5.800', '65.01', '1.1', '1.99')

print(m_sum)  # 777.493000000000340054
print(m_sum1)  # 25.020733932013981023091
print(m_sum2)  # 78.0

print(-0.043 - 777.45 - 0.000000000000340054)  # 777.4930000000004
print(-25.000405 - 0.020328932013981023091)  # 25.020733932013982
print(- 4.1 - 5.800 - 65.01 - 1.1 - 1.99)  # 77.99999999999999
