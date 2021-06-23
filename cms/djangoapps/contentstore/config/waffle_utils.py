"""Util methods for Waffle checks"""


from cms.djangoapps.contentstore.config.waffle import ENABLE_CHECKLISTS_QUALITY, CUSTOM_PLS


def should_show_checklists_quality(course_key):
    """
        Determine if the ENABLE_CHECKLISTS_QUALITY waffle flag is set
        and if the user is able to see it
    """
    if ENABLE_CHECKLISTS_QUALITY.is_enabled(course_key):
        return True
    return False


def custom_pls_is_active(course_key):
    """
        Return if custom PLS pacing schedule for self paced courses is active
    """
    return CUSTOM_PLS.is_enabled(course_key)
