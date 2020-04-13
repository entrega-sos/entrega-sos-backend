from flask import url_for

def pagination(query, page, per_page, endpoint, **kwargs):
    resources = query.paginate(page, per_page, False)

    items = []
    if 'Empresas' in str(resources.items):
        for item in resources.items:
            if not item.admin:
                items.append(item.to_json())
            else:
                resources.total = resources.total - 1
    else:
        for item in resources.items:
            items.append(item.to_json())

    data = {
        '_meta': {
            'page': page,
            'per_page': per_page,
            'total_pages': resources.pages,
            'total_items': resources.total
        },
        '_links': {
            'self': url_for(endpoint, page=page, per_page=per_page,
                            **kwargs),
            'next': url_for(endpoint, page=page + 1, per_page=per_page,
                            **kwargs) if resources.has_next else None,
            'prev': url_for(endpoint, page=page - 1, per_page=per_page,
                            **kwargs) if resources.has_prev else None
        },
        'items': items # [item.to_json() for item in resources.items]
    }
    return data