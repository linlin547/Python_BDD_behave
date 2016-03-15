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
    * before_step(context, step), after_step(context, step)
        * 在这里面的脚本会在每一个步骤之前，之后执行

    * before_scenario(context, scenario), after_scenario(context, scenario)
        *在这里面的脚本会在每一个场景之前，之后执行

    * before_feature(context, feature), after_feature(context, feature)
        * 在这里面的脚本会在每一个feature之前，之后执行

    * before_tag(context, tag), after_feature(context, tag)
        * 在脚本里面可以设置tag(这个之后会介绍)，这里面的脚本会在含有tag的模块里面之前，之后执行

    * before_all(context), after_all(context)
        *这里面的脚本会在整个脚本开始之前，之后执行

2.工程结构
-----
  * ![feature](https://github.com/linlin547/Python_BDD_behave/blob/master/image/dir.png)


3.behave 示例
-----
  * 新建Behave_pro目录
  * 新建/Behave_pro/features
  * 新建/Behave_pro/features/steps
  * 新建/Behave_pro/features/test.feature 场景描述
    * ![feature](https://github.com/linlin547/Python_BDD_behave/blob/master/image/feature.png)
  * 新建/Behave_pro/features/environment.py 前后依赖函数,类似setup初始化
    * ![feature](https://github.com/linlin547/Python_BDD_behave/blob/master/image/env.png)
  * 新建/Behave_pro/features/steps/test.py 测试步骤文件,对应test.feature中场景
    * ![step](https://github.com/linlin547/Python_BDD_behave/blob/master/image/step.png)

4.behave 执行
-----
  * 进入Behave_pro目录,输入 behave,运行结果
    * ![result](https://github.com/linlin547/Python_BDD_behave/blob/master/image/result.png)

  * 运行结果可以看出,执行了多个场景,当出现失败时,会展示红色字体,标记失败场景

5.参考站点:
-----
  * T先生的博客:
    * http://www.cnblogs.com/tman/p/4115795.html
  * 卡农Lucas的博客
    * http://www.cnblogs.com/devtesters/p/4368318.html
  * 官方Demo
    * http://jenisys.github.io/behave.example/
