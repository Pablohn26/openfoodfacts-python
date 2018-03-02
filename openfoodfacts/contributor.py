# -*- coding: utf-8 -*-
from . import utils


def get_contributor(username):
    """
    Return information of a given contributor.
    """

    return utils.fetch('contributor/%s' % username)


def get_count(username):
    """
    Return the number of products of a contributor.
    """
    return get_contributor(username)["count"]
