# 使用Python调用coze

coze官方只提供了curl调用范例，未提供python调用接口。

一个有毅力的吃货花了些时间利用requests库进行了实现，封装成了coze这个python库。

支持流式输出，支持多轮对话。



## 一，安装coze库

```python
pip install coze 
```

## 二，使用范例


```python
import os 
from coze import Coze 
os.environ['COZE_API_TOKEN'] = 'pat_xxx'
os.environ['COZE_BOT_ID'] = "7362845197946257419"

```


```python
chat = Coze(api_token= os.environ['COZE_API_TOKEN'],
            bot_id = os.environ['COZE_BOT_ID'],
            max_chat_rounds=20,
            stream=True)

```

```raw
你好！有什么可以帮助你的？
register magic %%chat sucessed ...
```


可以使用__call__方法调用


```python
response = chat('北京最新的高级产品经理岗位有推荐吗')
```

```raw
call function: liepin-job_recommendation; args ={'address': '北京', 'jobName': '高级产品经理'}

北京近期推荐的高级产品经理岗位有以下几个，提供给对这一职业领域感兴趣的求职者：

1. 获客多 Hokdo公司提供产品经理和高级产品经理岗位，位于北京万泉河地区，产业属于计算机软件并且公司处于A轮融资阶段。提供的薪资为20-30k或25-35k，15个月薪资。招聘负责人是许先生。

2. 北京微云众网络科技有限公司招募的Futures Operations Director 职位涉及Web3 分布式产品运营，位于北京东四地区，公司规模100-499人，被标记具有较大的发展空间和国际化优势。

3. 美团是一个大规模的互联网生活服务公司，已上市，招聘的岗位是“企平-产品专家（工单平台方向）”和“财务科技-税务产品经理（海外税务方向）”，位于北京南法信，提出的薪资在30-60k和25-35k之间，均为15个月薪资。

以上职位都可以通过相应的跳转链接获取更详细的职位描述和申请方式。
```

在notebook中推荐使用jupyter魔法命令进行调用。


```python
%%chat
上海最近的算法岗位有推荐吗？给一下岗位简介和岗位链接。

```

```raw
call function: liepin-job_recommendation; args ={'address': '上海', 'jobName': '算法'}

以下是上海最近推荐的算法岗位列表：

1. **AIGC 算法工程师**：酷爱教育科技(上海)有限公司，薪水为14-22k·14薪，公司规模1-49人，位于上海-龙华。岗位链接：[点这里](https://www.liepin.com/job/1968037473.shtml)

2. **饿了么-NLP/知识图谱算法专家**：饿了么，薪水为10-20k，公司规模10000人以上，位于上海。岗位链接：[点这里](https://www.liepin.com/job/1967971499.shtml)

3. **车载智能系统开发工程师/专家**：芯安微众(上海)微电子技术有限公司，薪水为25-55k·14薪，公司规模100-499人，位于上海-淮海路。岗位链接：[点这里](https://www.liepin.com/job/1967961603.shtml)

4. **人工智能工程师/专家**：芯安微众(上海)微电子技术有限公司，薪水同上，公司规模和位置同上。岗位链接：[点这里](https://www.liepin.com/job/1967959705.shtml)

5. **大模型研究分析实习生**：美团，薪水为6-8k·15薪，公司规模10000人以上，位于上海。岗位链接：[点这里](https://www.liepin.com/job/1967761499.shtml)

岗位简介和具体要求可以通过链接进入了解。
```


```python
chat.history 
```


```raw
[('北京最新的高级产品经理岗位有推荐吗',
'目前在北京的高级产品经理岗位有以下推荐：\n\n1. 获客多 Hokdo提供产品经理职位，月薪范围20-30k，共15薪，位于北京-万泉河。\n   \n2. 获客多 Hokdo还有高级产品经理职位，月薪25-35k，15薪，同样位于北京。\n\n3. 北京微云众网络科技有限公司提供一个Web3分布式的Futures Operations Director职位，月薪20-50k，公司位于北京-东四。\n\n4. 美团在南法信有产品专家职位（工单平台方向），月薪范围30-60k，15薪。\n\n5. 美团在南法信还有税务产品经理职位，专注于海外税务方向，月薪25-35k，15薪。\n\n上述岗位涵盖了从初创A轮的获客多 Hokdo到已上市的大公司美团，提供了不同规模和发展阶段的职位选择。相关职位详情链接可见领英网站。'),
('上海最近的算法岗位有推荐吗？给一下岗位简介和岗位链接。\n',
'以下是上海最近推荐的算法岗位列表：\n\n1. **AIGC 算法工程师**：酷爱教育科技(上海)有限公司，薪水为14-22k·14薪，公司规模1-49人，位于上海-龙华。岗位链接：[点这里](https://www.liepin.com/job/1968037473.shtml)\n\n2. **饿了么-NLP/知识图谱算法专家**：饿了么，薪水为10-20k，公司规模10000人以上，位于上海。岗位链接：[点这里](https://www.liepin.com/job/1967971499.shtml)\n\n3. **车载智能系统开发工程师/专家**：芯安微众(上海)微电子技术有限公司，薪水为25-55k·14薪，公司规模100-499人，位于上海-淮海路。岗位链接：[点这里](https://www.liepin.com/job/1967961603.shtml)\n\n4. **人工智能工程师/专家**：芯安微众(上海)微电子技术有限公司，薪水同上，公司规模和位置同上。岗位链接：[点这里](https://www.liepin.com/job/1967959705.shtml)\n\n5. **大模型研究分析实习生**：美团，薪水为6-8k·15薪，公司规模10000人以上，位于上海。岗位链接：[点这里](https://www.liepin.com/job/1967761499.shtml)\n\n岗位简介和具体要求可以通过链接进入了解。')]
```


## 三，详细教程

参考 本项目下的 coze_tutorial.ipynb 文件
