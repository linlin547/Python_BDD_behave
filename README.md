# Python-BDD-behave
1.关键词
-----
  * Feature （功能）
  * Scenario （场景）
  * Scenario Outline （场景大纲-即多个Scenario）
  * Given （假如）
  * When （当）
  * Then （那么）
  * Environment （环境变量）
    * 在某些特定代码执行之前运行
    * 比如在一个 Feature 开始或之后执行
    * 在一个 Scenario 开始或之后执行
    * 在一个 Step 开始或之后执行

2.工程结构
-----
  * ![feature](https://github.com/linlin547/Python_BDD_behave/blob/master/image/dir.png)


3.behave 示例
-----
  * 新建Behave_pro目录
  * 新建/Behave_pro/features
  * 新建/Behave_pro/features/steps
  * 新建/Behave_pro/features/test.feature文件
    * ![feature](https://github.com/linlin547/Python_BDD_behave/blob/master/image/feature.png)
  * 新建/Behave_pro/features/steps/test.py 文件
    * ![step](https://github.com/linlin547/Python_BDD_behave/blob/master/image/step.png)

4.behave 执行
-----
  * 进入Behave_pro目录,输入 behave,运行结果
    * ![result](https://github.com/linlin547/Python-BDD-behave/image/step.png)