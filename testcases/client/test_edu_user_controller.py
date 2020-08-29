# coding:utf-8

import allure
from common.basic_handler import Basic


@allure.feature("客户端用户相关接口")
class TestEduUserController:

    @allure.story("查询用户信息接口")
    def test_case_1_get_edu_user_info(self):
        api_info = Basic().get_api_by_name("get_user_list")
        content = Basic().send_request(**api_info)
        assert content.status_code == 200

    @allure.story("获取用户课程信息")
    def test_case_2_get_course_order(self):
        api_info = Basic().get_api_by_name("get_course_order")
        content = Basic().send_request(**api_info)
        assert content.status_code == 200