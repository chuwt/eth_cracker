# coding: utf-8
"""
Created by chuwt on 18/4/26.
"""
# os

# third
import web3
# self


class ETHClient(object):
    def __init__(self, url):
        self.client = web3.Web3(web3.HTTPProvider("http://" + url))

    def list_account(self):
        print(self.client.personal.listAccounts)


if __name__ == '__main__':
    eth_client = ETHClient('http://51.145.154.204:8545')
    eth_client.list_account()
