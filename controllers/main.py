# Copyright 2018 ACSONE SA/NV
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

from odoo.addons.base_rest.controllers import main


class BaseRestDemoPublicApiController(main.RestController):
    _root_path = "/wolf_gym_api/public/"
    _collection_name = "base.rest.demo.public.services"
    _default_auth = "public"


class BaseRestDemoPrivateApiController(main.RestController):
    _root_path = "/wolf_gym_api/private/"
    _collection_name = "base.rest.demo.private.services"
    _default_auth = "user"


class BaseRestDemoNewApiController(main.RestController):
    _root_path = "/wolf_gym_api/"
    _collection_name = "base.rest.demo.records.services"
    _default_auth = "public"
