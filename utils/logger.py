import json
import logging
import os
import re

import allure
from _pytest.fixtures import SubRequest
from requests import PreparedRequest, Response

from config import Config