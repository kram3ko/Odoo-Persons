from odoo import http
from odoo.http import request


class PersonsController(http.Controller):

    @http.route("/persons", type="http", auth="public", website=True)
    def list_persons(self, **kwargs):
        persons = request.env["my.person"].sudo().search([], limit=5, order="id desc")
        return request.render("persons.person_list_template", {
            "persons": persons
        })

    @http.route(
        "/persons/create",
        type="http",
        auth="public",
        website=True,
        methods=["POST"]
    )
    def create_person(self, **post):
        request.env["my.person"].sudo().create({
            "first_name": post.get("first_name"),
            "last_name": post.get("last_name"),
            "birthday": post.get("birthday") or None,
            "sex": post.get("sex"),
            "company_id": int(post.get("company_id")),
        })
        return request.redirect("/persons")
