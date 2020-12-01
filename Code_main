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
def minus(*args):
    values_list = [arg.split('.') for arg in args if type(arg) == str and arg[0] == '-']
    int_sum = sum([int(args[0]) for args in values_list]) * -1

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
    total_sum = ('-' + total_sum)
    return total_sum

def plum(*args):
    p_value = plus(*args).split('.')
    m_value = minus(*args).split('.')
    flt_v = [p_value[1], m_value[1]]
    max_l = len(max(flt_v, key=len))
    flt_v = list(map(lambda x: x.ljust(max_l, '0'), flt_v))
    p_value = int(p_value[0] + flt_v[0])
    m_value = int(m_value[0] + flt_v[1])
    pre_total = str(sum([p_value, m_value]))
    total = pre_total[:-max_l] + '.' + pre_total[-max_l:]
    if total[0] == '-' and total[1] == '.':
        total = total[0] + '0' + total[1:]
    if total[0] == '.' and total[1] == '-':
        total = '-0.' + total[2:]
    if total[0] == '.':
        total = '0' + total[:]
    return total
