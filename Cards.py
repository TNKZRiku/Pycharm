#需求 三类卡 打出的时候抽牌 未抽到的卡权重加一 打出的卡返回牌堆并权重重置为一
#普通卡 n回合内不会被抽到的卡 打出时抽取特定卡牌的卡
#思路 设置三类卡的字典 属性：编号 卡牌效果 特殊效果 权重 卡牌名

import random

#构建卡组
Hoori_dict = {
    'a1':['释放多余的法力进行攻击',
          False,1,'魔法狙击'],
    'a2':['以心灵感应覆盖我方所有角色 使得所有角色攻击力+10% 防御力+10%',
          False,1,'心灵感应'],
    'a3':['释放法力为火焰魔法 攻击指定目标',
          False,1,'烈焰侵袭'],
    'a4':['使指定敌方目标失去20%生命值 并为自己回复15%生命值',
          False,1,'暗影魔法'],
    'a5':['去寻找丢失的行李箱 5回合内无法抽取该卡牌',
          [1,5],1,'守护意志'],
    'a6':['解放天使之力 为我方角色回复20%生命值并解除1个随机负面效果 释放过后3回合内无法抽取该卡牌',
          [1,3],1,'天使之力'],
    'a7':['觉醒魔王之力 并抽取一张‘魔王之力',
          2,1,'前世复苏'],
    'a8':['对敌方所有角色造成30%生命值的伤害',
          3,1,'魔王之力']
}

#卡组格式为 {...,'编号':['技能描述',特殊效果,权重,'卡牌名称'],...}
#可以自行添加新的卡片
#特殊效果：False为无效果
#        1 为n个回合内不会抽到 n回合后权重重置为1 用列表表示[1，n]
#        2 为抽取额外的卡牌
#        3 无法被抽中的卡牌
#2 -> 3的抽取规则在下面

#构建编号与卡牌对应的字典 -> 丛雨字典

Murasame_dict = {
    '魔法狙击':'a1',
    '心灵感应':'a2',
    '烈焰侵袭':'a3',
    '暗影魔法':'a4',
    '守护意志':'a5',
    '天使之力':'a6',
    '前世复苏':'a7',
    '魔王之力':'a8'
}

#上文提到的抽牌对应字典 -> 柚子字典
Yuzu_dict = {
    '前世复苏':'魔王之力'
}
#格式:{...,'打出的牌':'抽取的牌',...}

#历史遗留问题
#手中的牌 -> 祟神字典
Nozomi_dict = {}
#仅第一次抽牌用到的蕾娜数
Rena_num = 0
#构建1类特殊卡列表 -> 小春列表
Koharu_list = []
#控制程序终止的字句 -> 华乃语句 别问 问就是忘了芦花名字了
Kano_num = 0
#记录回合的数字 -> 天梨数
Ameri_num = 1

#开局的时候抽取3张牌
while True:
    co1 = 0
    if not Rena_num:
        while co1 < 3:
            rand1 = random.randint(1,8)
            str1 = 'a'+str(rand1)
            if str1 not in Nozomi_dict and not Hoori_dict[str1][1] == 3:
                Nozomi_dict['a'+str(rand1)] = Hoori_dict.get(str1)
                co1 += 1

    #增加牌堆的权重 将手中的卡牌权重设为0
    for i in Hoori_dict:
        Hoori_dict[i][2] += 1
    for i in Nozomi_dict:
        if i in Hoori_dict:
            Hoori_dict[i][2] = 0

#仅在第一回合生效
    if not Rena_num:
        print('\n')
        print('游戏开始！输入Ciallo退出~你的卡组:')
        for i in Nozomi_dict:
            print(Nozomi_dict[i][3],':',Nozomi_dict[i][0])

    #出牌阶段
    print('第{}回合！'.format(Ameri_num),end='')
    inp1 = input('你要采取的行动：')
    if inp1 == 'Ciallo':
        break
    Act1 = Murasame_dict[inp1]
    print('\n')
    print('你使用了{}'.format(Nozomi_dict[Act1][3]))
    print('\n')
    #立刻删掉出的牌
    del Nozomi_dict[Act1]
    Hoori_dict[Act1][2] = 1
    #print(Nozomi_dict)
    #1特殊卡的限制
    #如果是1特殊卡 则把对应的列表加进小春列表
    try:
        if Hoori_dict[Act1][1][0] == 1:
            Koharu_list.append([Act1,Hoori_dict[Act1][1][1]])
            #print(Koharu_list)
    #我知道这种写法很屎但是我没办法
    except:
        pass




    #权重抽卡阶段
    #构建屎山列表
    #重构小春列表
    for i in Koharu_list:
        Koharu_str = i[0]
        Koharu_num = i[1]
        if Koharu_num == 0:
            Koharu_list.pop(i)
            Hoori_dict[Koharu_str][2] = 1
        else:
            Koharu_num -= 1
            Hoori_dict[Koharu_str][2] = 0

    #构建屎山列表 -> 芳乃列表
    #最不需要操作的堆数据
    Yoshino_list = []
    for i in Hoori_dict:
        if not Hoori_dict[i][1] == 3:
            for num in range(int(Hoori_dict[i][2])):
                Yoshino_list.append(i)
    #随机数抽卡
    #随机数字载体 -> 茉子数
    Hitachi_num = random.randint(0,int(len(Yoshino_list))-1)
    #print(Hitachi_num)
    Hitachi_card = Yoshino_list[Hitachi_num]
    #print(Hitachi_card)
    Nozomi_dict[Hitachi_card] = Hoori_dict[Hitachi_card]
    #2特殊卡的额外抽卡
    #若为2类特殊卡 则根据列表规则抽卡
    if Hoori_dict[Act1][1] == 2:
        #下面这行或许你会看得头晕 头晕是正常的 我写的时候我也头晕
        Nozomi_dict[Murasame_dict[Yuzu_dict[str(Hoori_dict[Act1][3])]]] = Hoori_dict[Murasame_dict[Yuzu_dict[str(Hoori_dict[Act1][3])]]]
#每次循环结束的时候输出卡牌
    print('你的卡组:')
    Rena_num += 1
    for i in Nozomi_dict:
        print(Nozomi_dict[i][3],':',Nozomi_dict[i][0])
    #print('\n')
    Ameri_num += 1
    #注释掉的print按说可以删了 但是我不敢













