# coding:utf-8

from config.global_config import GlobalConfig
from common.basic_handler import Basic
import allure


@allure.feature("后台管理员相关接口")
class TestAdminController:
    cookies = GlobalConfig.cookies
    base_url = GlobalConfig.base_url

    @allure.story("获取某管理员信息")
    def test_case_1_get_admin_info(self):
        api_info = Basic().get_api_by_name("get_admin_by_id")
        content = Basic().send_request(**api_info)
        assert content.status_code == 200

    @allure.story("获取管理员列表")
    def test_case_2_get_admin_list(self):
        api_info = Basic().get_api_by_name("get_admin_list")
        content = Basic().send_request(**api_info)
        assert content.status_code == 200

    @allure.story("通过ID获取管理员信息")
    def test_case_3_get_admin_by_id(self):
        admin_id = "1"
        api_info = Basic().get_api_by_name("get_admin_by_id")
        response = Basic().send_request(admin_id, **api_info)
        assert response.status_code == 200

