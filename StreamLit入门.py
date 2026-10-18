#Streamlit可以简单进行web开发
import streamlit as st
from streamlit import text_input


st.set_page_config(
    page_title="哇是固定翼入门",
    page_icon="😍",
    layout="centered",
    #侧边栏控制 但是这里没有侧边栏
    initial_sidebar_state="expanded",
    #超链接跳转
    menu_items={
        'Get Help': 'https://www.yuanshen.com/#/',
        'Report a bug': "https://www.yuzu-soft.com/products/senren/index.html",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# 'Get Help': 'https://www.extremelycoolapp.com/help',
#         'Report a bug': "https://www.extremelycoolapp.com/bug",
#         'About': "# This is a header. This is an *extremely* cool app!"


#设置标题 一级标题 二级标题
st.title('空战入门')
st.header('固定翼篇')
st.subheader('作战篇')

#引入文字write方法
st.write(
    ''' 一、起飞与巡航阶段
1. 起飞前完成飞控自检、航电系统校准、武器保险确认；
2. 低空阶段避免大角度机动，防止气流扰动引发失速；
3. 巡航时刻监控剩余燃油，预留至少30%燃油用于交战与返航。
'''
)
st.write(
    '''二、超视距（BVR）空战
1. 保持雷达间歇扫描模式，持续锁定目标同时降低自身电磁暴露概率；
2. 发射中距弹后不要直线脱离，执行侧向机动规避敌方反击导弹；
3. 持续观察敌我距离，合理分配导弹数量，避免一次性打光所有远程弹药。
'''
)
st.write(
    '''三、近距离缠斗（WVR）
1. 优先控制高度与能量，不要盲目持续拉杆拉升，防止速度骤降进入失速；
2. 紧盯敌方机动趋势，预判转向路线，不要跟随对手做同向持续盘旋；
3. 进入导弹射击窗口前确认敌我识别（IFF），杜绝误击友机。
'''
)
st.write(
    '''四、防御机动与应急处置
1. 遭遇来袭导弹：同步执行侧向机动+热诱弹/干扰箔条投放，单一干扰手段极易被抗干扰制导过滤；
2. 战机出现引擎喘振时立刻减小仰角，避免空中停车；
3. 机身受损、操控响应异常，第一时间评估返航可行性，不要强行继续交战。
'''
)
#如何插入图片与视频
#图片
st.image('./STresource/img.png')
#视频
st.video('./STresource/video.mp4')
#LOGO
#st.logo(...)
#表格
table_data = {
    '型号':['A10','F35','F16'],
    '类型':['攻击机','多用途战机','空优机'],
    '特点':['‘空中堡垒’，装甲厚重，火力强大','隐身，高速飞行，垂直起降','空战特化，速度快火力猛']
}
st.table(table_data)

name = text_input('型号')
st.write('飞机型号为{}'.format(name))
#密码（额外参数）
name = text_input('密码',type="password")
st.write('密码为{}'.format(name))
#单选按钮(提示文本，[选项1，选项2...])
gender = st.radio('请选择性别',['男','女','第三性'])
st.write('您的性别为{}'.format(gender))