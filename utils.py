import os
import sys


LOGO = """
╔══╗─╔══╗╔════╗╔══╗────╔══╗╔══╗╔═══╗╔═══╗╔═══╗
║╔╗║─║╔╗║╚═╗╔═╝║╔═╝────║╔═╝║╔╗║║╔═╗║║╔══╝║╔══╝
║╚╝╚╗║║║║──║║──║╚═╗╔══╗║╚═╗║║║║║╚═╝║║║╔═╗║╚══╗
║╔═╗║║║║║──║║──╚═╗║╚══╝║╔═╝║║║║║╔╗╔╝║║╚╗║║╔══╝
║╚═╝║║╚╝║──║║──╔═╝║────║║──║╚╝║║║║║─║╚═╝║║╚══╗
╚═══╝╚══╝──╚╝──╚══╝────╚╝──╚══╝╚╝╚╝─╚═══╝╚═══╝
https://t.me/bots_forge
"""


def resource_path(relative):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative)
    else:
        return os.path.join(os.path.abspath("."), relative)
