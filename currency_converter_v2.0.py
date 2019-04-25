"""
    作者：jamke
    功能：汇率兑换
    版本：2.0
    日期：2019.03.05
    新增功能：根据输入判断是人民币还是美元，进行相应的转换计算
"""

# 汇率
USD_VS_RMB = 6.77

# 带单位的货币的输入
currency_str_value = input('请输入带单位的货币金额：')

# 获取货币单位
currency_unit = currency_str_value[-3:]

# print(currency_unit)

# # 将字符串转换为数字，获取货币数值
currency_value = eval(currency_str_value[:-3])

# 判断货币单位，并根据货币单位
if currency_unit == 'CNY':
    # 输入的是人民币（RMB）
    usd_value = currency_value / USD_VS_RMB

    # 输出结果
    print('美元（USD）金额是：', usd_value)
elif currency_unit == 'USD':
    # 输入的是美元（USD）
    rmb_value = currency_value * USD_VS_RMB

    # 输出结果
    print('人民币（CNY）金额是：', rmb_value)
else:
    # 其他情况
    print('目前版本尚不支持该种货币')
