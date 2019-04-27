"""
    作者：jamke
    功能：汇率兑换
    版本：3.0
    日期：2019.03.06
    4.0新增功能：将汇率兑换功能封装到函数
"""


def convert_currency(in_money, ex_rate):
    """
        汇率兑换
    """
    result = in_money*ex_rate
    return result


# 汇率
USD_VS_RMB = 6.77

# 带单位的货币的输入
currency_str_value = input('请输入带单位的货币金额：')

# 获取货币单位
currency_unit = currency_str_value[-3:]

# 将字符串转换为数字，获取货币数值
currency_value = eval(currency_str_value[:-3])

# 判断货币单位，并根据货币单位
if currency_unit == 'CNY':
    exchange_rate = 1/USD_VS_RMB

elif currency_unit == 'USD':
    exchange_rate = USD_VS_RMB

else:
    exchange_rate = -1

if exchange_rate != -1:
    # 调用函数
    currency_value = convert_currency(currency_value, exchange_rate)
    print('转换后的金额为：', currency_value)
else:
    print('目前版本暂不支持该货币！')
