# ApiAutomationFrameworkPractice
用来练手的api自动化框架项目，尽可能做到通用

I . 技术栈：
    1. Python 3.7
    2. requests
    3. allure
    4. pytest
II. 执行程序
    run.py文件为主执行文件，进入到项目根目录下，命令行执行：run.py -e=prod -p=client 执行client端对应的api，若-p=server则执行的是server端对应的api；
III. 各模块说明
    1. api_list模块：按照server端和client端分成两个目录，用csv文件格式各自维护对应api；
    2. common模块：主要存放整个框架通用功能脚本，如basic_handler.py包含：获取api名称和api相关信息的方法，发送请求的方法等；
    3. config模块：主要用于获取和处理配置相关信息，如global_config.py包含：获取全局配置相应的信息
    4. envs文件夹：按环境分开，存放各环境的配置信息如host、port等；
    5. logs文件夹：存放运行自动化程序时产生的日志信息；
    6. reports文件夹：存放allure生成的测试报告及报告相应的网页；
    7. testcases模块：以client和server分为两个文件夹，测试集以test_命名，该py脚本中用于编写可执行的api用例；
    8. util模块：工具模块，存放工具类相关信息，如file_handler.py包含：处理csv文件相关方法、json文件处理的相关方法；
    9. 其他：environment.txt 包含指定client 或者 server执行的环境信息；requirements.txt包含该框架所需要的安装包名称和版本信息；
    10. run.py：主程序运行脚本文件，以pytest执行相应case脚本；
    
        
