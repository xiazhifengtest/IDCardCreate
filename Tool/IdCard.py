import random

print('工具进攻内部使用，请勿外传\n')
print('开始生成\n')
def generate_id_check_code(id_number_prefix):
    weights = [int(x) for x in id_number_prefix]
    factors = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    total = sum(weight * factor for weight, factor in zip(weights, factors))
    remainder = total % 11
    check_code_mapping = {0: '1', 1: '0', 2: 'X', 3: '9', 4: '8', 5: '7', 6: '6', 7: '5', 8: '4', 9: '3', 10: '2'}
    check_code = check_code_mapping[remainder]
    return check_code


def generate_id_number():
    # 随机生成地区码
    region_code = str(random.randint(110000, 659000))

    # 随机生成生日
    year = str(random.randint(1950, 2022))
    month = str(random.randint(1, 12)).zfill(2)
    day = str(random.randint(1, 28)).zfill(2)

    # 随机生成顺序号
    sequence = str(random.randint(1, 999)).zfill(3)
    #前17位数
    id_no=region_code + year + month + day + sequence
    check_code=generate_id_check_code(id_no)
    # 生成校验位
    # check_code = str(random.randint(0, 9))
    # 组合生成身份证号码
    idcard = id_no+check_code
    return idcard

# for i in range(11):
#     generate_id_number()
# print('\n生成完成\n')
# input('Press any key to exit')



