# Changelog

## [0.4.0] - 2023-10-09

-   Add post_params and \*\*payloads params to EsaMdfier.write()
    -   post_params
        -   is expected to be used as additional parameters for the post.
        -   see https://docs.esa.io/posts/102#POST%20/v1/teams/:team_name/posts. Defaults to {}.
    -   \*\*payloads
        -   offers access to piyo which is esa.io client library.
        -   see https://github.com/argonism/piyo/blob/master/piyo/client.py#L112 for details.

## [0.3.1] - 2023-10-09

-   Remove print blended in

## [0.3.0] - 2023-10-07

-   Modify min python version to 3.8

## [0.2.1] - 2023-10-07

-   Modify EsaMdier docstrings

## [0.2.0] - 2023-10-07

-   Add docstrings to stringify_element

## [0.1.1] - 2023-10-07

-   Fix codecov

## [0.1.0] - 2023-10-02

-   First release on PyPI.
