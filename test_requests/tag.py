import json

import requests

corpid = 'ww505cb1c1f4f2501d'
corpsecret = 'VvSIXbQeqJ_zBd8GxDp_XptoMcTjT3-9PmQBXDF-LQo'


class Tag:
    def get_token(self):
        r = requests.get(
            'https://qyapi.weixin.qq.com/cgi-bin/gettoken',
            params={
                'corpid': corpid,
                'corpsecret': corpsecret
            }
        )
        self.token = r.json()['access_token']

    def list(self):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/get_corp_tag_list',
            params={'access_token': self.token},
            json={
                'tag_id': []
            }
        )

        print(json.dumps(r.json(),indent=2))

    def add(self, group_id, tags):
        tag = [{'name':tag} for tag in tags]
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/add_corp_tag',
            params={'access_token': self.token},
            json={
                'group_id': group_id,
                'tag.yaml': tag
            }
        )
        print(r.json())
        return r

    def delete(self, group_id):
        r = requests.post(
            'https://qyapi.weixin.qq.com/cgi-bin/externalcontact/del_corp_tag',
            params={'access_token': self.token},
            json={
                'group_id': group_id
            }
        )
