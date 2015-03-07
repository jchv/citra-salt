from collections import OrderedDict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    """
    This is a list of all of the APIs accessible at citra-emu.org.
    # API conventions
    [citra-emu.org](http://citra-emu.org) uses Django REST framework,
    a framework for building RESTful APIs. These APIs follow defacto REST
    conventions.

    A list resource URL will typically look like this:

        /api/[application]/[resource type]/

    Whereas a detail resource URL will typically look like this:

        /api/[application]/[resource type]/[resource id]/

    ## Pagination
    Pagination is simple. All list views provide pagination unless otherwise stated.
    A paginated list contains the following fields:

      * `count`: A count of the total number of items for your query.
      * `next`: A URL for the next page of results for your query.
      * `previous`: A URL for the previous page of results for your query.
      * `results`: An array of objects (or `list-item` elements in XML)
                   for the current page.

    The current pagination scheme for all endpoints is page-based, so in
    addition to the above API, you can also rely on using query string
    parameters to set the page exactly. `page` should be a 1-based integer
    pointing to a valid page number. `page_size` is an optional parameter
    between 1 and 100 specifying how many results should appear on a page.
    (The default, unless otherwise stated, is 10.)

    ## Content types
    Although JSON is the default and preferred format for accessing the API,
    you may also use XML or YAML. The most idiomatic way of doing this is by
    simply sending the right HTTP headers: `Content-Type` for your request
    body, and `Accept` for the response body. In addition, the `format`
    querystring parameter can also override the transport format.

    ## Filtering
    Filtering is done through query string parameters. A list view with
    filtering capabilities should contain documentation on what parameters
    are supported.

    # Application roots
    """
    return Response(OrderedDict([
        ('blog', reverse('api:blog:root', request=request, format=format)),
        ('account', reverse('api:account:root', request=request, format=format)),
    ]))
