from time import sleep

import pytest


class TestBase:

    @pytest.mark.possitive
    def test_login(self, pm, user):
        pm.login_page.open() \
            .enter_email(user.email()) \
            .enter_pass(user.password()) \
            .click_login_btn()
