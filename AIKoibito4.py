#基于StreamLit实现AI聊天
#Streamlit可以简单进行web开发

import os
import json
import datetime
import streamlit as st
from openai import OpenAI
import BlueArchiveModels
import HamidashiModels

###########################################################################
#函数配置阶段

#定义当前时间函数
def random_time():
    return datetime.datetime.now().strftime("%Y_%m_%d_%H_%M_%S")

#设置一个保存函数
def save_sessions(name,persona,st_messages,key):
    if st_messages:
        #print("写入文件：{}".format(key))
        session_data = {
                        'name': name,
                        'persona': persona,
                        'message': st_messages
                    }
        # 创建文件夹
        if not os.path.exists('D:/李空的下载/导出的数据/Sessions'):
            os.mkdir('D:/李空的下载/导出的数据/Sessions')
            # 保存会话文件
        with open('D:/李空的下载/导出的数据/Sessions/{}.json'.format(key), 'w',
                    encoding='utf-8') as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

#加载历史对话的函数
def load_sessions():
    sessions_list = []
    #加载所有文件目录
    if os.path.exists('D:/李空的下载/导出的数据/Sessions'):
        file_list = os.listdir('D:/李空的下载/导出的数据/Sessions')
        for filename in file_list:
            if filename.endswith('.json'):
                show_name = filename[:-5]
                sessions_list.append(show_name)
        #排序
    sessions_list.sort(reverse=True)
    return sessions_list

#加载指定会话
def load_session(session_name):
    try:
        if os.path.exists('D:/李空的下载/导出的数据/Sessions/{}.json'.format(session_name)):
            print('vv')
            with open('D:/李空的下载/导出的数据/Sessions/{}.json'.format(session_name),'r',encoding='utf-8') as f:
                session_data = json.load(f)
                st.session_state.messages.clear()
                st.session_state.current_session = session_name
                st.session_state.name = session_data['name']
                st.session_state.persona = session_data['persona']
                st.session_state.messages.append(session_data['message'])
                for ii in session_data['messages']:
                    st.session_state.messages.extend(ii)


                # st.session_state.messages = session_data['message']
                # st.session_state.name = session_data['name']
                # st.session_state.persona = session_data['persona']
                # st.session_state.current_session = session_name
    except Exception as e:
        st.error('加载失败,')

#删除函数
def delete_session(session):
    try:
        if os.path.exists('D:/李空的下载/导出的数据/Sessions/{}.json'.format(session)):
            os.remove('D:/李空的下载/导出的数据/Sessions/{}.json'.format(session))
            if session == st.session_state.current_session:
                st.session_state.messages = []
                st.session_state.current_session = None
    except:
        print('删除失败！')

###########################################################################
#整体配置阶段

#主页面配置
st.set_page_config(
    page_title="AI聊天",
    page_icon="❄️",
    layout="wide",
    #侧边栏控制 但是这里没有侧边栏
    initial_sidebar_state="expanded",
    #超链接跳转
    menu_items={}
)
#大标题
st.title("AI聊天")
promote = st.chat_input(placeholder="开始虚拟世界的旅程！")

#创建所需的空容器
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'current_session' not in st.session_state:
    st.session_state.current_session = random_time()

#左侧侧边栏
#with 是一个上下文管理器 就不用给每个元素加上sidebar了
with st.sidebar:
    #模型选择模块
    st.subheader('模型选择')
    model_select = st.radio(
    label = ' ',
    options = ['爱丽丝','锦亚澄'],
    horizontal = False)

    if model_select == '锦亚澄':
        model = HamidashiModels.Asumi
    else:
        model = BlueArchiveModels.Arisu

    name = model.Name
    persona = model.Persona

    #保存历史会话
    st.subheader('设置')
    bt = st.button('新建会话',width='stretch',icon='✏️')
    if bt:
        if st.session_state.messages:
            save_sessions(name,persona,st.session_state.messages,st.session_state.current_session)
            #创建新会话
            st.session_state.messages = []
            st.session_state.current_session = random_time()
            save_sessions(name,persona,st.session_state.messages,st.session_state.current_session)
            st.rerun()

    #历史会话模块 用column模块实现一行多个按钮
    st.text('历史会话')
    sessions_list = load_sessions()
    for session in sessions_list:
        co1,co2 = st.columns([4,1])
        with co1:
                #加载会话
            if st.button(session,width='stretch',icon='🎬',key=session):
                load_session(session)
                st.rerun()
            #删除会话
        with co2:
            if st.button('',icon='❌️',width='stretch',key='delete_{}'.format(session)):
                delete_session(session)
                st.rerun()
    #分割线
    st.divider()

    #文本域展示 无实际作用 仅用来练习
    name1 = st.text_input('文本',placeholder='请输入文本',value=model_select)
    if name1:
        st.session_state.textarea = name1
    st.write(name1)

    #name就是返回值
    name2 = st.text_area('文本',placeholder='请输入文本',value='滚木')
    if name2:
        st.session_state.textarea = name2
    st.write(name2)

if promote:
    # 保存结果1
    st.session_state.messages.append({'role': 'user', 'content': promote})

    #通过把历史会话保存在session中 遍历输出来达到多轮对话
print('msg',st.session_state.messages)
for i in st.session_state.messages:
    for iii in i:
        if iii['role'] == 'user':
            st.chat_message('user').write(iii['content'])
        else:
            st.chat_message('assistant').write(iii['content'])

##########################################################################
#运行阶段

if promote:
    # 创建交互客户端
    client = OpenAI(
        api_key=os.environ.get('DEEPSEEK_API_KEY'),
        base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", 'content': persona},
            *st.session_state.messages
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )

#流式输出
    response_messages = st.empty()
    full_resp = ''

    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content =  chunk.choices[0].delta.content
            full_resp += content
            response_messages.chat_message('assistant').write(full_resp)
    #保存结果2
    st.session_state.messages.append({'role':'system', 'content': full_resp})

    save_sessions(name,persona,st.session_state.messages,st.session_state.current_session)

############################################################################
#后门
print('总内容：',st.session_state.messages)