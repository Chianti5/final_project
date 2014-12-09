__author__ = 'chianti'

from StateCheckinDistribution.CheckinStateExceptions import *


def checkin_state_check(state):
    """
    This function is used to check whether a state is a valid one in the check-in record.
    I.e: whether the state is an element from ['ON', 'EDH', 'MLN', 'WI', 'KHL', 'AZ', 'NV']
    :param state: an abbreviation for a state
    :return: an error if the state is invalid in this case, otherwise pass
    """
    try:
        state = state.upper()
    except:
        raise ValueError

    if state in ['ON', 'EDH', 'MLN', 'WI', 'AZ', 'NV']:
        pass
    else:
        raise InvaldStateForCheckinError('Sorry, invalid state for check-in records.')

